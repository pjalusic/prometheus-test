# syntax = docker/dockerfile:1.3

FROM python:3.7.5-slim-buster

RUN apt-get update \
    && apt-get install -y glances curl

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY . /app

WORKDIR /app

ENTRYPOINT ["python", "main.py"]
