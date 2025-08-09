import logging
import requests
import urllib.parse
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 Your Bot Token
TOKEN = "7955744196:AAG7pWKC_fcW3UQffYSyBBdyllueJfS7XL8"

# 📋 Logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# 🚀 /start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_msg = (
        "🔗 **TinyLink Gen**\n"
        "Your personal fast & clean URL shortener.\n\n"
        "📌 Send me any link and I'll shorten it using **3 services** instantly!"
    )
    await update.message.reply_text(welcome_msg, parse_mode="Markdown")

# ✂️ Shorten Link Function with Inline Buttons
async def shorten_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    long_url = update.message.text.strip()

    if not long_url.startswith("http"):
        await update.message.reply_text("❗ Please send a valid URL starting with http or https.")
        return

    try:
        encoded_url = urllib.parse.quote(long_url, safe='')

        # Shorteners
        try:
            tinyurl = requests.get(f"https://tinyurl.com/api-create.php?url={encoded_url}", timeout=5).text
        except:
            tinyurl = None

        try:
            isgd = requests.get(f"https://is.gd/create.php?format=simple&url={encoded_url}", timeout=5).text
        except:
            isgd = None

        try:
            vgd = requests.get(f"https://v.gd/create.php?format=simple&url={encoded_url}", timeout=5).text
        except:
            vgd = None

        # Create Inline Keyboard
        buttons = []
        if tinyurl:
            buttons.append([InlineKeyboardButton("🔗 TinyURL", url=tinyurl)])
        if isgd:
            buttons.append([InlineKeyboardButton("⚡ is.gd", url=isgd)])
        if vgd:
            buttons.append([InlineKeyboardButton("🚀 v.gd", url=vgd)])

        reply_markup = InlineKeyboardMarkup(buttons)

        await update.message.reply_text(
            "✨ **Your Shortened Links**\nChoose one below 👇\n\n⚡ _Powered by @Shashu9148_",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    except Exception as e:
        await update.message.reply_text("🚫 Error: Could not shorten the link. Please try again later.")
        logging.error(e)

# 🧠 Run Bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_link))
    print("Bot is running...")
    app.run_polling()            f"1️⃣ [TinyURL]({tiny_url})\n"
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
