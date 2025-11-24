ARG BUILD_FROM
FROM $BUILD_FROM

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN apk add --no-cache bash \
    && pip3 install requests

WORKDIR /app

COPY hikvision_event_listener.py /app/hikvision_event_listener.py
COPY run.sh /run.sh
RUN chmod +x /run.sh

CMD [ "/run.sh" ]
