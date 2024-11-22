FROM python:3.10-slim

WORKDIR /app

COPY kafka_example.py /app/kafka_example.py
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "kafka_example.py"]
