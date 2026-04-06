from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import date 
from typing import Optional


app = FastAPI()


tasks = {
    1: {
        "task_name" : "python project" ,
        "task_enddate" : "2026-04-30", 
    }
}

class task(BaseModel):
    task_name: str
    task_enddate: date 

class update_task(BaseModel):
  task_name: Optional[str] = None
  task_enddate: Optional[date] = None
  

@app.get("/task/{id}")
def get_task(id:int):
  return tasks[id]

@app.post("/task/{id}")
def post_task(id:int, task:task):
    if id in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks[id] = task.model_dump()
    return tasks 

@app.put("/task/{id}")
def update_taskk(id:int, task:update_task):
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.task_name != None:
        tasks[id]["task_name"] = task.task_name

    if task.task_date != None:
        tasks[id]["task_enddate"] = task.task_enddate
    return tasks[id]

@app.delete("/task{id}")
def delete_student(id:int):
    if id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    del tasks[id]
    return("successfully deleted")
    


