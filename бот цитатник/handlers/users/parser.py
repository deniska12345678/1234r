from aiogram.types import Message
from bs4 import BeautifulSoup
import requests
import random
from aiogram.dispatcher.filters import Text
from loader import dp


URL = 'https://bash.im'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 'accept': '*/*'}

@dp.message_handler(Text(["Цитата"]))
async def parse(message: Message, params=None):
    html = requests.get(URL, headers=HEADERS, params=params)
    soup = BeautifulSoup(html.text, 'html.parser')
    items = soup.find_all('div', class_='quote__frame')
    TEXT =[]
    ID =[]
    for item in items:
        TEXT.append({
            'text': item.find('div', class_ = 'quote__body').get_text(),
        })
        ID.append({
            'id': item.find('a', class_ = 'quote__header_permalink').get_text(),
        })
    quote = TEXT[random.randint(0,25)]
    quote_text = quote['text']
    await message.answer(quote_text)