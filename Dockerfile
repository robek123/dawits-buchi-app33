FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

LABEL maintainer="Dawit"

WORKDIR /app

COPY ./app ./app

RUN pip install -r ./app/requirements.txt