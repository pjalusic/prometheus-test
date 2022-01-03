# syntax = docker/dockerfile:1.3

FROM python:3.7.5-slim-buster

COPY requirements.txt ./

RUN pip3 install -r requirements.txt

COPY main.py /

ENTRYPOINT ["python"]

CMD ["main.py"]