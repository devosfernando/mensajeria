# Sistema de Notificaciones con Flask y Telegram

Este proyecto implementa un **sistema de notificaciones** utilizando **Flask** como servidor web y **Telegram** como plataforma de mensajería. El sistema recibe mensajes a través de solicitudes POST y los envía a un canal o chat de Telegram utilizando el bot de Telegram.

## Características

- **Flask**: Se utiliza Flask como servidor web para recibir solicitudes HTTP.
- **Telegram Bot**: Los mensajes se envían a través de un bot de Telegram.
- **Soporte Asíncrono**: Se utiliza `asyncio` para enviar mensajes de forma asíncrona a Telegram.
- **Instalación Automática de Dependencias**: Si Flask, `python-telegram-bot` o `nest_asyncio` no están instalados, el código los instalará automáticamente.
- **Fecha y Hora**: Al iniciar, el sistema envía un mensaje con la fecha y hora actual (ajustada a la zona horaria de Colombia) notificando que el sistema ha entrado en línea.

## Requisitos

- **Python 3.x**
- **pip** para manejar las dependencias.
- **Variables de Entorno**:
  - `TELEGRAM_TOKEN`: El token del bot de Telegram.
  - `TELEGRAM_CHAT_ID`: El ID del chat o canal de Telegram donde se enviarán los mensajes.

## Instalación

1. **Clona este repositorio** en tu máquina local:
   ```bash
   git clone <url-del-repositorio>
   cd <nombre-del-repositorio>
    ```