from typing import Annotated
from fastapi import Depends

from app.modules.patient import patient_schema as schemas
from app.modules.patient import patient_service as service

PatientService = Annotated[service.PatientService, Depends(service.PatientService)]

from app.modules.patient.patient_router import router