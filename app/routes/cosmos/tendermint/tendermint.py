# from fastapi import APIRouter, HTTPException
# from app.models.error_models import ErrorResponseModel
# from src.calls.abci_queries import request

# upgrade_router = APIRouter(prefix="/cosmos/tendermint/v1beta1", tags=["Tendermint"], responses={500: {"model": ErrorResponseModel, "description": "Server-side error"}})

# @upgrade_router.get("/node_info",
#                     summary="CurrentPlan queries the current upgrade plan.",
#                     response_model=None)

# def get_upgrade_info():
#     result = request.get_upgrade_info()
#     if result['code'] != 0:
#         raise HTTPException(status_code=500, detail=result['message'])
    
#     return result['data']