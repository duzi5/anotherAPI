from bs4 import BeautifulSoup
import requests

resposta = requests.get('https://www.google.com/search?q=cotacao+do+dolar+site&rlz=1C5CHFA_enBR995BR995&oq=cotacao+do+dolar+site&aqs=chrome..69i57j0i22i30l8.6124j1j4&sourceid=chrome&ie=UTF-8')

soup = BeautifulSoup(resposta.text, 'html.parser')

x = soup.find('span', class_='FCUp0c rQMQod').text

x = float(x.replace('R$', '').replace(',', '.').replace(' ', ''))

print(x)