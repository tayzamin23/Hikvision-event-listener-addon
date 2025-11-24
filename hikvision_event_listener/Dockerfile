FROM python:3.11-alpine

RUN apk add --no-cache bash \
    && pip3 install requests

WORKDIR /app

# Copy run.sh correctly
COPY run.sh /app/run.sh

# Copy python file correctly (exact same name)
COPY hikvision_event_listener.py /app/hikvision_event_listener.py

# Make run.sh executable
RUN chmod +x /app/run.sh

