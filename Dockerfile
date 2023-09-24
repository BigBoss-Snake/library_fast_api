FROM python:3.11-alpine

WORKDIR /home/library

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev libxml2-dev libxslt-dev


RUN pip3 install --upgrade "pip>=22"
COPY ./requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

