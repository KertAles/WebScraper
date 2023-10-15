# app/Dockerfile
FROM python:3.8

WORKDIR /app

COPY requirementsApp.txt .
RUN pip install --no-cache-dir -r requirementsApp.txt

# Copy the custom server script into the container
COPY . /app

# Expose the port your server listens on
EXPOSE 8080

# Run your custom server script
CMD ["python", "http_server.py"]