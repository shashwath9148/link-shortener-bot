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
    await update.message.reply_text("🔗 Hey! Send me a link to shorten using 3 services:")

# ✂️ Shorten Link Function
async def shorten_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    long_url = update.message.text.strip()
    if not long_url.startswith("http"):
        await update.message.reply_text("❗ Please send a valid URL starting with http or https.")
        return

    try:
        # Shortener 1: TinyURL
        tiny_url = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}").text

        # Shortener 2: is.gd
        isgd_url = requests.get(f"https://is.gd/create.php?format=simple&url={long_url}").text

        # Shortener 3: shrtco.de
        shrtco_data = requests.get(f"https://api.shrtco.de/v2/shorten?url={long_url}").json()
        shrtco_url = shrtco_data["result"]["full_short_link"]

        # Send all three clickable links
        await update.message.reply_text(
            f"🔗 Shortened Links:\n"
            f"1️⃣ [TinyURL]({tiny_url})\n"
            f"2️⃣ [is.gd]({isgd_url})\n"
            f"3️⃣ [shrtco.de]({shrtco_url})\n\n"
            f"✨ Powered by @Shashu9148",
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

    except Exception:
        await update.message.reply_text("🚫 Error: Could not shorten the link. Please try again later.")

# 🧠 Run the Bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_link))
    print("Bot is running...")
    app.run_polling()
