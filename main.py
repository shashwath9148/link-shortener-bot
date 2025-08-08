import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "
          7955744196:AAFqFip1tuV1IYeFSmZXt-jdkGgfpbvsYp8
        "

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 Welcome to Link Shortener Bot!\nJust send me any long URL and I’ll shorten it for you instantly.")

async def shorten_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    long_url = update.message.text.strip()
    if not long_url.startswith("http"):
        await update.message.reply_text("❗ Please send a valid URL starting with http or https.")
        return
    try:
        res = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}")
        if res.status_code == 200:
            await update.message.reply_text(f"🔗 Shortened URL: {res.text}")
        else:
            await update.message.reply_text("⚠️ Failed to shorten link. Please try again later.")
    except Exception as e:
        await update.message.reply_text("🚫 Error: Could not shorten the link.")

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_link))
    print("Bot is running...")
    app.run_polling()
