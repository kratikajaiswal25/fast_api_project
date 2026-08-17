

from pathlib import Path
from typing_extensions import Annotated
from pydantic import BaseModel, Field,computed_field
from fastapi import FastAPI, HTTPException, Query

class Patient(BaseModel):
    id:Annotated[str, Field(description="The unique identifier for the patient",example='P001')]
    name:Annotated[str, Field(description="The name of the patient",example='John Doe')]
    city:Annotated[str, Field(description="The city where the patient resides",example='New York')]
    age:Annotated[int, Field(description="The age of the patient",example=30)]
    gender:Annotated[str, Field(description="The gender of the patient",example='Male')]
    height:Annotated[float, Field(description="The height of the patient in meters",example=1.75)]
    weight:Annotated[float, Field(description="The weight of the patient in kilograms",example=70.5)]
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)
    @computed_field
    @property  
    def verdict(self)->str:
        if self.bmi <18.5:
            return 'Underweight'
        elif self.bmi<25:
            return 'Normal'
        else:
            return 'Obese'
app = FastAPI()
def load_data():
    import json
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API "}
@app.get('/about')
def about():
    return {"message": "A fully functional API for managing patient data, including BMI calculations and health verdicts."}
@app.get('/view')
def view():
    data = load_data()
    return data
@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="The ID of the patient to retrieve",example='P001')):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")
@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="Sort on the basis of height, weight, or bmi"), order: str = Query('asc', description="Order of sorting: 'asc' or 'desc'")):
    if sort_by not in ['height', 'weight', 'bmi']:
        raise HTTPException(status_code=400, detail="Invalid sort parameter. Use 'height', 'weight', or 'bmi'.")
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order parameter. Use 'asc' or 'desc'.")
    data = load_data()
    sort_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sort_order)
    return sorted_data
@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists.")
    data[patient.id] = patient.dict()
    with open('patients.json', 'w') as f:
        import json
        json.dump(data, f, indent=4)
    return {"message": "Patient created successfully", "patient": patient.dict()}