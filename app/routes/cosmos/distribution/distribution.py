from fastapi import APIRouter, Depends, HTTPException, Query, Path
from src.calls.abci_queries import request
from app.pagination.paginator import get_pagination_params
from app.models.error_models import ErrorResponseModel
from protobuf.src.cosmospy_protobuf.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest

distribution_router = APIRouter(prefix="/cosmos/distribution/v1beta1", tags=["Distribution"], responses={500: {"model": ErrorResponseModel, "description": "Server-side error"}})

@distribution_router.get("/params",
                    summary="Parameters queries the distribution_router parameters.",
                    response_model=None)
def get_distribution_params():
    result = request.get_distribution_params()
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@distribution_router.get("/pool",
                    summary="CommunityPool queries the community pool coins.",
                    response_model=None)
def get_community_pool():
    result = request.get_community_pool()
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']



@distribution_router.get("/delegators/{delegator_address}/validators",
                    summary="DelegatorValidators queries the validators of a delegator.",
                    response_model=None)
def get_validators_of_delegator_distributions(delegator_address: str = Path(description="delegator_address defines the delegator address to query for.")):
    result = request.get_validators_of_delegator_distributions(delegator_address=delegator_address)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@distribution_router.get("/delegators/{delegator_address}/rewards",
                    summary="DelegationTotalRewards queries the total rewards accrued by a each validator.",
                    response_model=None)
def get_delegation_total_rewards(delegator_address: str = Path(description="delegator_address defines the delegator address to query for.")):
    result = request.get_delegation_total_rewards(delegator_address=delegator_address)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@distribution_router.get("/delegators/{delegator_address}/rewards/{validator_address}",
                    summary="DelegationRewards queries the total rewards accrued by a delegation.",
                    response_model=None)
def get_delegator_validator_pair_rewards(delegator_address: str = Path(description="delegator_address defines the delegator address to query for."),
                                         validator_address: str = Path(description="validator_address defines the validator address to query for.")):
    result = request.get_delegator_validator_pair_rewards(delegator_address=delegator_address, validator_address=validator_address)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@distribution_router.get("/delegators/{delegator_address}/withdraw_address",
                    summary="DelegatorWithdrawAddress queries withdraw address of a delegator.",
                    response_model=None)
def get_delegator_withdraw_address(delegator_address: str = Path(description="delegator_address defines the delegator address to query for.")):
    result = request.get_delegator_withdraw_address(delegator_address=delegator_address)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@distribution_router.get("/validators/{validator_address}",
                    summary="ValidatorDistributionInfo queries validator commission and self-delegation rewards for validator.",
                    response_model=None)
def get_validator_distribution_info(validator_address: str = Path(description="validator_address defines the validator address to query for.")):
    result = request.get_validator_distribution_info(validator_address=validator_address)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@distribution_router.get("/validators/{validator_address}/commission",
                    summary="ValidatorCommission queries accumulated commission for a validator.",
                    response_model=None)
def get_validator_accumulated_commission(validator_address: str = Path(description="validator_address defines the validator address to query for.")):
    result = request.get_validator_accumulated_commission(validator_address=validator_address)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@distribution_router.get("/validators/{validator_address}/outstanding_rewards",
                    summary="ValidatorOutstandingRewards queries rewards of a validator address.",
                    response_model=None)
def get_validator_outstanding_rewards(validator_address: str = Path(description="validator_address defines the validator address to query for.")):
    result = request.get_validator_outstanding_rewards(validator_address=validator_address)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@distribution_router.get("/validators/{validator_address}/slashes",
                    summary="ValidatorSlashes queries slash events of a validator.",
                    response_model=None)
def get_validator_slashes(validator_address: str = Path(description="validator_address defines the validator address to query for."),
                          starting_height = Query(default=None, description="starting_height defines the optional starting height to query the slashes.", ge=0),
                          ending_height = Query(default=None, description="ending_height defines the optional ending height to query the slashes.", ge=0),
                          pagination: PageRequest = Depends(get_pagination_params),
                          ):
    result = request.get_validator_slashes(validator_address=validator_address,
                                           starting_height=starting_height,
                                           ending_height=ending_height,
                                           pagination=pagination
                                           )
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']