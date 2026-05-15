from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import os

# 🔑 Replit Secrets ichida shu nom bilan qo'y:
# TELEGRAM_BOT_TOKEN

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    print("❌ TOKEN topilmadi! Secrets tekshir!")
    exit()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("START ishladi")
    await update.message.reply_text("Bot ishlayapti ✅")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("MESSAGE:", update.message.text)
    await update.message.reply_text(f"Siz yozdingiz: {update.message.text}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("🤖 Bot ishga tushdi...")
    app.run_polling()

if __name__ == "__main__":
    main()
