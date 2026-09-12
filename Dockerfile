FROM python:3.12-slim

WORKDIR /app

COPY calculadora.py .

CMD ["python", "calculadora.py"]