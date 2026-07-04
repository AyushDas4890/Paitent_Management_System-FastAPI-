from fastapi import FastAPI, Path, HTTPException, Query
from typing import Literal, Annotated, Optional
import json
from fastapi.responses import JSONResponse
from pydantic import BaseModel, computed_field, Field, field_validator

app = FastAPI()

class Patient(BaseModel):
    id: Annotated[str, Field(..., description="Id of the patient", example="P001")]
    name: Annotated[str, Field(..., description="Name of the Patient")]
    city: Annotated[str, Field(..., description="City where the patient belongs to")]
    age: Annotated[int, Field(..., gt=0, lt=120, description="Age of the patient")]
    gender: Annotated[Literal["Male", "Female", "Other"], Field(..., description="Gender of the patient")]

    height: Annotated[float, Field(..., gt=0, lt=30, description="Height of the patient in meters")]
    weight: Annotated[float, Field(..., gt=0, lt=500.0, description="Weight of the patient in kg")]



    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight / (self.height ** 2), 2)

    @computed_field
    @property
    def verdict(self) -> str:
        if self.bmi < 18.5:
            return 'Underweight'
        elif self.bmi < 25:
            return 'Normal'
        elif self.bmi < 30:
            return 'Overweight'
        else:
            return 'Obese'


# New pydantic model for updating patient
class PatientUpdate(BaseModel):
    name: Annotated[Optional[str], Field(default=None)]
    age: Annotated[Optional[int], Field(default=None, gt=0, lt=120)]
    gender: Annotated[Optional[Literal["Male", "Female", "Other"]], Field(default=None)]
    height: Annotated[Optional[float], Field(default=None, gt=0, lt=30)]
    weight: Annotated[Optional[float], Field(default=None, gt=0, lt=500.0)]


def load_data():
    try:
        with open('patient.json', 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}

def save_data(data: dict):
    with open('patient.json', 'w') as f:
        json.dump(data, f)

@app.get("/")
def hello():
    return {'message': 'Patient Management System API'}

@app.get('/about')
def about():
    return {'message': 'A fully functional API to manage your patient records'}

@app.get('/view')
def view():
    data = load_data()
    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id: str = Path(..., description="This is the id of the patient", example="P001")):
    data = load_data()
    patient_data = data.get(patient_id)
    if not patient_data:
        raise HTTPException(status_code=404, detail='Patient not found')
    return patient_data

@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight, or BMI"),
    order: str = Query('asc', description="Sort in asc or desc order")
):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail=f"Invalid field selected. Choose from {valid_fields}")
    data = load_data()
    sorted_order = True if order == 'desc' else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sorted_order)
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()

    #check if the patient already exist
    if patient.id in data:
        raise HTTPException(status_code=400, detail='Patient with same ID already exists')
    
    #new patient add to the database
    data[patient.id] = patient.model_dump(exclude=['id']) # Convert model instance to dictionary before storing because the incoming data is a pydantic object and the data base has data in the form of dictionary

    save_data(data)
    return JSONResponse(status_code=201, content={"message": "Patient created successfully"})


@app.put('/edit/{patient_id}')
def update_patient(patient_id : str, patient_update: PatientUpdate):
    data =load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")

    existing_patient_info = data[patient_id]

    #convert the pydantic output (PatientUpdate) of the pydantic model into a dictionary 
    # as existing_paitent_info is also in dictionary

    updated_patient_info = patient_update.model_dump(exclude_unset=True)

    #Using exclude_unset=True allows you to extract only the fields the user provided, 
    # preventing you from accidentally overwriting existing database fields with default model values.

    for key,value in updated_patient_info.items():
        existing_patient_info[key] = value #example key = "city", value = "mumbai"
        
    #When we change the weight and height , we also have top chang the BMI & Verdict
    # Therefore we will convert the existing_patient_info into a pydantic object(add the id ), then the BMI and verdict will be calculated automatically
    existing_patient_info['id'] = patient_id
    patient_pydantic_obj = Patient(**existing_patient_info)
    # Then we will again convert the pydantic object into a dictionary and follow the below steps
    data[patient_id] = patient_pydantic_obj.model_dump(exclude = 'id')
    save_data(data)
    return JSONResponse(status_code=200, content={"message": "Patient updated successfully"})


@app.delete('/delete/{patient_id}')
def delete_patient(patient_id : str):

    #load data
    data = load_data()

    if patient_id not in data:
        raise HTTPException(status_code=404, detail="Patient not found")
    
    #delete the patient
    del data[patient_id]

    save_data(data)

    return JSONResponse(status_code=200, content={"message": "Patient deleted successfully"})
