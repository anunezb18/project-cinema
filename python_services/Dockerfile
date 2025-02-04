FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app/python_services

COPY ./backend_python /app/backend_python

EXPOSE 8000

CMD ["uvicorn", "backend_python.main:app", "--host", "0.0.0.0", "--port", "8000"]