from pydantic import BaseModel
from typing import List, Optional

class FieldValueBase(BaseModel):
    field_id: int
    value: Optional[str] = None
    type: str

class FormFieldBase(BaseModel):
    form_id: Optional[int] = None
    field_id: Optional[int] = None

class FieldBase(BaseModel):
    id: int
    name: Optional[str] = None
    type_id: Optional[int] = None
    has_subfields: Optional[bool] = None
    type_name: Optional[str] = None  

class OptionBase(BaseModel):
    id: int
    field_id: int
    subfield_id: Optional[int] = None 
    name: str
    
class SubFieldBase(BaseModel):
    id: int
    field_id: Optional[int] = None
    parent_id: Optional[int] = None
    name: str
    type: str
    options: Optional[List[OptionBase]] = None 


class FieldWithSubFields(BaseModel):
    id: int
    name: str
    type_id: Optional[int] = None
    type_name: Optional[str] = None
    has_subfields: Optional[bool] = None
    options: Optional[List[OptionBase]] = None
    subfields: Optional[List[SubFieldBase]] = None

class FormBase(BaseModel):
    id: int
    name: Optional[str] = None
    fields: Optional[List[FieldWithSubFields]] = None  
