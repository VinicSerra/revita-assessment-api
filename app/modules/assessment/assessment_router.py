from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.config.database import get_db
from app.modules.assessment import AssessmentService, schemas
from app.utils.helpers import to_schema

router = APIRouter(
    prefix="/assessment",
    tags=["Assessment"],
)


@router.get("/forms")
def get_forms(service: AssessmentService):
    forms = service.get_all_forms()
    return forms


@router.get("/initial")
def initial_forms(service: AssessmentService):
    initial_forms = service.initial_forms()
    return initial_forms


@router.get("/{id}")
def find_by_id(id: int,service: AssessmentService):
    forms = service.find_fields_forms(id)
    return forms

# @router.get("/forms/{id}")
# def get_form(id: int, service: AssessmentService  ):
#     """
#     Obtém um formulário pelo ID.
#     """
#     form = service.get_form_by_id(id)
#     if form is None:
#         raise HTTPException(status_code=404, detail="Form not found")
#     return form

# @router.post("/forms")
# def create_form(form_create: schemas.FormCreate, service: AssessmentService  ):
#     """
#     Cria um novo formulário.
#     """
#     return service.create_form(form_create)

# @router.put("/forms/{id}")
# def update_form(id: int, form_update: schemas.FormCreate, service: AssessmentService  ):
#     """
#     Atualiza um formulário existente.
#     """
#     updated_form = service.update_form(id, form_update)
#     if updated_form is None:
#         raise HTTPException(status_code=404, detail="Form not found")
#     return updated_form

# @router.delete("/forms/{id}")
# def delete_form(id: int, service: AssessmentService  ):
#     """
#     Exclui um formulário pelo ID.
#     """
#     if not service.delete_form(id):
#         raise HTTPException(status_code=404, detail="Form not found")
#     return {"message": "Form deleted successfully"}


# @router.get("/fields")
# def get_fields(service: AssessmentService):
#     """
#     Obtém todos os campos.
#     """
#     return service.get_all_fields()

# @router.get("/fields/{id}")
# def get_field(id: int, service: AssessmentService):
#     """
#     Obtém um campo pelo ID.
#     """
#     field = service.get_field_by_id(id)
#     if field is None:
#         raise HTTPException(status_code=404, detail="Field not found")
#     return field

# @router.post("/fields",  )
# def create_field(field_create: schemas.FieldCreate, service: AssessmentService  ):
#     """
#     Cria um novo campo.
#     """
#     return service.create_field(field_create)

# @router.put("/fields/{id}")
# def update_field(id: int, field_update: schemas.FieldCreate, service: AssessmentService  ):
#     """
#     Atualiza um campo existente.
#     """
#     updated_field = service.update_field(id, field_update)
#     if updated_field is None:
#         raise HTTPException(status_code=404, detail="Field not found")
#     return updated_field

# @router.delete("/fields/{id}")
# def delete_field(id: int, service: AssessmentService ):
#     """
#     Exclui um campo pelo ID.
#     """
#     if not service.delete_field(id):
#         raise HTTPException(status_code=404, detail="Field not found")
#     return {"message": "Field deleted successfully"}


# @router.get("/options")
# def get_options(service: AssessmentService):
#     """
#     Obtém todas as opções.
#     """
#     return service.get_all_options()

# @router.get("/options/{id}")
# def get_option(id: int, service: AssessmentService):
#     """
#     Obtém uma opção pelo ID.
#     """
#     option = service.get_option_by_id(id)
#     if option is None:
#         raise HTTPException(status_code=404, detail="Option not found")
#     return option

# @router.post("/options")
# def create_option(option_create: schemas.OptionCreate, service: AssessmentService  ):
#     """
#     Cria uma nova opção.
#     """
#     return service.create_option(option_create)

# @router.put("/options/{id}")
# def update_option(id: int, option_update: schemas.OptionCreate, service: AssessmentService  ):
#     """
#     Atualiza uma opção existente.
#     """
#     updated_option = service.update_option(id, option_update)
#     if updated_option is None:
#         raise HTTPException(status_code=404, detail="Option not found")
#     return updated_option

# @router.delete("/options/{id}")
# def delete_option(id: int, service: AssessmentService  ):
#     """
#     Exclui uma opção pelo ID.
#     """
#     if not service.delete_option(id):
#         raise HTTPException(status_code=404, detail="Option not found")
#     return {"message": "Option deleted successfully"}

# # FormValue Endpoints
# @router.get("/form-values")
# def get_form_values(service: AssessmentService  ):
#     """
#     Obtém todos os valores de formulário.
#     """
#     return service.get_all_form_values()

# @router.get("/form-values/{id}")
# def get_form_value(id: int, service: AssessmentService  ):
#     """
#     Obtém um valor de formulário pelo ID.
#     """
#     form_value = service.get_form_value_by_id(id)
#     if form_value is None:
#         raise HTTPException(status_code=404, detail="Form value not found")
#     return form_value

# @router.post("/form-values")
# def create_form_value(form_value_create: schemas.FormValueCreate, service: AssessmentService  ):
#     """
#     Cria um novo valor de formulário.
#     """
#     return service.create_form_value(form_value_create)

# @router.put("/form-values/{id}")
# def update_form_value(id: int, form_value_update: schemas.FormValueCreate, service: AssessmentService  ):
#     """
#     Atualiza um valor de formulário existente.
#     """
#     updated_form_value = service.update_form_value(id, form_value_update)
#     if updated_form_value is None:
#         raise HTTPException(status_code=404, detail="Form value not found")
#     return updated_form_value

# @router.delete("/form-values/{id}")
# def delete_form_value(id: int, service: AssessmentService  ):
#     """
#     Exclui um valor de formulário pelo ID.
#     """
#     if not service.delete_form_value(id):
#         raise HTTPException(status_code=404, detail="Form value not found")
#     return {"message": "Form value deleted successfully"}

# # FieldValue Endpoints
# @router.get("/field-values")
# def get_field_values(service: AssessmentService  ):
#     """
#     Obtém todos os valores de campo.
#     """
#     return service.get_all_field_values()

# @router.get("/field-values/{id}")
# def get_field_value(id: int, service: AssessmentService  ):
#     """
#     Obtém um valor de campo pelo ID.
#     """
#     field_value = service.get_field_value_by_id(id)
#     if field_value is None:
#         raise HTTPException(status_code=404, detail="Field value not found")
#     return field_value

# @router.post("/field-values")
# def create_field_value(field_value_create: schemas.FieldValueCreate, service: AssessmentService ):
#     """
#     Cria um novo valor de campo.
#     """
#     return service.create_field_value(field_value_create)

# @router.put("/field-values/{id}")
# def update_field_value(id: int, field_value_update: schemas.FieldValueCreate, service: AssessmentService):
#     """
#     Atualiza um valor de campo existente.
#     """
#     updated_field_value = service.update_field_value(id, field_value_update)
#     if updated_field_value is None:
#         raise HTTPException(status_code=404, detail="Field value not found")
#     return updated_field_value

# @router.delete("/field-values/{id}",)
# def delete_field_value(id: int, service: AssessmentService):
#     """
#     Exclui um valor de campo pelo ID.
#     """
#     if not service.delete_field_value(id):
#         raise HTTPException(status_code=404, detail="Field value not found")
#     return {"message": "Field value deleted successfully"}
