import re
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from uuid import uuid4

import secret


def replace_to_e(text):
    return re.sub("[АУОЫИЭЯЮЕ]", "Ё", re.sub("[ауоыиэяюе]", "ё", text))


def replace_to_bi(text):
    return re.sub("[АУОЫИЭЯЮЕЁ]", "Ы", re.sub("[ауоыиэяюеё]", "ы", text))


def replace_to_custom(text):
    to, source_text = text.split(' ', 1)
    return re.sub("[АУОЫИЭЯЮЕЁауоыиэяюеё]", to, source_text)


def without_glass(text):
    return re.sub("[АУОЫИЭЯЮЕЁ]", "", re.sub("[ауоыиэяюеё]", "", text))


def inlinequery(update, context):
    """Handle the inline query."""
    query = update.inline_query.query
    results = [
        InlineQueryResultArticle(
            id=uuid4(),
            title=replace_to_e(query),
            input_message_content=InputTextMessageContent(replace_to_e(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title=replace_to_bi(query),
            input_message_content=InputTextMessageContent(replace_to_bi(query))),
        InlineQueryResultArticle(
            id=uuid4(),
            title=without_glass(query),
            input_message_content=InputTextMessageContent(without_glass(query)))
    ]

    try:
        replace_text = replace_to_custom(query)
        results.append(InlineQueryResultArticle(
            id=uuid4(),
            title=replace_text,
            input_message_content=InputTextMessageContent(replace_text)))
    except ValueError:
        pass

    update.inline_query.answer(results)


def main():
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(secret.token, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(InlineQueryHandler(inlinequery))

    # Start the Bot
    updater.start_polling()

    # Block until the user presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
