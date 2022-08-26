from telegram.ext import ApplicationBuilder, CommandHandler
from dotenv import load_dotenv
import os
from funcs_db import salvar_id

load_dotenv()

def get_contacts():
    # essa parte é a que vai levar mais planejamento da minha parte
    async def start(update, context):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=f'{update.effective_chat.id}')
        id_user = update.effective_chat.id
        salvar_id(id_user)
    
    aplicacao = ApplicationBuilder().token(os.environ['token']).build()

    start_handler = CommandHandler('start', start)

    aplicacao.add_handler(start_handler)

    aplicacao.run_polling()

get_contacts()