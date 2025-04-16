import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import os
from dotenv import load_dotenv

# Načítanie tokenu z .env súboru
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

# Nastavenie logovania
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Funkcia pre príkaz /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Ahoj, som tvoj nový Telegram bot!')

def main():
    """Spustenie bota."""
    # Vytvorenie Updater objektu a nastavenie tokenu
    updater = Updater(TELEGRAM_TOKEN)

    # Získanie Dispatcher pre prácu s príkazmi
    dispatcher = updater.dispatcher

    # Pridanie CommandHandler pre príkaz /start
    dispatcher.add_handler(CommandHandler("start", start))

    # Spustenie bota
    updater.start_polling()

    # Udržiavanie bota bežiaceho
    updater.idle()

if __name__ == '__main__':
    main()
