import logging
import sqlite3
from datetime import datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, filters

# Habilitar logs de erro
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.ERROR)

# Definir o token de acesso do bot
TOKEN = "seu_token_aqui"

def plantonista_do_dia(update, context):
    # Obter a data atual
    hoje = datetime.today().strftime('%Y-%m-%d')

    # Conectar ao banco de dados
    conn = sqlite3.connect('plantao.db')

    # Consultar o plantonista do dia
    cursor = conn.execute("SELECT plantonista FROM plantao WHERE data=?", (hoje,))
    plantonistas = cursor.fetchall()

    if len(plantonistas) > 0:
        # Enviar mensagem com o nome do plantonista
        plantonista = plantonistas[0][0]
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=f"O plantonista de hoje é {plantonista}.")
    else:   
        # Enviar mensagem informando que não há plantonista cadastrado para hoje
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text="Não há plantonista cadastrado para hoje.")

    # Fechar a conexão com o banco de dados
    conn.close()



# Definir o comando de ajuda
def ajuda(update, context):
    # Mensagem de ajuda
    ajuda_texto = "Comandos disponíveis:\n/plantonista - Mostrar o plantonista do dia\n/ajuda - Mostrar esta mensagem de ajuda\n"

    # Enviar a mensagem de ajuda para o grupo
    context.bot.send_message(chat_id=update.effective_chat.id, text=ajuda_texto)

# Configurar o bot e os handlers de comandos e mensagens
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('plantonista', plantonista_do_dia))
dispatcher.add_handler(CommandHandler('ajuda', ajuda))

# Iniciar o bot
updater.start_polling()

# Mantém o bot em execução
updater.idle()

# Termina o bot
updater.stop()
