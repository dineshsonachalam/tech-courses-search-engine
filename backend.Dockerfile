FROM python:3.10-slim-buster

WORKDIR /app

COPY backend .

RUN pip install -r requirements.txt

EXPOSE 8000

RUN chmod +x /app/main.py

CMD ["python3", "main.py"]
