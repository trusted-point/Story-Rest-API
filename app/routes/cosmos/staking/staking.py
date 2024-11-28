from fastapi import APIRouter, Depends, HTTPException, Query, Path
from src.calls.abci_queries import request
from app.pagination.paginator import get_pagination_params
from app.models.error_models import ErrorResponseModel
from protobuf.src.cosmospy_protobuf.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest
from typing import Literal

staking_router = APIRouter(prefix="/cosmos/staking/v1beta1", tags=["Staking"], responses={500: {"model": ErrorResponseModel, "description": "Server-side error"}})

@staking_router.get("/params",
                    summary="Parameters queries the staking parameters.",
                    response_model=None)
def get_staking_params():
    result = request.get_staking_params()
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/pool",
                    summary="Pool queries the pool info.",
                    response_model=None)
def get_token_pool():
    result = request.get_token_pool()
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/validators",
                    summary="Validators queries all validators that match the given status.",
                    response_model=None)
def get_validators(
    status: Literal["BOND_STATUS_BONDED", "BOND_STATUS_UNBONDED", "BOND_STATUS_UNBONDING", ""] = Query(default=None, description="status enables to query for validators matching a given status."),
    pagination: PageRequest = Depends(get_pagination_params)):

    result = request.get_validators_staking(status=status, pagination=pagination)

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@staking_router.get("/validators/{validator_addr}",
                    summary="Validator queries validator info for given validator address.",
                    response_model=None)
def get_validator_by_valoper(
    validator_addr: str = Path(description="The address of the validator whose information is being queried.")):
    result = request.get_validator_staking(validator_addr)

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@staking_router.get("/validators/{validator_addr}/delegations",
                    summary="ValidatorDelegations queries delegate info for given validator.",
                    response_model=None)
def get_validator_delegations(
    validator_addr: str = Path(description="validator_addr defines the validator address to query for."),
    pagination: PageRequest = Depends(get_pagination_params)):
    result = request.get_validator_delegations(validator_addr=validator_addr, pagination=pagination)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/validators/{validator_addr}/delegations/{delegator_addr}",
                    summary="Delegation queries delegate info for given validator delegator pair.",
                    response_model=None)
def get_delegator_validator_pair(
    validator_addr: str = Path(description="validator_addr defines the validator address to query for."),
    delegator_addr: str = Path(description="delegator_addr defines the delegator address to query for.")):
    result = request.get_delegator_info_for_validator_delegator_pair(delegator_addr=delegator_addr, validator_addr=validator_addr)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/validators/{validator_addr}/unbonding_delegations",
                    summary="ValidatorUnbondingDelegations queries unbonding delegations of a validator.",
                    response_model=None)
def get_validator_unbonding_delegations(validator_addr: str = Path(description="validator_addr defines the validator address to query for."),
                                        pagination: PageRequest = Depends(get_pagination_params)):
    result = request.get_validator_unbonding_delegations(validator_addr=validator_addr, pagination=pagination)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/validators/{validator_addr}/delegations/{delegator_addr}/unbonding_delegation",
                    summary="UnbondingDelegation queries unbonding info for given validator delegator.",
                    response_model=None)
def get_delegator_validator_pair_unbonding_delegation(
    validator_addr: str = Path(description="validator_addr defines the validator address to query for."),
    delegator_addr: str = Path(description="delegator_addr defines the delegator address to query for.")):
    
    result = request.get_delegator_validator_pair_unbonding_delegation(validator_addr=validator_addr, delegator_addr=delegator_addr)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/delegators/{delegator_addr}/unbonding_delegations",
                    summary="DelegatorUnbondingDelegations queries all unbonding delegations of a given delegator address.",
                    response_model=None)
def get_delegator_unbonding_delegations(
    delegator_addr: str = Path(description="delegator_addr defines the delegator address to query for."),
    pagination: PageRequest = Depends(get_pagination_params)):
    
    result = request.get_delegator_unbonding_delegations(validator_addr=delegator_addr, pagination=pagination)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

### redelegations
@staking_router.get("/delegators/{delegator_addr}/redelegations",
                    summary="Redelegations queries redelegations of given address.",
                    response_model=None)
def get_delegator_unbonding_delegations(
    delegator_addr: str = Path(description="delegator_addr defines the delegator address to query for."),
    src_validator_addr: str = Path(description="src_validator_addr defines the validator address to redelegate from."),
    dst_validator_addr: str = Path(description="dst_validator_addr defines the validator address to redelegate to."),
    pagination: PageRequest = Depends(get_pagination_params)):
    
    result = request.get_delegator_redelegation(delegator_addr=delegator_addr, src_validator_addr=src_validator_addr, dst_validator_addr=dst_validator_addr, pagination=pagination)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/delegators/{delegator_addr}/validators",
                    summary="DelegatorValidators queries the validators of a delegator.",
                    response_model=None)
def get_validators_of_delegator_staking(
    delegator_addr: str = Path(description="delegator_addr defines the delegator address to query for."),
    pagination: PageRequest = Depends(get_pagination_params)):
    
    result = request.get_validators_of_delegator_staking(validator_addr=delegator_addr, pagination=pagination)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/delegators/{delegator_addr}/validators/{validator_addr}",
                    summary="DelegatorValidator queries validator info for given delegator validator pair.",
                    response_model=None)
def get_validator_info_for_delegator_validator_pair(
    delegator_addr: str = Path(description="delegator_addr defines the delegator address to query for."),
    validator_addr: str = Path(description="validator_addr defines the validator address to query for.")):
    
    result = request.get_validator_info_for_delegator_validator_pair(delegator_addr=delegator_addr, validator_addr=validator_addr)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@staking_router.get("/delegations/{delegator_addr}",
                    summary="DelegatorDelegations queries all delegations of a given delegator address.",
                    response_model=None)
def get_delegator_delegations(
    delegator_addr: str = Path(description="delegator_addr defines the delegator address to query for."),
    pagination: PageRequest = Depends(get_pagination_params)):
    
    result = request.get_delegator_delegations(delegator_addr=delegator_addr, pagination=pagination)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']