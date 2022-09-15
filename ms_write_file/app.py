
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from celery import Celery
import os
from dotenv import load_dotenv

app=FastAPI()

load_dotenv("../.env")
celery=Celery(__name__)
celery.conf.broker_url=os.getenv('CELERY_BROKER_URL')
celery.conf.result_backend=os.getenv('CELERY_BACKEND_URL')

@app.get('/')
def home():
    return {"Message":"Hola mundo"}
@app.get('/file')
def sendWriteFile():
    result = celery.send_task('writeTask', [2,'test'],
        queue="write_file"
    ) 
    print(result)
    return JSONResponse({"RESULT":"Tarea enviada"})
