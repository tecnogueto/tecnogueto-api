FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD HOME=/root python3 manage.py runserver 0.0.0.0:8000 --noreload