from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class CompanionResponse(BaseModel):
    id: int
    response_name: Optional[str] = None
    kinship: Optional[str] = None
    phone: Optional[str] = None 

class PatientResponse(BaseModel):
    id: int
    cpf: Optional[str] = None
    name:Optional[str] = None
    birthday: Optional[str] = None
    address:Optional[str] = None
    responsible_id: Optional[CompanionResponse] = None
    # altura: str
    # adresse: str
    # phone: str
    # whatsapp: str
    # education: str
    # studyTime: str
