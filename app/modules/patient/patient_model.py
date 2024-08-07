from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from app.config.database import Base



SCHEMA = 'assessment'


class Patient(Base):
    __tablename__ = 'core_patient'
    id = Column(Integer, primary_key=True)
    cpf = Column(String(255))
    name = Column(String(255))
    birthday = Column(DateTime)
    address = Column(String(255))
    responsible_id = Column(Integer, ForeignKey('users_user.id'))
    

class Companion(Base):
    __tablename__ = 'users_user'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    phone = Column(String(255))
    
    


# class PatientCompanion(Base):
#     __tablename__ = 'patient_companion'
#     __table_args__ = {'schema': SCHEMA}
#     id = Column(Integer, primary_key=True, index=True)
#     patient_id = Column(Integer, ForeignKey('patients.id'))
#     companion_id = Column(Integer, ForeignKey('companions.id'))

#     patient = relationship("Patient", back_populates="patient_companions")
#     companion = relationship("Companion", back_populates="patient_companions")
    
    
# class PatientAssessment(Base):
#     __tablename__ = "patients"
#     __table_args__ = {'schema': SCHEMA}
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     cpf = Column(String, unique=True, index=True)
#     birthday = Column(DateTime)
#     gender = Column(String)
#     altura = Column(String)
#     adresse = Column(String)
#     phone = Column(String, index=True)
#     whatsapp = Column(String)
#     education = Column(String)
#     studyTime = Column(String)
    
#     patient_companions = relationship('PatientCompanion', back_populates='patient')

# class CompanionAssessment(Base):
#     __tablename__ = "companions"
#     __table_args__ = {'schema': SCHEMA}
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     kinship = Column(String)
#     phone = Column(String)
    
#     patient_companions = relationship('PatientCompanion', back_populates='companion')