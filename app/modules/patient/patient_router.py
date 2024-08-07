from fastapi import APIRouter, HTTPException

from app.utils.helpers import to_schema
from app.modules.patient import  PatientService,schemas


router = APIRouter(
    prefix="/patient",
    tags=["patient"],
)


@router.get("/{id}")
async def get_paciente(id: int, service:PatientService):
    paciente_data = service.find_patient_by_id(id)
    if paciente_data:
        return to_schema(paciente_data, schemas.PatientResponse)
    else:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")