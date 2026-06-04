import os
import logging
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, MessageHandler, filters

# Configuración
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Variables de entorno (seguras)
TOKEN = os.getenv('BOT_TOKEN')
SOURCE_CHAT_ID = int(os.getenv('SOURCE_CHAT_ID'))
DEST_CHAT_ID = int(os.getenv('DEST_CHAT_ID'))

# Flask para mantener vivo el servicio
app = Flask(__name__)

@app.route('/')
@app.route('/health')
def health():
    return "Bot is running", 200

# Lógica del bot: reenviar mensajes
async def forward(update: Update, context):
    chat_id = update.effective_chat.id
    if chat_id == SOURCE_CHAT_ID:
        try:
            await context.bot.forward_message(
                chat_id=DEST_CHAT_ID,
                from_chat_id=SOURCE_CHAT_ID,
                message_id=update.effective_message.message_id
            )
            logging.info(f"Mensaje {update.effective_message.message_id} reenviado.")
        except Exception as e:
            logging.error(f"Error: {e}")

def run_bot():
    # Crear la aplicación del bot
    application = Application.builder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, forward))
    # Iniciar el bot (polling)
    application.run_polling()

def run_flask():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    # Hilo para Flask
    flask_thread = Thread(target=run_flask)
    flask_thread.start()
    # Ejecutar el bot en el hilo principal
    run_bot()
