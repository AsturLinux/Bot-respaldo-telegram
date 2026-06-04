# 🤖 Bot de Telegram - Copia de mensajes entre canales

Este bot copia automáticamente los mensajes (texto, fotos, vídeos, documentos, etc.) enviados en un canal de Telegram **a otro canal**, **sin mostrar el remitente original**. El mensaje aparece como enviado directamente por el bot.

Es ideal para:
- Crear una copia de seguridad oculta de un canal privado.
- Migrar contenido entre canales manteniendo el anonimato.
- Automatizar la sincronización de publicaciones sin marcas de reenvío.

---

## 🚀 Características

- ✅ Copia mensajes en **tiempo real** (apenas se publican en el canal origen).
- ✅ Elimina la etiqueta "Reenviado desde..." – el mensaje aparece como enviado por el bot.
- ✅ Soporta todo tipo de contenido: texto, fotos, vídeos, documentos, stickers, etc.
- ✅ Funciona con canales **privados** (el bot debe ser administrador en ambos canales).
- ✅ Incluye un servidor web (Flask) para mantener el servicio activo en Render.
- ✅ Se puede mantener 24/7 de forma gratuita con cron-job.org o UptimeRobot.

---

## 📋 Requisitos previos

- Cuenta en [GitHub](https://github.com)
- Cuenta en [Render](https://render.com) (gratuita)
- Cuenta en [cron-job.org](https://cron-job.org) (gratuita, opcional pero recomendada)
- Un bot de Telegram creado con [@BotFather](https://t.me/botfather)
- Ser **administrador** de los dos canales (origen y destino)

---

## 🛠️ Configuración paso a paso

### 1. Crear el bot y obtener el token

1. Abre Telegram y busca [@BotFather](https://t.me/botfather).
2. Envía `/newbot` y sigue las instrucciones (nombre, nombre de usuario).
3. Al final, BotFather te dará un token que se parece a `1234567890:ABCdefGHIjklmNOPqrstUVwxyz`.  
   **Guarda este token** (lo necesitarás más adelante).

### 2. Obtener los IDs de tus canales

Puedes usar [@userinfobot](https://t.me/userinfobot) o cualquier bot que muestre IDs:

1. Añade el bot a tus canales como **administrador** (necesitarás al menos permisos para "Ver mensajes" y "Enviar mensajes").
2. Envía un mensaje a cada canal.
3. Escribe `/id` en el chat con @userinfobot. El bot te responderá con el ID numérico de cada canal (normalmente empieza con `-100`).  
   **Guarda estos IDs** (origen y destino).

### 3. Preparar el repositorio en GitHub

1. Crea un repositorio nuevo en GitHub (público o privado).
2. Sube los siguientes archivos en la raíz:

   - `main.py` (con el código del bot)
   - `requirements.txt` (dependencias)
   - `README.md` (este archivo)

   **Contenido de `requirements.txt`:**
