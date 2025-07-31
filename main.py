# bot developer @mr_jisshu
import threading
from flask import Flask
from bot import Bot  # your custom Pyrogram Bot class

# Create Flask app inside main
flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot is running!"

# Run Flask in background (always bind 8080)
def run_flask():
    flask_app.run(host='0.0.0.0', port=8080)

threading.Thread(target=run_flask, daemon=True).start()

# Start the Telegram bot
if __name__ == "__main__":
    Bot().run()
