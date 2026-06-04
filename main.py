import os
import logging
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

# ================= CONFIGURACIÓN =================
BOT_TOKEN = os.getenv('BOT_TOKEN')
SOURCE_CHAT_ID = int(os.getenv('SOURCE_CHAT_ID'))
DEST_CHAT_ID = int(os.getenv('DEST_CHAT_ID'))

logging.getLogger('telegram').setLevel(logging.WARNING)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# =================================================

app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health():
    return "Bot is running", 200

async def forward(update: Update, context):
    """Copia el mensaje del canal origen al destino SIN mostrar el remitente original"""
    chat_id = update.effective_chat.id
    if chat_id == SOURCE_CHAT_ID:
        try:
            # copy_message copia el contenido pero el autor será el bot
            await context.bot.copy_message(
                chat_id=DEST_CHAT_ID,
                from_chat_id=SOURCE_CHAT_ID,
                message_id=update.effective_message.message_id
            )
            logging.info(f"Mensaje {update.effective_message.message_id} copiado sin remitente.")
        except Exception as e:
            logging.error(f"Error al copiar mensaje {update.effective_message.message_id}: {e}")

def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, forward))
    logging.info("✅ Bot iniciado. Copiando mensajes sin remitente...")
    application.run_polling()

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    run_bot()
