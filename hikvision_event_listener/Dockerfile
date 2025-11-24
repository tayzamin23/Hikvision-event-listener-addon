ARG BUILD_FROM
FROM $BUILD_FROM

# Install dependencies
RUN apk add --no-cache bash dos2unix \
    && pip3 install requests urllib3

# App folder
WORKDIR /app

# Copy files
COPY run.sh /app/run.sh
COPY hikvision_event_listener.py /app/hikvision_event_listener.py

# Fix permissions and line endings
RUN chmod +x /app/run.sh \
    && dos2unix /app/run.sh

# Start script
CMD [ "/app/run.sh" ]
