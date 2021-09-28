"""
Busca de clima usando API https://home.openweathermap.org/
"""
import requests

token = ''
city = input('Qual o nome da cidade que deseja visualizar as temperaturas?:')
url = 'http://api.openweathermap.org/data/2.5/weather?&appid=' + token + '&q=' + city
print(url)
requisicao_clima = requests.get(url)
clima = requisicao_clima.json()

if clima["cod"] != "404":
    desc = clima["weather"]
    temp_atual = round((clima["main"]["temp"]) - 273.15)
    temp_min = round((clima["main"]["temp_min"]) - 273.15)
    temp_max = round((clima["main"]["temp_max"]) - 273.15)
    descricao = desc[0]["description"]
    print(f'Temperatura atual: {temp_atual}\n'
          f'Temperatura minima: {temp_min}\n'
          f'Temperatura máxima: {temp_max}\n'
          f'Descrição: {descricao}')

else:
    print("Cidade não encontrada")
