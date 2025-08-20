📜 Thirukkural WhatsApp Bot

This Python bot fetches a Thirukkural from the GetThirukkural API
 and automatically sends it to a WhatsApp group every morning via Whapi.cloud
.

🚀 Features

Fetches Thirukkural (any number, customizable).

Sends formatted message in Tamil with explanation.

Uses Whapi.cloud API for WhatsApp integration.

Logs all activities and errors to thirukkural_bot.log.

🛠️ Requirements

Python 3.8+

requests library

Install dependencies:

pip install requests

⚙️ Configuration

Edit the following variables in the script before running:

# API keys
KURAL_API_KEY = "YOUR_API_KEY"   # Get from getthirukkural.appspot.com
WHAPI_TOKEN   = "YOUR_API_TOKEN" # Get from whapi.cloud

# URLs
KURAL_API_URL = "https://getthirukkural.appspot.com/api/3.0/kural/{num}?appid={api_key}&format=json"
WHAPI_URL     = "https://gate.whapi.cloud/messages/text"

# WhatsApp Group
WHATSAPP_GROUP_ID = "GROUP_ID"   # Format: "1203xxxxxxxxxx@g.us"

# Kural settings
KURAL_NUMBER = 1                 # Change to random or sequential later
KURAL_URAI_VERSION = "urai2"     # urai1 / urai2 / urai3

▶️ Usage

Run the bot manually:

python thirukkural_bot.py


You should see output like:

{'sent': True, 'id': 'xxxxxxx'}


And your group will receive:

காலை வணக்கம் 🌞

இன்றைய குறள் #1

அகர முதல எழுத்தெல்லாம் ஆதி
பகவன் முதற்றே உலகு.

பொருள்:
எழுத்துக்கள் எல்லாம் அகரத்தை அடிப்படையாக கொண்டிருக்கின்றன.
அதுபோல உலகம் கடவுளை அடிப்படையாக கொண்டிருக்கிறது.

நன்றி

📒 Logs

All logs are stored in thirukkural_bot.log:

✅ Successful fetch & send

❌ Errors (e.g., API issues, invalid JSON, network errors)

⏰ Automation

You can schedule this bot to run every morning (6 AM) using:

Linux (Cron):
0 6 * * * /usr/bin/python3 /path/to/thirukkural_bot.py

Windows (Task Scheduler):

Create a daily task at 6 AM and run:

python C:\path\to\thirukkural_bot.py

📌 Notes

Ensure your Whapi session is active (linked to WhatsApp).

Group ID can be fetched from Whapi API or logs.

API may return non-JSON (like parked domain pages) if quota expires or wrong endpoint is used → handled in logs.

👨‍💻 Author

Made with ❤️ for Tamil & Technology.