from fastapi import APIRouter, HTTPException
from app.models.error_models import ErrorResponseModel

from src.calls.abci_queries import request

mint_router = APIRouter(prefix="/cosmos/mint/v1beta1", tags=["Mint"], responses={500: {"model": ErrorResponseModel, "description": "Server-side error"}})

@mint_router.get("/params",
                    summary="Params queries the parameters of x/mint module.",
                    response_model=None)
def get_mint_params():
    result = request.get_mint_params()

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@mint_router.get("/inflation",
                    summary="Inflation queries the parameters of inflation.",
                    response_model=None)
def get_mint_params():
    result = request.get_inflation()

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

@mint_router.get("/annual_provisions",
                    summary="Annual_provisions queries annual_provisions.",
                    response_model=None)
def get_mint_params():
    result = request.get_annual_provisions()

    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])

    return result['data']

