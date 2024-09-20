from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.models.error_models import ErrorResponseModel
from app.routes.cosmos.staking.staking import staking_router
from app.routes.cosmos.upgrade.upgrade import upgrade_router
from app.routes.cosmos.slashing.slashing import slashing_router
from app.routes.cosmos.bank.bank import bank_router
from app.routes.cosmos.mint.mint import mint_router
from app.routes.cosmos.distribution.distribution import distribution_router
from utils.config import config

app = FastAPI(docs_url=config.App.swagger_path if config.App.swagger else None,
              openapi_url='/openapi' if config.App.swagger else None,
              version=config.App.version,
              title=config.App.swagger_title,
              description=config.App.swagger_description)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET"],
    allow_headers=["Content-Type"],
)

app.include_router(staking_router)
app.include_router(upgrade_router)
app.include_router(slashing_router)
app.include_router(bank_router)
app.include_router(mint_router)
app.include_router(distribution_router)

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(request: Request, exc: HTTPException):
    error_response = ErrorResponseModel(code=exc.status_code, message=exc.detail)
    return JSONResponse(
        status_code=exc.status_code,
        content=error_response.model_dump()
    )
