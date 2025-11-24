#!/usr/bin/with-contenv bash
echo "Starting Hikvision Event Listener..."
exec python3 -u /app/hikvision_event_listener.py
