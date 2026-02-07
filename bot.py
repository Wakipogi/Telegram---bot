from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("8442519587:AAH3iJXKHIb4pHGHpH7C0Gri4iJbnh_py6k")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! 👋 Bot is running on Fly.io")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
