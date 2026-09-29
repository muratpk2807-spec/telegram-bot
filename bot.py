import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = "8351886950:AAHE3qCX1d-2t-UtJ6UVcyV0bkNuRbU7O9c"
PDF_FILE_PATH = 'Nutrilogy.pdf'   # файл рядом со скриптом

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().upper()

    if user_text == "ПОДАРОК":
        try:
            with open(PDF_FILE_PATH, 'rb') as doc:
                await update.message.reply_document(
                    document=doc,
                    filename="Ваш_Подарок.pdf",
                    caption="Забирайте ваш подарок!"
                )
        except FileNotFoundError:
            import os
            await update.message.reply_text(
                f"Ищу файл тут: {os.path.abspath(PDF_FILE_PATH)}\n"
                f"Текущая папка: {os.getcwd()}"
            )
    else:
        await update.message.reply_text("Напишите слово «ПОДАРОК», чтобы получить файл.")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен...")
    app.run_polling()