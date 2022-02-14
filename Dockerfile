# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /rub2b
COPY requirements.txt /rub2b/
RUN pip install -r requirements.txt
COPY . /rub2b/