FROM python:3.9

ENV CELERY_BROKER_URL=redis://redis:6379/
ENV CELERY_BACKEND_URL=redis://redis:6379/

RUN apt-get -y update
RUN apt-get -y upgrade

WORKDIR /app

# 
COPY ./requirements.txt /app/requirements.txt


# 
RUN pip install --no-cache-dir -r /app/requirements.txt

# 
COPY . /app

# 
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]



