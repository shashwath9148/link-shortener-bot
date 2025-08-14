import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 Your Bot Token
TOKEN = "7955744196:AAHGVBmHduUJx5mtvziagvK2uJF2Ce6ty9E"

# 📋 Logging Config
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🚀 /start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔗 Hey! Send me a link to shorten:")

# ✂️ Link Shortening Logic
async def shorten_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    long_url = update.message.text.strip()

    if not long_url.lower().startswith("http"):
        await update.message.reply_text("❗ Please send a valid URL starting with http or https.")
        return

    try:
        res = requests.get(f"https://tinyurl.com/api-create.php?url={long_url}", timeout=10)
        if res.status_code == 200:
            short_url = res.text.strip()
            await update.message.reply_text(
                f"🔗 Shortened URL:\n{short_url}\n\n✨ Powered by @Shashu9148",
                disable_web_page_preview=True
            )
        else:
            logger.error(f"TinyURL API returned status {res.status_code}")
            await update.message.reply_text("⚠️ Failed to shorten link. Please try again later.")
    except Exception as e:
        logger.error(f"Error while shortening link: {e}")
        await update.message.reply_text("🚫 Error: Could not shorten the link.")

# 🧠 Bot App Setup
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_link))

    logger.info("✅ Bot is running...")
    app.run_polling()        await update.message.reply_text("❗ Please send a valid URL starting with http or https.")
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
