import telebot

chaveAPI = "6706522782:AAGZDff-S-L2QNsHqzGgohORMCN6EGNsnAY"
bot = telebot.TeleBot(chaveAPI)


@bot.message_handler(commands=["alemenezes"])
def alemenezes(mensagem):
    texto_alemenezes = """
    Saiba mais sobre o meu trabalho!
menezesalexandre_dev 👨‍💻 Programador Full-Stack
HTML | CSS | JavaScript | Python | MySQL | Git
GitHub: https://encurtador.com.br/qGHO3
LinkedIn: https://encurtador.com.br/bkqt2"""
    bot.send_message(mensagem.chat.id, texto_alemenezes)


#MENSAGENS GERAIS:


def verificar(mensagem):
   return True


@bot.message_handler(func=verificar)
def responder(mensagem):
    print(mensagem)
    texto = f"""
    Olá, {mensagem.from_user.first_name} {mensagem.from_user.last_name}!
Selecione uma opção para continuar (Clique no item):
/brasileirao Ver tabela do Brasileirão 
/dataclima Ver a data e clima de hoje
/alemenezes Ver mais do trabalho de menezesalexandre_dev
Selecione uma das opções disponíveis acima"""
    bot.send_message(mensagem.chat.id, texto)


bot.polling()
