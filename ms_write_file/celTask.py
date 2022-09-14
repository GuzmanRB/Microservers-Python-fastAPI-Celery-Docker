from celery import Celery
import os
from dotenv import load_dotenv
import time


load_dotenv("../.env")
app=Celery(__name__)
app.conf.broker_url=os.getenv('CELERY_BROKER_URL')
app.conf.result_backend=os.getenv('CELERY_BACKEND_URL')

@app.task(name="writeTask")
def writeFile(delay):
    time.sleep(delay)
    f=open(".tmp/test.txt","a+")
    for i in range(10):
        f.write("Esto es una prueba de escritura con celery, linea:" +str(i)+"\n")
    f.close()
    return 'Fichero escrito'
    
