import requests
import traceback
import json
import base64
from typing import Literal

from utils.config import config
from utils.logger import logger

from src.formater.formater import large_int_to_string
from protobuf.src.cosmospy_protobuf.cosmos.crypto.ed25519.keys_pb2 import PubKey as ed25519_pub_key
from protobuf.src.cosmospy_protobuf.cosmos.crypto.secp256k1.keys_pb2 import PubKey as secp256k1_pub_key
from protobuf.src.cosmospy_protobuf.cosmos.crypto.secp256r1.keys_pb2 import PubKey as secp256r1_pub_key

from protobuf.src.cosmospy_protobuf.cosmos.staking.v1beta1.query_pb2 import (
    QueryValidatorRequest,
    QueryValidatorResponse,
    QueryValidatorsRequest,
    QueryValidatorsResponse,
    QueryParamsRequest as StakingQueryParamsRequest,
    QueryParamsResponse as StakingQueryParamsResponse,
    QueryPoolRequest,
    QueryPoolResponse,
    QueryDelegatorValidatorRequest,
    QueryDelegatorValidatorResponse,
    QueryDelegationRequest,
    QueryDelegationResponse,
    QueryValidatorDelegationsRequest,
    QueryValidatorDelegationsResponse,
    QueryRedelegationsRequest,
    QueryRedelegationsResponse,

    QueryDelegatorDelegationsRequest,
    QueryDelegatorDelegationsResponse,

    QueryUnbondingDelegationRequest,
    QueryUnbondingDelegationResponse,

    QueryValidatorUnbondingDelegationsRequest,
    QueryValidatorUnbondingDelegationsResponse,

    QueryDelegatorUnbondingDelegationsResponse,
    QueryDelegatorUnbondingDelegationsRequest,

    QueryDelegatorValidatorsRequest as StakingQueryDelegatorValidatorsRequest,
    QueryDelegatorValidatorsResponse as StakingQueryDelegatorValidatorsResponse,

    QueryHistoricalInfoRequest,
    QueryHistoricalInfoResponse
)
from protobuf.src.cosmospy_protobuf.cosmos.upgrade.v1beta1.query_pb2 import (
    QueryCurrentPlanRequest,
    QueryCurrentPlanResponse,
)

from protobuf.src.cosmospy_protobuf.cosmos.slashing.v1beta1.query_pb2 import (

    QueryParamsRequest as SlashingQueryParamsRequest,
    QueryParamsResponse as SlashingQueryParamsResponse,
    QuerySigningInfosRequest,
    QuerySigningInfosResponse,
    QuerySigningInfoRequest,
    QuerySigningInfoResponse
)

from protobuf.src.cosmospy_protobuf.cosmos.bank.v1beta1.query_pb2 import (
    QuerySupplyOfRequest,
    QuerySupplyOfResponse,
    QuerySpendableBalanceByDenomRequest,
    QuerySpendableBalanceByDenomResponse,
    QueryBalanceRequest,
    QueryBalanceResponse,
    QueryAllBalancesRequest,
    QueryAllBalancesResponse,
    QuerySpendableBalancesRequest,
    QuerySpendableBalancesResponse,
    QueryTotalSupplyRequest,
    QueryTotalSupplyResponse
)

from protobuf.src.cosmospy_protobuf.cosmos.mint.v1beta1.query_pb2 import (
    QueryInflationRequest,
    QueryInflationResponse,
    QueryParamsRequest as MintQueryParamsRequest,
    QueryParamsResponse as MintQueryParamsResponse,
    QueryAnnualProvisionsRequest,
    QueryAnnualProvisionsResponse
)

from protobuf.src.cosmospy_protobuf.cosmos.distribution.v1beta1.query_pb2 import (
    QueryCommunityPoolRequest,
    QueryCommunityPoolResponse,
    QueryParamsRequest as DistributionQueryParamsRequest,
    QueryParamsResponse as DistributionQueryParamsResponse,
    QueryDelegationTotalRewardsRequest,
    QueryDelegationTotalRewardsResponse,
    QueryDelegationRewardsRequest,
    QueryDelegationRewardsResponse,
    QueryDelegatorValidatorsRequest as DistributionQueryDelegatorValidatorsRequest,
    QueryDelegatorValidatorsResponse as DistributionQueryDelegatorValidatorsResponse,
    QueryDelegatorWithdrawAddressRequest,
    QueryDelegatorWithdrawAddressResponse,
    QueryValidatorDistributionInfoRequest,
    QueryValidatorDistributionInfoResponse,
    QueryValidatorCommissionRequest,
    QueryValidatorCommissionResponse,
    QueryValidatorOutstandingRewardsRequest,
    QueryValidatorOutstandingRewardsResponse,
    QueryValidatorSlashesRequest,
    QueryValidatorSlashesResponse
)

from google.protobuf.json_format import MessageToDict

from protobuf.src.cosmospy_protobuf.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest

class SyncHttpCalls:

    def __init__(self, timeout=10):
        self.rpc = config.Chain.rpc
        self.timeout = timeout
    
    def handle_abci_request(self, callback, hex_data, path, prove=False) -> bytes:
        try:
            payload = {
                "jsonrpc": "2.0",
                "method": "abci_query",
                "params": {
                    "path": path,
                    "data": hex_data,
                    "prove": prove
                },
                "id": -1
            }
            headers = {"Content-Type": "application/json", "Accept": "application/json"}
            response = requests.get(self.rpc, timeout=self.timeout , headers=headers, data=json.dumps(payload))

            if response.status_code == 200:
                response = response.json()
                code = response.get('result', {}).get('response', {}).get('code', 6)
                abci_error_log = response.get('result', {}).get('response', {}).get('log', '')

                if code == 0:
                    response_value = response.get('result', {}).get('response', {}).get('value', '')
                    if not response_value:
                        logger.error(f"ABCI returned 0 code, but with empty response [{payload}]")
                    return {'code': 0, 'data': callback(base64.b64decode(response_value))}
                else:
                    logger.error(f"ABCI retuned {code} code. Payload: {payload}. ABCI log: {abci_error_log}")
                    return {'code': 500, 'message': abci_error_log}
            else:
                logger.error(f"Request to {self.rpc}. Payload: {payload}. failed with status code {response.status_code}")
                return {'code': 500, 'message': 'Internal Server Error: A server-side issue occurred while processing the request.'}
            
        except requests.RequestException as e:
            logger.error(f"Issue with making request to {self.rpc}. Payload: {payload}. {e}")
            return {'code': 500, 'message': 'ABCI Error: A server-side issue occurred while processing the request.'}

        except TimeoutError as e:
            logger.error(f"Issue with making request to {self.rpc}. Payload: {payload}. TimeoutError: {e}")
            return {'code': 500, 'message': 'ABCI Timeout Error: A server-side issue occurred while processing the request.'}

        except Exception as e:
            logger.error(f"An unexpected error occurred: {e}")
            traceback.print_exc()
            return {'code': 500, 'message': 'Internal Server Error: A server-side issue occurred while processing the request.'}

##################################
# Staking
##################################

    def get_validator_staking(self, validator_addr: str):
        query = QueryValidatorRequest(validator_addr=validator_addr)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryValidatorResponse()
            query_response.ParseFromString(response)
            validator = MessageToDict(query_response, preserving_proto_field_name=True)

            if validator['validator'].get('commission',{}).get('commission_rates'):
                if 'rate' in validator['validator']['commission']['commission_rates']:
                    validator['validator']['commission']['commission_rates']['rate'] = large_int_to_string(validator['validator']['commission']['commission_rates']['rate'])
                if 'max_rate' in validator['validator']['commission']['commission_rates']:
                    validator['validator']['commission']['commission_rates']['max_rate'] = large_int_to_string(validator['validator']['commission']['commission_rates']['max_rate'])
                if 'max_change_rate' in validator['validator']['commission']['commission_rates']:
                    validator['validator']['commission']['commission_rates']['max_change_rate'] = large_int_to_string(validator['validator']['commission']['commission_rates']['max_change_rate'])
            
            if validator['validator'].get('delegator_shares'):
                validator['validator']['delegator_shares'] = large_int_to_string(validator['validator']['delegator_shares'])
            if validator['validator'].get('consensus_pubkey'):
                validator['validator']['consensus_pubkey'] = dict(validator['validator']['consensus_pubkey'])

            return validator

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/Validator')

    def get_validators_staking(self, status: Literal["BOND_STATUS_BONDED", "BOND_STATUS_UNBONDED", "BOND_STATUS_UNBONDING", None], pagination: PageRequest):

        query = QueryValidatorsRequest(status=status, pagination=pagination)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryValidatorsResponse()
            query_response.ParseFromString(response)
            validators = MessageToDict(query_response, preserving_proto_field_name=True)

            if validators and validators.get('validators'):
                for validator in validators['validators']:
                    if validator.get('commission',{}).get('commission_rates'):
                        if 'rate' in validator['commission']['commission_rates']:
                            validator['commission']['commission_rates']['rate'] = large_int_to_string(validator['commission']['commission_rates']['rate'])
                        if 'max_rate' in validator['commission']['commission_rates']:
                            validator['commission']['commission_rates']['max_rate'] = large_int_to_string(validator['commission']['commission_rates']['max_rate'])
                        if 'max_change_rate' in validator['commission']['commission_rates']:
                            validator['commission']['commission_rates']['max_change_rate'] = large_int_to_string(validator['commission']['commission_rates']['max_change_rate'])
                            
                    validator['delegator_shares'] = large_int_to_string(validator['delegator_shares'])
                    validator['consensus_pubkey'] = dict(validator['consensus_pubkey'])
            return validators

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/Validators')

    def get_staking_params(self):

        query = StakingQueryParamsRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = StakingQueryParamsResponse()
            query_response.ParseFromString(response)
            params = MessageToDict(query_response, preserving_proto_field_name=True)
            if 'min_commission_rate' in params['params']:
                params['params']['min_commission_rate'] = large_int_to_string(params['params']['min_commission_rate'])

            return params
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/Params')

    def get_token_pool(self):

        query = QueryPoolRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()
        def process_response(response):
            query_response = QueryPoolResponse()
            query_response.ParseFromString(response)
            params = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return params
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/Pool')

    def get_staking_historical_info(self, height: int):

        query = QueryHistoricalInfoRequest(height=height)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryHistoricalInfoResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/HistoricalInfo')
        
    def get_validator_info_for_delegator_validator_pair(self, delegator_addr: str, validator_addr: str):
        
        query = QueryDelegatorValidatorRequest(delegator_addr=delegator_addr, validator_addr=validator_addr)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryDelegatorValidatorResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/DelegatorValidator')

    def get_delegator_info_for_validator_delegator_pair(self, validator_addr: str, delegator_addr: str):

        query = QueryDelegationRequest(delegator_addr=delegator_addr, validator_addr=validator_addr)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryDelegationResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            if data.get('delegation_response',{}).get('delegation',{}).get('shares'):
                data['delegation_response']['delegation']['shares'] =large_int_to_string(data['delegation_response']['delegation']['shares'])
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/Delegation')

    def get_validators_of_delegator_staking(self, delegator_address: str, pagination: PageRequest):

        query = StakingQueryDelegatorValidatorsRequest(delegator_address=delegator_address, pagination=pagination)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = StakingQueryDelegatorValidatorsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            return data

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/StakingDelegatorValidators')
    
    def get_delegator_delegations(self, delegator_addr: str, pagination: PageRequest):

        query = QueryDelegatorDelegationsRequest(delegator_addr=delegator_addr, pagination=pagination)
        
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryDelegatorDelegationsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            if data.get('delegation_responses'):
                for delegation in data['delegation_responses']:
                    if delegation.get('delegation', {}).get('shares'):
                        delegation['delegation']['shares'] = large_int_to_string(delegation['delegation']['shares'])
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/DelegatorDelegations')
    
    def get_validator_delegations(self, validator_addr: str, pagination: PageRequest):
        
        query = QueryValidatorDelegationsRequest(validator_addr=validator_addr, pagination=pagination)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryValidatorDelegationsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/ValidatorDelegations')

    def get_delegator_redelegation(self,
                                   delegator_addr: str,
                                   src_validator_addr: str,
                                   dst_validator_addr: str,
                                   pagination: PageRequest):

        query = QueryRedelegationsRequest(delegator_addr=delegator_addr,
                                          src_validator_addr=src_validator_addr,
                                          dst_validator_addr=dst_validator_addr,
                                          pagination=pagination)
        
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryRedelegationsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/Redelegations')

    def get_validator_unbonding_delegations(self, validator_addr: str, pagination: PageRequest):

        query = QueryValidatorUnbondingDelegationsRequest(validator_addr=validator_addr, pagination=pagination)
        
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryValidatorUnbondingDelegationsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/ValidatorUnbondingDelegations')

    def get_delegator_unbonding_delegations(self, delegator_addr: str, pagination: PageRequest):

        query = QueryDelegatorUnbondingDelegationsRequest(delegator_addr=delegator_addr, pagination=pagination)
        
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryDelegatorUnbondingDelegationsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/DelegatorUnbondingDelegations')

    def get_delegator_validator_pair_unbonding_delegation(self, delegator_addr: str, validator_addr: str):

        query = QueryUnbondingDelegationRequest(delegator_addr=delegator_addr, validator_addr=validator_addr)
        
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryUnbondingDelegationResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.staking.v1beta1.Query/UnbondingDelegation')

    def get_upgrade_info(self):

        query = QueryCurrentPlanRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryCurrentPlanResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.upgrade.v1beta1.Query/CurrentPlan')

    def get_slashing_params(self):

        query = SlashingQueryParamsRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = SlashingQueryParamsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            if 'min_signed_per_window' in data['params']:
                data['params']['min_signed_per_window'] = large_int_to_string(base64.b64decode((data['params']['min_signed_per_window'])).decode('utf-8'))
            if 'slash_fraction_double_sign' in data['params']:
                data['params']['slash_fraction_double_sign'] = large_int_to_string(base64.b64decode((data['params']['slash_fraction_double_sign'])).decode('utf-8'))
            if 'slash_fraction_downtime' in data['params']:
                data['params']['slash_fraction_downtime'] = large_int_to_string(base64.b64decode((data['params']['slash_fraction_downtime'])).decode('utf-8'))

            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.slashing.v1beta1.Query/Params')

    def get_signing_infos(self, pagination: PageRequest):

        query = QuerySigningInfosRequest(pagination=pagination)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QuerySigningInfosResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.slashing.v1beta1.Query/SigningInfos')
    
    def get_signing_info(self, cons_address: str):

        query = QuerySigningInfoRequest(cons_address=cons_address)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QuerySigningInfoResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.slashing.v1beta1.Query/SigningInfo')

    def get_total_supply_by_denom(self, denom: str):

        query = QuerySupplyOfRequest(denom=denom)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QuerySupplyOfResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.bank.v1beta1.Query/SupplyOf')

    def get_total_supply(self, pagination: PageRequest):

        query = QueryTotalSupplyRequest(pagination=pagination)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryTotalSupplyResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.bank.v1beta1.Query/TotalSupply')

    def get_spendable_wallet_balance_by_denom(self, denom: str, address: str):

        query = QuerySpendableBalanceByDenomRequest(address=address, denom=denom)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QuerySpendableBalanceByDenomResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.bank.v1beta1.Query/SpendableBalanceByDenom')
    
    def get_all_spendable_wallet_balances(self, address: str, pagination: PageRequest):

        query = QuerySpendableBalancesRequest(address=address, pagination=pagination)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QuerySpendableBalancesResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.bank.v1beta1.Query/SpendableBalances')

    def get_all_wallet_balance_by_denom(self, denom: str, address: str):

        query = QueryBalanceRequest(address=address, denom=denom)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryBalanceResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.bank.v1beta1.Query/Balance')

    def get_all_wallet_balances(self, address: str, pagination: PageRequest):

        query = QueryAllBalancesRequest(address=address, pagination=pagination)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryAllBalancesResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.bank.v1beta1.Query/AllBalances')

    def get_mint_params(self):

        query = MintQueryParamsRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = MintQueryParamsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            if 'inflation_max' in data['params']:
                data['params']['inflation_max'] = large_int_to_string((data['params']['inflation_max']))
            if 'inflation_min' in data['params']:
                data['params']['inflation_min'] = large_int_to_string((data['params']['inflation_min']))
            if 'goal_bonded' in data['params']:
                data['params']['goal_bonded'] = large_int_to_string((data['params']['goal_bonded']))
            
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.mint.v1beta1.Query/Params')

    def get_inflation(self):

        query = QueryInflationRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryInflationResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            return {'inflation': large_int_to_string(base64.b64decode(data['inflation']).decode('utf-8'))}
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.mint.v1beta1.Query/Inflation')

    def get_annual_provisions(self):

        query = QueryAnnualProvisionsRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryAnnualProvisionsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            return {'annual_provisions': large_int_to_string(base64.b64decode(data['annual_provisions']).decode('utf-8'))}
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.mint.v1beta1.Query/AnnualProvisions')
    
    def get_community_pool(self):

        query = QueryCommunityPoolRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryCommunityPoolResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            for pool in data['pool']:
                pool['amount'] = large_int_to_string(pool['amount'])

            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/CommunityPool')

    def get_distribution_params(self):

        query = DistributionQueryParamsRequest()
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = DistributionQueryParamsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            if 'community_tax' in data['params']:
                data['params']['community_tax'] = large_int_to_string((data['params']['community_tax']))
            if 'base_proposer_reward' in data['params']:
                data['params']['base_proposer_reward'] = large_int_to_string((data['params']['base_proposer_reward']))
            if 'bonus_proposer_reward' in data['params']:
                data['params']['bonus_proposer_reward'] = large_int_to_string((data['params']['bonus_proposer_reward']))
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/Params')
    
    def get_delegation_total_rewards(self, delegator_address: str):

        query = QueryDelegationTotalRewardsRequest(delegator_address=delegator_address)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryDelegationTotalRewardsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            for reward_entry in data.get('rewards', [{}]):
                for reward in reward_entry.get('reward', [{}]):
                    if reward.get('amount'):
                        reward['amount'] = large_int_to_string(reward['amount'])
            
            for total_entry in data.get('total', [{}]):
                if total_entry.get('amount'):
                    total_entry['amount'] = large_int_to_string(total_entry['amount'])

            return data

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/DelegationTotalRewards')

    def get_delegator_validator_pair_rewards(self, delegator_address: str, validator_address: str):

        query = QueryDelegationRewardsRequest(delegator_address=delegator_address, validator_address=validator_address)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryDelegationRewardsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            
            for reward in data.get('rewards', [{}]):
                if reward.get('amount'):
                    reward['amount'] = large_int_to_string(reward['amount'])
            return data

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/DelegationRewards')

    def get_validators_of_delegator_distributions(self, delegator_address: str):

        query = DistributionQueryDelegatorValidatorsRequest(delegator_address=delegator_address)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = DistributionQueryDelegatorValidatorsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            return data

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/DelegatorValidators')

    def get_delegator_withdraw_address(self, delegator_address: str):

        query = QueryDelegatorWithdrawAddressRequest(delegator_address=delegator_address)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryDelegatorWithdrawAddressResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            return data

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/DelegatorWithdrawAddress')

    def get_validator_distribution_info(self, validator_address: str):

        query = QueryValidatorDistributionInfoRequest(validator_address=validator_address)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryValidatorDistributionInfoResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            for reward in data.get('self_bond_rewards', [{}]):
                if reward.get('amount'):
                    reward['amount'] = large_int_to_string(reward['amount'])
            
            for commission_entry in data.get('commission', [{}]):
                if commission_entry.get('amount'):
                    commission_entry['amount'] = large_int_to_string(commission_entry['amount'])
            return data

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/ValidatorDistributionInfo')

    def get_validator_accumulated_commission(self, validator_address: str):

        query = QueryValidatorCommissionRequest(validator_address=validator_address)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryValidatorCommissionResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            for commission_entry in data.get('commission', {}).get('commission', [{}]):
                if commission_entry.get('amount'):
                    commission_entry['amount'] = large_int_to_string(commission_entry['amount'])
            return data

        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/ValidatorCommission')

    def get_validator_outstanding_rewards(self, validator_address: str):

        query = QueryValidatorOutstandingRewardsRequest(validator_address=validator_address)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryValidatorOutstandingRewardsResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)

            for reward in data.get('rewards', {}).get('rewards', [{}]):
                if reward.get('amount'):
                    reward['amount'] = large_int_to_string(reward['amount'])
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/ValidatorOutstandingRewards')
    
    def get_validator_slashes(self, validator_address: str, starting_height: int, ending_height: int, pagination: PageRequest):

        query = QueryValidatorSlashesRequest(validator_address=validator_address, starting_height=starting_height, ending_height=ending_height, pagination=pagination)
        serialized_query = query.SerializeToString()
        hex_data = serialized_query.hex()

        def process_response(response):
            query_response = QueryValidatorSlashesResponse()
            query_response.ParseFromString(response)
            data = MessageToDict(query_response, preserving_proto_field_name=True)
            return data
        
        return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.distribution.v1beta1.Query/ValidatorSlashes')


##################################
# Service
##################################

    # def get_block_with_tx(self, height: int, pagination: PageRequest):

    #     query = GetBlockWithTxsRequest(height=height, pagination=pagination)
    #     serialized_query = query.SerializeToString()
    #     hex_data = serialized_query.hex()

    #     def process_response(response):
    #         query_response = GetBlockWithTxsResponse()
    #         query_response.ParseFromString(response)
    #         data = MessageToDict(query_response, preserving_proto_field_name=True)
    #         return data
        
    #     return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.tx.v1beta1.Service/GetBlockWithTxs')

##################################
# Tendermint
##################################

    # def get_node_info(self) -> dict:

    #     query = GetNodeInfoRequest()
    #     serialized_query = query.SerializeToString()
    #     hex_data = serialized_query.hex()

    #     def process_response(response):
    #         query_response = GetNodeInfoResponse()
    #         query_response.ParseFromString(response)
    #         data = MessageToDict(query_response, preserving_proto_field_name=True)
    #         return data
        
    #     return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.base.tendermint.v1beta1.Service/GetNodeInfo')
    
##################################
# Governance
##################################

    # def get_proposals(self, proposal_status: Literal["PROPOSAL_STATUS_UNSPECIFIED", "PROPOSAL_STATUS_DEPOSIT_PERIOD", "PROPOSAL_STATUS_VOTING_PERIOD", "PROPOSAL_STATUS_PASSED", "PROPOSAL_STATUS_REJECTED", "PROPOSAL_STATUS_FAILED", None],
    #                   voter: str,
    #                   depositor: str,
    #                   pagination: PageRequest
    #                   ) -> dict:
    
    #     query = QueryProposalsRequest(proposal_status=proposal_status)
    #     serialized_query = query.SerializeToString()
    #     hex_data = serialized_query.hex()
    #     def process_response(response):
    #         query_response = QueryProposalsResponse()
    #         query_response.ParseFromString(response)
    #         data = MessageToDict(query_response, preserving_proto_field_name=True)
    #         return data
        
    #     return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.gov.v1.Query/Proposals')
    
    # def get_proposal(self, proposal_id: int):
    #     query = QueryProposalRequest(proposal_id=proposal_id)
    #     serialized_query = query.SerializeToString()
    #     hex_data = serialized_query.hex()
    #     def process_response(response):
    #         query_response = QueryProposalResponse()
    #         query_response.ParseFromString(response)
    #         data = MessageToDict(query_response, preserving_proto_field_name=True)
    #         return data
        
    #     return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.gov.v1.Query/Proposals')

    # def get_gov_params(self, params_type: Literal["voting", "tallying", "deposit"]):
    #     query = QueryParamsRequest(params_type=params_type)
    #     serialized_query = query.SerializeToString()
    #     hex_data = serialized_query.hex()
    #     def process_response(response):
    #         query_response = QueryParamsResponse()
    #         query_response.ParseFromString(response)
    #         data = MessageToDict(query_response, preserving_proto_field_name=True)
    #         return data
        
    #     return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.gov.v1.Query/Params')

##################################
# TX search
##################################

    # def get_blcoks_with_tx(self, events: List[str], pagination: PageRequest, order_by: Literal["ORDER_BY_ASC", "ORDER_BY_DESC", None] = "ORDER_BY_ASC", page: int = 1, limit: int  = 100) -> dict:
    #     # _events = RepeatedScalarFieldContainer(message_listener=events, type_checker=)

    #     query = GetTxsEventRequest(events=events, order_by=order_by, pagination=pagination, page=page, limit=limit)

    #     serialized_query = query.SerializeToString()
    #     hex_data = serialized_query.hex()
    #     def process_response(response):
    #         query_response = GetTxsEventResponse()
    #         query_response.ParseFromString(response)
    #         data = MessageToDict(query_response, preserving_proto_field_name=True)
    #         return data
        
    #     return self.handle_abci_request(callback=process_response, hex_data=hex_data, path='/cosmos.tx.v1beta1.Query/GetTxsEvent') #'/cosmos.tx.v1beta1.Service/GetTxsEvent'

request = SyncHttpCalls()
