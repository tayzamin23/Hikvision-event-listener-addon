import requests, time, urllib3
from requests.auth import HTTPDigestAuth

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

CAMERA_IP = "192.168.110.74"
USERNAME = "admin"
PASSWORD = "Diginet@2025"
WEBHOOK_URL = "http://192.168.110.58:8123/api/webhook/hikvision_event"

url = f"https://{CAMERA_IP}/ISAPI/Event/notification/alertStream"

session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "*/*",
    "Connection": "keep-alive",
    "Cache-Control": "no-cache",
    "Pragma": "no-cache"
}

def send_webhook(event_type):
    payload = {"eventType": event_type}

    try:
        # IMPORTANT: Do NOT manually set "Content-Type"
        resp = requests.post(WEBHOOK_URL, json=payload, timeout=5)
        print(f"[WEBHOOK] Sent → {event_type}")
        print("STATUS:", resp.status_code)
        print("RESPONSE:", resp.text)
    except Exception as e:
        print("Webhook failed:", e)


while True:
    try:
        print("Connecting to Hikvision event stream...")

        r = session.get(
            url,
            auth=HTTPDigestAuth(USERNAME, PASSWORD),
            stream=True,
            timeout=20,
            verify=False,
            headers=headers
        )

        print("Connected. Waiting for events...")

        for raw_line in r.iter_lines():
            if not raw_line:
                continue

            try:
                line = raw_line.decode(errors="ignore")
            except:
                line = str(raw_line)

            # Debug print Hikvision raw output
            # print("RAW:", line)

            if "<eventType>" in line:
                print("EVENT:", line)

                event_value = line.lower()

                # FACE DETECTION DETECTED
                if "face" in event_value:
                    print("FACE DETECTED → Sending to Home Assistant")
                    send_webhook("faceDetection")

    except Exception as e:
        print("Connection lost:", e)
        print("Reconnecting in 5 seconds...")
        time.sleep(5)
