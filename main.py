from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telethon.tl.types import InputMessagesFilterEmpty
from telethon import TelegramClient
from constants import *

CHANNEL_USERNAME: Final = '@test_cf_dating_channel'
API_ID: Final = '7063969059' # ??
API_HASH: Final = 'AAHhFvNiKAGLztJFvI4WaqhIbHO6NvaQKvg' # ??

client = TelegramClient(CHANNEL_USERNAME, API_ID, API_HASH)

# Default command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Hello')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('Type something')


# Custom command handlers
async def shuffle_users_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	# new_seq = [];	
	new_seq ='DUMMY SEQ STR'

	print('Shuffling entries...')

	groupChat: chat = update.message.chat
	messages_5 = await client.get_messages(chat, ids=2)
	for message in client.iter_messages(chat):
		print(message.id, message.text)

	await update.message.reply_text('Shuffling is done.\n\n')


async def xyz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
	await update.message.reply_text('This is xyz command.')


# Responses


def handle_response(text: str) -> str:
	print('Handling response {text}...')



async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
	message_type = update.message.chat.type
	text: str = update.message.text

	print(f'User({update.message.chat.id}) in {message_type}): "{text}"')


	if message_type == 'group':
		if BOT_USERNAME in text:
			print('I am in a group')
			# do nothing. not designed to use in a gc
		# print('Unexpected usage. I am not designed to be used in a group chat.')
		# return

	else: # private chat
		response: str = handle_response(text)

	print('Bot: ', response)
	update.message.reply_text(response)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
	print(f'Update {update} caused error {context.error}')



if __name__ == '__main__':
	print('Starting...')
	app = Application.builder().token(TOKEN).build()

	# Commands
	app.add_handler(CommandHandler('start', start_command))
	app.add_handler(CommandHandler('help', help_command))
	app.add_handler(CommandHandler('shuffle_users', shuffle_users_command))

	# Messages
	app.add_handler(MessageHandler(filters.TEXT, handle_message))


	# Errors
	app.add_error_handler(error)


	print('Polling...')
	app.run_polling(poll_interval=3)





























