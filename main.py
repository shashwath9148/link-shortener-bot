import os
import logging
import aiohttp
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv

# 📂 Load environment variables
load_dotenv()

# 🔐 Bot Token from .env
TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN not found. Please set it in your .env file.")

# 📋 Logging Configuration
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🚀 /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔗 Hey! Send me a link to shorten.\n\n"
        "✅ Must start with http or https."
    )

# ✂️ Link Shortening Logic
async def shorten_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    long_url = update.message.text.strip()

    # ✅ Strong URL validation
    if not re.match(r"^https?://[^\s/$.?#].[^\s]*$", long_url, re.IGNORECASE):
        await update.message.reply_text("❗ Please send a valid URL starting with http or https.")
        return

    # ⏳ Send processing message
    processing_msg = await update.message.reply_text("⏳ Shortening your link...")

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://tinyurl.com/api-create.php?url={long_url}") as res:
                if res.status == 200:
                    short_url = await res.text()
                    await processing_msg.edit_text(
                        f"🔗 Shortened URL:\n{short_url}\n\n✨ Powered by @Shashu9148",
                        disable_web_page_preview=True
                    )
                else:
                    logger.error(f"TinyURL API error: {res.status}")
                    await processing_msg.edit_text("⚠️ Failed to shorten link. Please try again later.")

    except Exception as e:
        logger.error(f"Error while shortening URL: {e}")
        await processing_msg.edit_text("🚫 Error: Could not shorten the link.")

# 🧠 Bot App Setup
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_link))

    logger.info("✅ Bot is running...")
    app.run_polling()
