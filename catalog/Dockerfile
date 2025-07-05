FROM python:3.10

WORKDIR /app
ENV PYTHONPATH=/app

RUN pip install uvicorn

COPY ./requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir


COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]