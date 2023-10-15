# app/Dockerfile
FROM python:3.8

WORKDIR /scrappy

COPY requirementsScrapy.txt .
RUN pip install --no-cache-dir -r requirementsScrapy.txt

# Install Firefox and GeckoDriver
RUN apt-get update && apt-get install -y \
    firefox-esr \
    && apt-get clean

# Download and install the GeckoDriver
RUN wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
RUN tar -xvzf geckodriver-v0.30.0-linux64.tar.gz
RUN chmod +x geckodriver
RUN mv geckodriver /usr/local/bin
RUN rm -f geckodriver-v0.30.0-linux64.tar.gz

# Copy the rest of the application code into the container
COPY . /scrappy

CMD [ "python", "create_db.py" ]

CMD [ "scrapy", "crawl", "properties" ]