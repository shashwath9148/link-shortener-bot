import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 Your Bot Token
TOKEN = "7955744196:AAFqFip1tuV1IYeFSmZXt-jdkGgfpbvsYp8"

# 📋 Logging Setup
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# 🚀 /start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 Hey! Send me a link to shorten:")

# ✂️ Shorten Link Function
async def shorten_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    long_url = update.message.text.strip()
    if not long_url.startswith("http"):
        await update.message.reply_text("❗ Please send a valid URL starting with http or https.")
        return
    try:
        response = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}")
        if response.status_code == 200:
            short_url = response.text
            await update.message.reply_text(
                f"🔗 [Click here to open the link]({short_url})\n\n✨ Powered by @Shashu9148",
                parse_mode="Markdown",
                disable_web_page_preview=True
            )
        else:
            await update.message.reply_text("⚠️ Couldn't shorten link. Please try again.")
    except Exception:
        await update.message.reply_text("🚫 Error: Something went wrong. Try again later.")

# 🧠 Run the Bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_link))
    print("Bot is running...")
    app.run_polling()
