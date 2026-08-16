from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import Dict, List,Optional,Annotated
class Patient (BaseModel):
    name: Annotated[str, Field(max_length=50, description="The name of the patient",examples=['John Doe', 'Jane Smith'])]
    email:EmailStr
    linked_url:AnyUrl
    age: int = Field(gt=0,lt=120)
    weight:float=Field(gt=0)
    allergies:Optional[List[str]] = None
    contact_details:Dict[str,str]

def insert_patient_data(patient: Patient):
 
     print(patient.name)
     print(patient.age)
     print(patient.weight)
     print(patient.allergies)
     print(patient.contact_details)
     print(patient.linked_url)
     print("Inserted into database")
def update_patient_data(patient: Patient):
    print(f"Updating patient data for {patient.name}...")
    print(f"New age: {patient.age}")
    print(f"New weight: {patient.weight}")
    print(f"New linked URL: {patient.linked_url}")
    print("Updated in database")
patient_info = {'name': 'John Doe','email': 'john.doe@example.com', 'age': 30,'weight': 70.5, 'allergies': ['pollen', 'dust'], 'contact_details': {'phone': '123-456-7890', 'email': 'john.doe@example.com'}, 'linked_url': 'https://example.com/johndoe'}
patient1 = Patient(**patient_info)
insert_patient_data(patient1)
update_patient_data(patient1)
