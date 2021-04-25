FROM python:3.7

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["sh", "startup.sh"]

# docker build --no-cache -t myimage2 .
