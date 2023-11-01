import requests

chave_api_pyowm = os.environ["openWeatherChaveAPI"]
nome_cidade = str(input('Digite o nome da Cidade para ver a previsão do tempo: '))
nome_cidade += ', BR'
link = f"https://api.openweathermap.org/data/2.5/weather?q={nome_cidade}&appid={chave_api_pyowm}&lang=pt_br"

requisicao_pyowm = requests.get(link)
requisicao_dicionario_pyowm = requisicao_pyowm.json()
cidade_pyowm = requisicao_dicionario_pyowm['name']
descricao_pyowm = requisicao_dicionario_pyowm['weather'][0]['description']
temperatura_pyowm = requisicao_dicionario_pyowm['main']['temp']
umidade_pyowm = requisicao_dicionario_pyowm['main']['humidity']
visibilidade_pyowm = requisicao_dicionario_pyowm['visibility']
print(f'Cidade: {cidade_pyowm}\n'
      f'Descrição: {descricao_pyowm.capitalize()}\n'
      f'Temperatura: {(temperatura_pyowm - 273.15):.2f}°C\n'
      f'Umidade: {umidade_pyowm}%\n'
      f'Visibilidade: {(visibilidade_pyowm / 1000):.0f}km')
