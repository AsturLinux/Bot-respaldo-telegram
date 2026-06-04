# Bot de Telegram: copia mensajes entre canales sin remitente

Copia automáticamente mensajes de un canal a otro, **sin mostrar el remitente original** (el mensaje aparece como enviado por el bot).

## 🚀 Despliegue rápido en Render (gratis)

1. **Crea el bot** con [@BotFather](https://t.me/botfather) → guarda el `BOT_TOKEN`.
2. **Obtén los IDs** de tus canales con [@userinfobot](https://t.me/userinfobot) → guárdalos como `SOURCE_CHAT_ID` y `DEST_CHAT_ID`.
3. **Sube a GitHub** los archivos `main.py` y `requirements.txt` (el código está abajo).
4. **En Render**: Nuevo Web Service → conecta GitHub → añade variables:
   - `BOT_TOKEN`
   - `SOURCE_CHAT_ID` (ej: `-1001234567890`)
   - `DEST_CHAT_ID`
5. **Mantén vivo** con [cron-job.org](https://cron-job.org): ping cada 5 min a `https://tu-bot.onrender.com/health`.

El bot debe ser **administrador** en ambos canales.
