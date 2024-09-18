from fastapi import APIRouter, HTTPException, Query, Depends, Path
from protobuf.src.cosmospy_protobuf.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest
from app.models.error_models import ErrorResponseModel
from app.pagination.paginator import get_pagination_params

from src.calls.abci_queries import request

bank_router = APIRouter(prefix="/cosmos/bank/v1beta1", tags=["Bank"], responses={500: {"model": ErrorResponseModel, "description": "Server-side error"}})

@bank_router.get("/supply/by_denom",
                    summary="SupplyOf queries the supply of a single coin.",
                    response_model=None)
def get_total_supply_by_denom(
    denom: str = Query(description="denom is the coin denom to query balances for.")):
    result = request.get_total_supply_by_denom(denom)

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@bank_router.get("/supply",
                    summary="TotalSupply queries the total supply of all coins.",
                    response_model=None)
def get_total_supply(pagination: PageRequest = Depends(get_pagination_params)):
    result = request.get_total_supply(pagination=pagination)

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@bank_router.get("/spendable_balances/{address}/by_denom",
                    summary="SpendableBalanceByDenom queries the spendable balance of a single denom for a single account.",
                    response_model=None)
def get_spendable_wallet_balance_by_denom(address: str = Path(description="address is the address to query balances for"),
                                          denom: str = Query(description="denom is the coin denom to query balances for.")):
    result = request.get_spendable_wallet_balance_by_denom(denom=denom, address=address)

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@bank_router.get("/spendable_balances/{address}",
                    summary="SpendableBalances queries the spendable balance of all coins for a single account.",
                    response_model=None)
def get_all_spendable_wallet_balances(address: str = Path(description="address is the address to query balances for"),
                              pagination: PageRequest = Depends(get_pagination_params)):
    result = request.get_all_spendable_wallet_balances(address=address, pagination=pagination)

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@bank_router.get("/balances/{address}/by_denom",
                    summary="Balance queries the balance of a single coin for a single account.",
                    response_model=None)
def get_all_wallet_balance_by_denom(address: str = Path(description="address is the address to query balances for"),
                                    denom: str = Query(description="denom is the coin denom to query balances for.")):
    result = request.get_all_wallet_balance_by_denom(denom=denom, address=address)

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@bank_router.get("/balances/{address}",
                    summary="AllBalances queries the balance of all coins for a single account.",
                    response_model=None)
def get_all_wallet_balance_by_denom(address: str = Path(description="address is the address to query balances for"),
                                    pagination: PageRequest = Depends(get_pagination_params)):
    result = request.get_all_wallet_balances(address=address,pagination=pagination)

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']