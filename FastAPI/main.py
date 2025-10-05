from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Tea(BaseModel):
    id: int
    name: str
    origin: str


teas: List[Tea] = []


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}


@app.get("/teas")
def get_teas():
    return teas


@app.post("/teas")
def add_tea(tea: Tea):
    # prevent duplicate ids
    for t in teas:
        if t.id == tea.id:
            raise HTTPException(status_code=400, detail="Tea with this id already exists")
    teas.append(tea)
    return tea


@app.put("/teas/{tea_id}")
def update_tea(tea_id: int, updated_tea: Tea):
    for index, t in enumerate(teas):
        if t.id == tea_id:
            teas[index] = updated_tea
            return updated_tea
    raise HTTPException(status_code=404, detail="Tea not found")


@app.delete("/teas/{tea_id}")
def delete_tea(tea_id: int):
    for index, t in enumerate(teas):
        if t.id == tea_id:
            deleted = teas.pop(index)
            return deleted
    raise HTTPException(status_code=404, detail="Tea not found")
