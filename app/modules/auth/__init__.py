from typing import Annotated
from fastapi import Depends

# from app.modules.assessment import assessment_service as service

# AssessmentService = Annotated[service.AssessmentService, Depends(service.AssessmentService)]

from app.modules.auth.auth_service import router