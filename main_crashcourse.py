from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class Tea(BaseModel):
    id: int
    name: str
    origin: str


teas: List[Tea] = [] #Teas is a list which has tea data

@app.get("/")
def read_root():
    return {"message": "Welcome to the Tea API"}


@app.get("/teas")
def read_teas():
    return teas


@app.post("/teas")
def create_tea(tea: Tea):
    teas.append(tea)
    return tea

@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for tea in teas:
        if tea.id == tea_id:
            tea.name = updated_tea.name
            tea.origin = updated_tea.origin
            return tea
    return {"message": "Tea not found"}

@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index,tea in enumerate(teas):
        if tea.id == tea_id:
            deleted = teas.pop(index)
            return deleted
    return {"message": "Tea not found"}
    