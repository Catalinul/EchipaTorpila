# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENV FLASK_APP=fruits_app
ENV FLASK_ENV=development

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=127.0.0.1"]
