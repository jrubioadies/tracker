"""
Bot de Telegram — envío de enlaces de rastreo de IP
Requiere: pip install python-telegram-bot

Uso:
  python bot.py

Comandos disponibles:
  /start    — muestra ayuda
  /link     — genera un enlace de rastreo y lo envía
  /link ID  — genera enlace con un ID personalizado
"""

import logging
import uuid
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# ── CONFIGURA ESTOS VALORES ──────────────────────────────────────────────────
BOT_TOKEN  = "TU_BOT_TOKEN_AQUI"       # Obtén uno con @BotFather en Telegram
BASE_URL   = "https://tu-dominio.com"  # URL donde está alojado el index.html
# ─────────────────────────────────────────────────────────────────────────────

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 *Bot de rastreo de IP*\n\n"
        "Comandos disponibles:\n"
        "• /link — genera un enlace de rastreo\n"
        "• /link MiID — enlace con ID personalizado\n\n"
        "Cuando alguien pulse el enlace, recibirás su IP aquí.",
        parse_mode="Markdown"
    )


async def link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Usa el argumento como ID, o genera uno aleatorio
    if context.args:
        track_id = "_".join(context.args)
    else:
        track_id = str(uuid.uuid4())[:8]

    url = f"{BASE_URL}/index.html?id={track_id}"

    await update.message.reply_text(
        f"🔗 *Enlace de rastreo generado*\n\n"
        f"ID: `{track_id}`\n"
        f"URL: {url}\n\n"
        f"Envía este enlace. Cuando lo abran, recibirás su IP en este chat.",
        parse_mode="Markdown"
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("link", link))

    print("Bot en marcha. Pulsa Ctrl+C para detener.")
    app.run_polling()


if __name__ == "__main__":
    main()
