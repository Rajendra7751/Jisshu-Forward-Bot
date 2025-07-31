# bot developer @mr_jisshu
import os
import threading
from flask import Flask
from bot import Bot

# Create Flask app directly here
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

# Run Flask server in background (for Render)
def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

threading.Thread(target=run_flask, daemon=True).start()

# Start the Telegram bot
app = Bot()
app.run()
