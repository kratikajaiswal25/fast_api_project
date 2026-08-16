from pydantic import BaseModel, Field, ValidationError, validator
from typing import List, Optional, Dict, Any
class Patient(BaseModel):
    name:str
    email:str
    weight:float
    married:bool
    allergies:List[str]
    contact_details:Dict[str,str]
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=['hdfc.com','gmail.com','yahoo.com']
        #abc@gmail.com
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError("Invalid email domain")
        return value
    @field_validator('name',mode='after')
    @classmethod
    def name_validator(cls,value):
        return value.upper()
    @field_validator('age',mode='after')
    @classmethod
    def validate_age(cls,value):
        if value<0 or value>120:
            raise ValueError("Age must be between 0 and 120")
        return value

def update_patient_data(patient: Patient):
    print(f"Updating patient data for {patient.name}...")
    print(f"New email: {patient.email}")
    print(f"New weight: {patient.weight}")
    print(f"Married status: {patient.married}")
    print(f"Allergies: {patient.allergies}")
    print(f"Contact details: {patient.contact_details}")
    print("Updated in database")
patient_info = {'name': 'John Doe', 'email': 'john.doe@example.com', 'weight': 70.5, 'married': True, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com'}}
patient1 = Patient(**patient_info)
update_patient_data(patient1)