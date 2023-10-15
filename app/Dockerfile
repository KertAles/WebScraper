# app/Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirementsApp.txt .
RUN pip install --no-cache-dir -r requirementsApp.txt

COPY . .

CMD [ "python", "http_server.py" ]

EXPOSE 8080