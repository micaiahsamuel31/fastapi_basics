from fastapi import FastAPI


app = FastAPI()


tasks = {
    1: {
        "task_name" : "python project" ,
        "task_enddate" : "2026-04-30", 
    }
}

 
@app.get("/")
def root():
    return {"message": "Hello sam"}

