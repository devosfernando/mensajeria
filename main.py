import sys, os, asyncio, logging, subprocess, nest_asyncio
from flask import Flask, request, jsonify
from telegram import Bot
from datetime import datetime, timedelta

# Verificar si Flask y python-telegram-bot están instalados e instalarlos si no lo están
val = 1
try:
    from flask import Flask, request, jsonify
    val = 2
    from telegram import Bot
    val = 3
    import nest_asyncio 
except ImportError:
    if val == 1:
        print("Instalando Flask...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Flask"])
        from flask import Flask, request, jsonify
    if val <= 2:
        print("Instalando dependencias de Telegram...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "python-telegram-bot"])
        from telegram import Bot
    if val <= 3:
        print("Instalando dependencias de Telegram...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "nest_asyncio"])
        from telegram import Bot


# Inicializar bot con tu token
bot = Bot(token=os.getenv('TELEGRAM_TOKEN'))
app = Flask(__name__)
# Habilitar nest_asyncio para evitar errores de "Event loop is closed"
nest_asyncio.apply()
# Suprimir los mensajes de advertencia configurando el nivel de logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


# Función asíncrona para enviar el mensaje
async def enviar_mensaje_telegram(message):
    try:
        # Enviar mensaje a Telegram de forma asíncrona
        await bot.send_message(chat_id=os.getenv('TELEGRAM_CHAT_ID'), text=message)
        print("Mensaje enviado a Telegram")
    except Exception as e:
        print(f"Error al enviar mensaje: {e}")


# Función sincrónica para manejar el envío asíncrono dentro de Flask
def send_informe(message):
    try:
        # Ejecutar la tarea asíncrona dentro de un entorno sincrónico
        asyncio.run(enviar_mensaje_telegram(message))
    except Exception as e:
        print(f"Error al enviar el mensaje: {e}")


# Ruta para recibir mensajes a través de POST
@app.route('/send_message', methods=['POST'])
def recibir_mensaje():
    try:
        # Obtener los datos en formato JSON
        data = request.get_json()
        # Verificar si el campo 'message' está presente en los datos
        message = data.get('message', 'No se envió ningún mensaje')

        # Ejecutar el envío de mensaje
        send_informe(message)

        return jsonify({"status": "success", "message": "Mensaje enviado a Telegram"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == '__main__':
    # Obtener la hora actual en UTC
    now_utc = datetime.utcnow()
    now_colombia = now_utc - timedelta(hours=5)
    fecha_hora = now_colombia.strftime("%Y-%m-%d %H:%M:%S")

    # Crear el mensaje con la fecha y hora
    message = f"📡 Fecha y hora: {fecha_hora}\n \n    🆙 Sistema de notificaciones entra en línea."
    
    # Enviar el mensaje de inicio del sistema
    send_informe(message)

    # Iniciar el servidor Flask
    app.run(host='0.0.0.0', port=6367)
