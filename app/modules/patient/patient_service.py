from app.config.database import Database
from app.modules.patient.patient_model import Patient,Companion


class PatientService:
    def __init__(self, db: Database):
        self.db = db

    @staticmethod
    def normalize_cpf(cpf: str) -> str:
        """Remove pontuações do CPF."""
        if cpf:
            return cpf.replace('.', '').replace('-', '')
        return cpf

    def find_patient_by_id(self, id: int):
        patient = self.db.query(Patient).filter(Patient.id == id).first()
        
        if not patient:
            return None

        patient_data = {
            "id": patient.id,
            "cpf": patient.cpf,
            "name": patient.name,
            "birthday": str(patient.birthday),
            "address": patient.address
        }

        if patient.responsible_id:
            companion = self.db.query(Companion).filter(Companion.id == patient.responsible_id).first()
            if companion:
                patient_data["responsible_id"] = {
                    "id": companion.id,
                    "response_name": companion.name,
                    "phone": companion.phone,
                }

        return patient_data

