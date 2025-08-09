import logging
import os
import requests
import urllib.parse
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# 🔐 Get Bot Token from environment variable
TOKEN = os.environ.get("BOT_TOKEN")

if not TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set!")

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
        encoded_url = urllib.parse.quote(long_url, safe='')

        # TinyURL
        tinyurl = None
        try:
            r1 = requests.get(f"https://tinyurl.com/api-create.php?url={encoded_url}", timeout=5)
            if r1.status_code == 200:
                tinyurl = r1.text
        except:
            pass

        # is.gd
        isgd = None
        try:
            unique_part = urllib.parse.quote('link' + str(hash(long_url)))
            r2 = requests.get(f"https://is.gd/create.php?format=simple&url={encoded_url}&shorturl={unique_part}", timeout=5)
            if r2.status_code == 200:
                isgd = r2.text
        except:
            pass

        if not tinyurl and not isgd:
            await update.message.reply_text("⚠️ Couldn't shorten link. Please try again.")
            return

        # Prepare message
        msg = "✨ **Your Shortened Links**\n"
        if tinyurl:
            msg += f"🔗 [TinyURL]({tinyurl})\n"
        if isgd:
            msg += f"⚡ [is.gd]({isgd})\n"

        await update.message.reply_text(msg, parse_mode="Markdown", disable_web_page_preview=True)

    except Exception as e:
        logging.error(f"Error shortening link: {e}")
        await update.message.reply_text("🚫 Error: Something went wrong. Try again later.")

# 🧠 Run the Bot (Polling)
if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shorten_link))
    logging.info("Bot is running...")
    app.run_polling()            tinyurl = None

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
