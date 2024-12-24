FROM python:3.11-slim

ENV PYTHONNUNBUFFERED=1
RUN mkdir /app
WORKDIR /app
COPY . /app/
RUN pip install -r requirements.txt
