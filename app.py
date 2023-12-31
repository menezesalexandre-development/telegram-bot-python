import telebot
import os
import random
import requests
import time
from datetime import date
from dotenv import load_dotenv
from pathlib import Path
from keep_alive import keep_alive

keep_alive()

envPath = Path('.', '.env')
load_dotenv(envPath)

data_atual = date.today()
data_ddmmyyyy = f"{data_atual.day}/{data_atual.month}/{data_atual.year}"

telegramChaveAPI = os.getenv("chaveApiTelegram")
bot = telebot.TeleBot(telegramChaveAPI)


@bot.message_handler(commands=["biscoito_ou_bolacha"])
def biscoito_ou_bolacha(mensagem):
    print(mensagem)
    biscoito_e_bolacha = ['Biscoito', 'Bolacha']
    text_biscoito_e_bolacha = f"""
    É {random.choice(biscoito_e_bolacha)}!"""
    bot.send_message(mensagem.chat.id, text_biscoito_e_bolacha)
    time.sleep(0.2)
    text_biscoito_e_bolacha2 = """
    Tô de brinks, escolhi aleatoriamente"""
    bot.send_message(mensagem.chat.id, text_biscoito_e_bolacha2)


@bot.message_handler(commands=["data_clima"])
def data_clima(mensagem):
    print(mensagem)
    texto_data_clima = """
    Digite o nome de qualquer cidade!"""
    bot.send_message(mensagem.chat.id, texto_data_clima)


@bot.message_handler(commands=["alemenezes"])
def alemenezes(mensagem):
    texto_alemenezes = """
    Saiba mais sobre o meu trabalho!
menezesalexandre_dev 👨‍💻 Programador Full-Stack
HTML | CSS | JavaScript | Python | MySQL | Git
GitHub: http://bit.ly/github_menezesalexandre
LinkedIn: https://bit.ly/linkedin_menezesalexandre"""
    bot.send_message(mensagem.chat.id, texto_alemenezes)


def verificar_clima(mensagem):
    chave_api_pyowm = 'e4301b8a9bd9d49f970948fbd02f5b5f'
    nome_cidade = mensagem.text
    nome_cidade += ', BR'
    link = f"https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={chave_api_pyowm}&lang=pt_br"

    requisicao_pyowm = requests.get(link)
    requisicao_dicionario_pyowm = requisicao_pyowm.json()
    print(f'Requisição OpenWeather: {requisicao_dicionario_pyowm["cod"]}')
    if requisicao_dicionario_pyowm['cod'] == 200:
        return True


@bot.message_handler(func=verificar_clima)
def responder_clima(mensagem):
    chave_api_pyowm = 'e4301b8a9bd9d49f970948fbd02f5b5f'
    nome_cidade = mensagem.text
    nome_cidade += ', BR'
    link = f"https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={chave_api_pyowm}&lang=pt_br"

    requisicao_pyowm = requests.get(link)
    requisicao_dicionario_pyowm = requisicao_pyowm.json()
    cidade_pyowm = requisicao_dicionario_pyowm['name']
    descricao_pyowm = requisicao_dicionario_pyowm['weather'][0]['description']
    temperatura_pyowm = requisicao_dicionario_pyowm['main']['temp']
    umidade_pyowm = requisicao_dicionario_pyowm['main']['humidity']
    visibilidade_pyowm = requisicao_dicionario_pyowm['visibility']
    text_clima = f"""
    {cidade_pyowm.upper()} | {data_ddmmyyyy}
Temperatura: {round(temperatura_pyowm - 273.15):.0f}°C
Descrição: {descricao_pyowm.capitalize()}
Umidade: {umidade_pyowm}%
Visibilidade: {(visibilidade_pyowm / 1000):.0f}km"""
    bot.send_message(mensagem.chat.id, text_clima)


# MENSAGENS GERAIS:
def verificar_geral(mensagem):
    return True


@bot.message_handler(func=verificar_geral)
def responder_geral(mensagem):
    print(mensagem.text)
    texto = f"""
    Olá, {mensagem.from_user.first_name} {mensagem.from_user.last_name}!
Selecione uma opção para continuar (Clique no item):
/biscoito_ou_bolacha Para descobrir se é biscoito ou bolacha
/data_clima ou digite o nome de sua cidade para ver data e clima
/alemenezes Ver mais do trabalho de menezesalexandre_dev
Selecione uma das opções disponíveis acima"""
    bot.reply_to(mensagem, texto)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(non_stop=True, interval=0)
        except Exception as e:
            print(e)
            time.sleep(5)
            continue
