from fastapi import APIRouter, HTTPException, Depends, Path
from app.models.error_models import ErrorResponseModel
from src.calls.abci_queries import request
from protobuf.src.cosmospy_protobuf.cosmos.base.query.v1beta1.pagination_pb2 import PageRequest
from app.pagination.paginator import get_pagination_params

slashing_router = APIRouter(prefix="/cosmos/slashing/v1beta1", tags=["Slashing"], responses={500: {"model": ErrorResponseModel, "description": "Server-side error"}})

@slashing_router.get("/params",
                    summary="Params queries the parameters of slashing module.",
                    response_model=None)
def get_slashing_params():
    result = request.get_slashing_params()
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@slashing_router.get("/signing_infos",
                    summary="SigningInfos queries signing info of all validators.",
                    response_model=None)
def get_signing_infos(pagination: PageRequest = Depends(get_pagination_params)):
    result = request.get_signing_infos(pagination=pagination)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']

@slashing_router.get("/signing_infos/{cons_address}",
                    summary="SigningInfo queries the signing info of given cons address.",
                    response_model=None)
def get_signing_info(cons_address: str = Path(description="cons_address is the address to query signing info of.")):
    result = request.get_signing_info(cons_address=cons_address)
    if result['code'] != 0:
        raise HTTPException(status_code=500, detail=result['message'])
    
    return result['data']