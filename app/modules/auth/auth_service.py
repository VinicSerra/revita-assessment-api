from fastapi import APIRouter,HTTPException
from pydantic import BaseModel

from app.utils.helpers import to_schema
from app.modules.assessment import AssessmentService,schemas
import httpx


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.get("/TypeAssessment")


class TokenRequest(BaseModel):
    decryptedToken: str

@router.post("/external-request")
async def external_request(request: TokenRequest):
    url = "http://localhost:8000/api/users/me/"
    
    # Cria os headers com o token fornecido
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Authorization": f"Bearer {request.decryptedToken}",
        "Connection": "keep-alive",
        "Host": "localhost:8000",
        "Origin": "http://127.0.0.1:3000",
        "Referer": "http://127.0.0.1:3000/",
        "Sec-CH-UA": '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "cross-site",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers)

    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail=response.text)

    return response.json()