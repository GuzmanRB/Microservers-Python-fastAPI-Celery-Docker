
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from ..ms_celery_worker.celTask import writeFile

app=FastAPI()

@app.get('/')
def home():
    return {"Message":"Hola mundo"}
@app.get('/file')
def writeFile():
    result=writeFile(2)
    return JSONResponse({"RESULT":result})
