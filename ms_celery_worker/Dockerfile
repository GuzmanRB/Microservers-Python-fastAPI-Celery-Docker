FROM python:3.9

ENV CELERY_BROKER_URL=redis://redis:6379/
ENV CELERY_BACKEND_URL=redis://redis:6379/

RUN apt-get -y update
RUN apt-get -y upgrade

# copy source code
COPY . /app
WORKDIR /app

# install requirements
RUN pip install --no-cache-dir -r requirements.txt

CMD ["celery", "-A", "celTask", "worker", "--loglevel=debug","--pool=solo","-Qwrite_file"]
