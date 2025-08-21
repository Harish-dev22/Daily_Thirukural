import requests
import logging
import datetime

# ================= CONFIG =================
KURAL_API_KEY = "YOUR_API_KEY" #getthirukkural website
KURAL_API_URL = "https://getthirukkural.appspot.com/api/3.0/kural/{num}?appid={api_key}&format=json"

WHAPI_URL = "https://gate.whapi.cloud/messages/text"
WHAPI_TOKEN = "YOUR_API_TOKEN"   # Replace with your WHAPI token
WHATSAPP_GROUP_ID = "GROUP_ID"

KURAL_NUMBER = 1                   # You can randomize later
KURAL_URAI_VERSION = "urai2"       # Change to urai1 / urai2 / urai3
# ==========================================

# Setup logging
logging.basicConfig(
    filename="thirukkural_bot.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def fetch_kural(num: int):
    """Fetch a Thirukkural from the API"""
    try:
        url = KURAL_API_URL.format(num=num, api_key=KURAL_API_KEY)
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        logging.info(f"Fetched Kural #{num} successfully")
        return data
    except Exception as e:
        logging.error(f"Error fetching Kural #{num}: {e}")
        return None

def format_message(data: dict) -> str:
    """Format the WhatsApp message in Tamil"""
    try:
        kural_number = data.get("number", "")
        line1 = data.get("line1", "")
        line2 = data.get("line2", "")
        meaning = data.get(KURAL_URAI_VERSION, "")
        meaning_author = data.get(f"{KURAL_URAI_VERSION}Author", "ஆசிரியர் தெரியவில்லை")

        message = (
            "காலை வணக்கம் 🌞\n\n"
            f"இன்றைய குறள் #{kural_number}\n\n"
            f"{line1}\n{line2}\n\n"
            f"பொருள்:\n{meaning}\n\n"
            f"நன்றி"
        )

        logging.info(f"Formatted message for Kural #{kural_number}")
        return message
    except Exception as e:
        logging.error(f"Error formatting message: {e}")
        return "❌ குறள் தகவலை பெற முடியவில்லை."

def send_whatsapp_message(message: str):
    """Send message to WhatsApp via Whapi"""
    try:
        payload = {
            "to": WHATSAPP_GROUP_ID,
            "body": message
        }
        headers = {"Authorization": f"Bearer {WHAPI_TOKEN}"}
        response = requests.post(WHAPI_URL, headers=headers, json=payload)
        response.raise_for_status()
        try:
            result = response.json()
        except ValueError:
            logging.error(f"Non-JSON response: {response.text}")
            return {"error": "Invalid JSON", "raw": response.text}
        logging.info("Message sent successfully")
        return result
    except Exception as e:
        logging.error(f"Error sending WhatsApp message: {e}")
        return None

if __name__ == "__main__":
    logging.info("=== Thirukkural Bot Started ===")
    # Sequential kural logic
    START_DATE = datetime.date(2025, 8, 20)
    today = datetime.date.today()
    days_passed = (today - START_DATE).days
    kural_number = (days_passed % 1330) + 1
    kural = fetch_kural(kural_number)
    if kural:
        msg = format_message(kural)
        result = send_whatsapp_message(msg)
        print(result)
    else:
        print("Failed to fetch Kural.")
