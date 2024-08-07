from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from app.config.database import Base

SCHEMA = 'assessment'

class Form(Base):
    __tablename__ = 'forms'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    fields = relationship("FormField", back_populates="form")


class FieldType(Base):
    __tablename__ = 'field_type'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)

    fields = relationship("Field", back_populates="field_type")


class Option(Base):
    __tablename__ = 'options'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True, autoincrement=True)
    field_id = Column(Integer, ForeignKey(f'{SCHEMA}.fields.id'), nullable=True)  
    subfield_id = Column(Integer, ForeignKey(f'{SCHEMA}.subfields.id'), nullable=True) 
    name = Column(String(255), nullable=False)

    field = relationship("Field", back_populates="options")
    subfield = relationship("SubField", back_populates="options")


class Field(Base):
    __tablename__ = 'fields'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type_id = Column(Integer, ForeignKey(f'{SCHEMA}.field_type.id'), nullable=False)
    has_subfields = Column(Boolean, default=False)

    form_fields = relationship("FormField", back_populates="field")
    field_type = relationship("FieldType", back_populates="fields")
    options = relationship("Option", back_populates="field")
    subfields = relationship("SubField", back_populates="field")


class FormField(Base):
    __tablename__ = 'form_fields'
    __table_args__ = {'schema': SCHEMA}

    form_id = Column(Integer, ForeignKey(f'{SCHEMA}.forms.id'), primary_key=True)
    field_id = Column(Integer, ForeignKey(f'{SCHEMA}.fields.id'), primary_key=True)

    form = relationship("Form", back_populates="fields")
    field = relationship("Field", back_populates="form_fields")


class SubField(Base):
    __tablename__ = 'subfields'
    __table_args__ = {'schema': SCHEMA}

    id = Column(Integer, primary_key=True, index=True)
    field_id = Column(Integer, ForeignKey(f'{SCHEMA}.fields.id'), nullable=True)
    parent_id = Column(Integer, ForeignKey(f'{SCHEMA}.subfields.id'), nullable=True)
    name = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)

    field = relationship("Field", back_populates="subfields")
    parent = relationship("SubField", remote_side=[id], back_populates="children")
    children = relationship("SubField", back_populates="parent")
    options = relationship("Option", back_populates="subfield")  