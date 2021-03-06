FROM python:3.8.0-slim

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apt-get update && apt-get install -y \
  gcc \
 && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY ./requirements /usr/src/app/requirements
COPY ./requirements.txt /usr/src/app/
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

