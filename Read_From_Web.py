'''
Скачиваем все анкеты с сайта http://police.mosyabloko.ru/json и преобразуем обратно в объект Питон
Обращаем внимание, что все нестандартные символы - т.е. все, кроме стандартной латиницы,
представлены в JSON-выводе в виде кодов.
Преобразованию подверглись русские буквы, буквы с диакритикой во французском и польском языках.
В процессе обратного преобразования они были корректно восприняты.
'''
import json
from urllib.request import urlopen

responce = urlopen('http://police.mosyabloko.ru/json').read().decode('utf-8')

alldict = json.loads(responce)

for onekey, onedict in alldict.items():
    print('-Анкета--', onekey, '---')
    for key, value in onedict.items():
        print(key, value)
    print('--------------------')