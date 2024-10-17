from sqlalchemy.orm import joinedload

from typing import List,Optional,Dict
from sqlalchemy import and_
from app.config.database import Database
from app.modules.assessment.assessment_model import Form,Field,FormField,SubField

from app.modules.assessment.assessment_schemas import  FormBase

class AssessmentService:
    
    def __init__(self, db: Database) -> None:
        self.db = db


    def get_all_forms(self):
            """
            Obtém todos os formulários.
            """
            forms = self.db.query(Form).all()
            return [FormBase(**form.__dict__) for form in forms]
    
    
    
    def initial_forms(self):
        """
        Obtém formulários iniciais com ids específicos, ordenados por id.
        """
        forms = (
            self.db.query(Form)
            .options(
                joinedload(Form.fields)
                .joinedload(FormField.field)  
            )
            .filter(Form.id.in_([1, 2]))
            .order_by(Form.id)  
            .all()
        )
        
        result = []
        for form in forms:
            sorted_fields = sorted(form.fields, key=lambda x: getattr(x, 'some_other_field', 0))  
            
            form_data = {
                "id": form.id,
                "name": form.name,
                "fields": [
                    {
                        "id": form_field.field.id,
                        "name": form_field.field.name,
                        "type_id": form_field.field.type_id,
                        "type_name": form_field.field.field_type.name if form_field.field.field_type else None,
                        "has_subfields": form_field.field.has_subfields,
                        "options": [
                            {"id": option.id, "name": option.name}
                            for option in sorted(form_field.field.options, key=lambda x: getattr(x, 'id', 0)) 
                        ] if form_field.field.options else []
                    }
                    for form_field in sorted_fields
                ]
            }
            result.append(form_data)

        return result
            
    
    def find_fields_forms(self, id: int):
        """
        Obtém formulários iniciais com ids específicos, ordenados por id.
        """
        form = (
            self.db.query(Form)
            .options(
                joinedload(Form.fields)
                .joinedload(FormField.field)
                .joinedload(Field.subfields) 
                .joinedload(SubField.options)
            )
            .filter(Form.id == id)
            .order_by(Form.id)
            .first() 
        )
        
        if not form:
            return None  
        
        sorted_fields = form.fields  
        
        def process_subfields(subfields):
            """
            Processa uma lista de subcampos recursivamente.
            """
            return [
                {
                    "id": subfield.id,
                    "field_id": subfield.field_id,
                    "parent_id": subfield.parent_id,
                    "name": subfield.name,
                    "type": subfield.type,
                    "options": [
                        {"id": option.id, "name": option.name}
                        for option in sorted(subfield.options, key=lambda x: getattr(x, 'id', 0))
                    ] if subfield.options else [],
                    "children": process_subfields(subfield.children) if subfield.children else []
                }
                for subfield in subfields
            ]
        
        form_data = {
            "id": form.id,
            "name": form.name,
            "fields": [
                {
                    "id": form_field.field.id,
                    "name": form_field.field.name,
                    "type_id": form_field.field.type_id,
                    "type_name": form_field.field.field_type.name if form_field.field.field_type else None,
                    "has_subfields": form_field.field.has_subfields,
                    "options": [
                        {"id": option.id, "name": option.name}
                        for option in sorted(form_field.field.options, key=lambda x: getattr(x, 'id', 0))
                    ] if form_field.field.options else [],
                    "subfields": process_subfields(form_field.field.subfields) if form_field.field.subfields else []
                }
                for form_field in sorted_fields
            ]
        }

        return form_data


    # def create_form(self, form_create: FormCreate) -> FormResponse:
    #     """
    #     Cria um novo formulário.
    #     """
    #     form = Form(**form_create.dict())
    #     self.db.add(form)
    #     self.db.commit()
    #     self.db.refresh(form)
    #     return FormResponse.from_orm(form)

    # def update_form(self, id: int, form_update: FormCreate) -> Optional[FormResponse]:
    #     """
    #     Atualiza um formulário existente.
    #     """
    #     form = self.db.query(Form).filter(Form.id == id).first()
    #     if form:
    #         for key, value in form_update.dict().items():
    #             setattr(form, key, value)
    #         self.db.commit()
    #         self.db.refresh(form)
    #         return FormResponse.from_orm(form)
    #     return None

    # def delete_form(self, id: int) -> bool:
    #     """
    #     Exclui um formulário pelo ID.
    #     """
    #     form = self.db.query(Form).filter(Form.id == id).first()
    #     if form:
    #         self.db.delete(form)
    #         self.db.commit()
    #         return True
    #     return False

    # # Field Methods
    # def get_all_fields(self) -> List[FieldResponse]:
    #     """
    #     Obtém todos os campos.
    #     """
    #     fields = self.db.query(Field).all()
    #     return [FieldResponse.from_orm(field) for field in fields]

    # def get_field_by_id(self, id: int) -> Optional[FieldResponse]:
    #     """
    #     Obtém um campo pelo ID.
    #     """
    #     try:
    #         field = self.db.query(Field).filter(Field.id == id).one()
    #         return FieldResponse.from_orm(field)
    #     except NoResultFound:
    #         return None

    # def create_field(self, field_create: FieldCreate) -> FieldResponse:
    #     """
    #     Cria um novo campo.
    #     """
    #     field = Field(**field_create.dict())
    #     self.db.add(field)
    #     self.db.commit()
    #     self.db.refresh(field)
    #     return FieldResponse.from_orm(field)

    # def update_field(self, id: int, field_update: FieldCreate) -> Optional[FieldResponse]:
    #     """
    #     Atualiza um campo existente.
    #     """
    #     field = self.db.query(Field).filter(Field.id == id).first()
    #     if field:
    #         for key, value in field_update.dict().items():
    #             setattr(field, key, value)
    #         self.db.commit()
    #         self.db.refresh(field)
    #         return FieldResponse.from_orm(field)
    #     return None

    # def delete_field(self, id: int) -> bool:
    #     """
    #     Exclui um campo pelo ID.
    #     """
    #     field = self.db.query(Field).filter(Field.id == id).first()
    #     if field:
    #         self.db.delete(field)
    #         self.db.commit()
    #         return True
    #     return False

    # # Option Methods
    # def get_all_options(self) -> List[OptionResponse]:
    #     """
    #     Obtém todas as opções.
    #     """
    #     options = self.db.query(Option).all()
    #     return [OptionResponse.from_orm(option) for option in options]

    # def get_option_by_id(self, id: int) -> Optional[OptionResponse]:
    #     """
    #     Obtém uma opção pelo ID.
    #     """
    #     try:
    #         option = self.db.query(Option).filter(Option.id == id).one()
    #         return OptionResponse.from_orm(option)
    #     except NoResultFound:
    #         return None

    # def create_option(self, option_create: OptionCreate) -> OptionResponse:
    #     """
    #     Cria uma nova opção.
    #     """
    #     option = Option(**option_create.dict())
    #     self.db.add(option)
    #     self.db.commit()
    #     self.db.refresh(option)
    #     return OptionResponse.from_orm(option)

    # def update_option(self, id: int, option_update: OptionCreate) -> Optional[OptionResponse]:
    #     """
    #     Atualiza uma opção existente.
    #     """
    #     option = self.db.query(Option).filter(Option.id == id).first()
    #     if option:
    #         for key, value in option_update.dict().items():
    #             setattr(option, key, value)
    #         self.db.commit()
    #         self.db.refresh(option)
    #         return OptionResponse.from_orm(option)
    #     return None

    # def delete_option(self, id: int) -> bool:
    #     """
    #     Exclui uma opção pelo ID.
    #     """
    #     option = self.db.query(Option).filter(Option.id == id).first()
    #     if option:
    #         self.db.delete(option)
    #         self.db.commit()
    #         return True
    #     return False

    # # FormValue Methods
    # def get_all_form_values(self) -> List[FormValueResponse]:
    #     """
    #     Obtém todos os valores de formulário.
    #     """
    #     form_values = self.db.query(FormValue).all()
    #     return [FormValueResponse.from_orm(form_value) for form_value in form_values]

    # def get_form_value_by_id(self, id: int) -> Optional[FormValueResponse]:
    #     """
    #     Obtém um valor de formulário pelo ID.
    #     """
    #     try:
    #         form_value = self.db.query(FormValue).filter(FormValue.id == id).one()
    #         return FormValueResponse.from_orm(form_value)
    #     except NoResultFound:
    #         return None

    # def create_form_value(self, form_value_create: FormValueCreate) -> FormValueResponse:
    #     """
    #     Cria um novo valor de formulário.
    #     """
    #     form_value = FormValue(**form_value_create.dict())
    #     self.db.add(form_value)
    #     self.db.commit()
    #     self.db.refresh(form_value)
    #     return FormValueResponse.from_orm(form_value)

    # def update_form_value(self, id: int, form_value_update: FormValueCreate) -> Optional[FormValueResponse]:
    #     """
    #     Atualiza um valor de formulário existente.
    #     """
    #     form_value = self.db.query(FormValue).filter(FormValue.id == id).first()
    #     if form_value:
    #         for key, value in form_value_update.dict().items():
    #             setattr(form_value, key, value)
    #         self.db.commit()
    #         self.db.refresh(form_value)
    #         return FormValueResponse.from_orm(form_value)
    #     return None

    # def delete_form_value(self, id: int) -> bool:
    #     """
    #     Exclui um valor de formulário pelo ID.
    #     """
    #     form_value = self.db.query(FormValue).filter(FormValue.id == id).first()
    #     if form_value:
    #         self.db.delete(form_value)
    #         self.db.commit()
    #         return True
    #     return False

    # # FieldValue Methods
    # def get_all_field_values(self) -> List[FieldValueResponse]:
    #     """
    #     Obtém todos os valores de campo.
    #     """
    #     field_values = self.db.query(FieldValue).all()
    #     return [FieldValueResponse.from_orm(field_value) for field_value in field_values]

    # def get_field_value_by_id(self, id: int) -> Optional[FieldValueResponse]:
    #     """
    #     Obtém um valor de campo pelo ID.
    #     """
    #     try:
    #         field_value = self.db.query(FieldValue).filter(FieldValue.id == id).one()
    #         return FieldValueResponse.from_orm(field_value)
    #     except NoResultFound:
    #         return None

    # def create_field_value(self, field_value_create: FieldValueCreate) -> FieldValueResponse:
    #     """
    #     Cria um novo valor de campo.
    #     """
    #     field_value = FieldValue(**field_value_create.dict())
    #     self.db.add(field_value)
    #     self.db.commit()
    #     self.db.refresh(field_value)
    #     return FieldValueResponse.from_orm(field_value)

    # def update_field_value(self, id: int, field_value_update: FieldValueCreate) -> Optional[FieldValueResponse]:
    #     """
    #     Atualiza um valor de campo existente.
    #     """
    #     field_value = self.db.query(FieldValue).filter(FieldValue.id == id).first()
    #     if field_value:
    #         for key, value in field_value_update.dict().items():
    #             setattr(field_value, key, value)
    #         self.db.commit()
    #         self.db.refresh(field_value)
    #         return FieldValueResponse.from_orm(field_value)
    #     return None

    # def delete_field_value(self, id: int) -> bool:
    #     """
    #     Exclui um valor de campo pelo ID.
    #     """
    #     field_value = self.db.query(FieldValue).filter(FieldValue.id == id).first()
    #     if field_value:
    #         self.db.delete(field_value)
    #         self.db.commit()
    #         return True
    #     return False
