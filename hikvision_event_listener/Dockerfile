ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies
RUN apk add --no-cache bash \
    && pip3 install requests urllib3

# Copy files
WORKDIR /app
COPY run.sh /app/run.sh
COPY hikvision_event_listener.py /app/hikvision_event_listener.py

# Permissions
RUN chmod +x /app/run.sh

# Start script
CMD [ "/app/run.sh" ]
