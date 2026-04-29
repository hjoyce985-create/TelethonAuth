import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start(update: telegram.Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello!')

def echo(update: telegram.Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main() -> None:
    updater = Updater("8252412070:AAGBh9V3LVAvWOvjXicO6NQgIVIDd5eLtdA", use_context=True)
    
    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler("start", start)) # pyright: ignore[reportOptionalMemberAccess]
    
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo)) # pyright: ignore[reportOptionalMemberAccess]

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()