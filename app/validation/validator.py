# from fastapi import HTTPException, Path

# def validate_valoper(validator_addr: str = Path(..., description="validator_addr defines the validator address to query for.")) -> str:
#     if not (25 < len(validator_addr) < 100):
#         raise HTTPException(status_code=400, detail="Invalid valoper address length")
#     if "valoper"  not in validator_addr:
#         raise HTTPException(status_code=400, detail="Invalid valoper address format")
#     return validator_addr