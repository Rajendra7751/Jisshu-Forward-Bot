# bot developer @mr_jisshu
import os
import threading
from web import app as flask_app
from bot import Bot

# Run Flask server in background (for Render)
def run_flask():
    flask_app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

threading.Thread(target=run_flask, daemon=True).start()

# Start the Telegram bot
app = Bot()
app.run()
