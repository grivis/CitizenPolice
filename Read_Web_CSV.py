import json
import csv
import time
from urllib.request import urlopen

responce = urlopen('http://police.mosyabloko.ru/json').read().decode('utf-8')

alldict = json.loads(responce)
trans = {'yes':'Да', 'no':'Нет'}

tics = time.time()
lt = time.localtime(tics)
day = str(lt.tm_mday)
month = str(lt.tm_mon)
year = str(lt.tm_year)
hour = str(lt.tm_hour)
min = str(lt.tm_min)

filename = year+month+day+hour+min+'.csv'
csvFile = open(filename, 'wt', encoding='utf-8')
writer = csv.writer(csvFile)
writer.writerow((
    'Файл анкеты',
'Учреждение',
'Адрес',
'Дата',
'Время',
'Участник 1',
'Телефон',
'Участник 2',
'Участник 3',
'Вопрос 1',
'Вопрос 2',
'Вопрос 3',
'Вопрос 4',
'Вопрос 5',
'Вопрос 6',
'Вопрос 7',
'Вопрос 8',
'Вопрос 9',
'Вопрос 10',
'Вопрос 11',
'Вопрос 12',
'Вопрос 13',
'Вопрос 14',
'Вопрос 15',
'Вопрос 16',
'Вопрос 17',
'Вопрос 18',
'Вопрос 19',
'Вопрос 20',
'Вопрос 21',
'Вопрос 22',
'Вопрос 23',
'Вопрос 24',
'Вопрос 25',
'Вопрос 26',
    'Отзывы',
    'Ожидание',
    'Компетентность',
    'Комментарии'))

for onekey, onedict in alldict.items():
    writer.writerow((
    onekey,
    onedict['OrgName'],
    onedict['OrgAddr'],
    onedict['Date'],
    onedict['Time'],
    onedict['FIO1'],
    onedict['Phone'],
    onedict['FIO2'],
    onedict['FIO3'],
    trans[onedict['Q1']],
    trans[onedict['Q2']],
    trans[onedict['Q3']],
    trans[onedict['Q4']],
    trans[onedict['Q5']],
    trans[onedict['Q6']],
    trans[onedict['Q7']],
    trans[onedict['Q8']],
    trans[onedict['Q9']],
    trans[onedict['Q10']],
    trans[onedict['Q11']],
    trans[onedict['Q12']],
    trans[onedict['Q13']],
    trans[onedict['Q14']],
    trans[onedict['Q15']],
    trans[onedict['Q16']],
    trans[onedict['Q17']],
    trans[onedict['Q18']],
    trans[onedict['Q19']],
    trans[onedict['Q20']],
    trans[onedict['Q21']],
    trans[onedict['Q22']],
    trans[onedict['Q23']],
    trans[onedict['Q24']],
    trans[onedict['Q25']],
    trans[onedict['Q26']],
    onedict['reviews'],
    onedict['wait'],
    onedict['competence'],
    onedict['comments']))

csvFile.close()


    #
    # print('-Анкета--', onekey, '---')
    # for key, value in onedict.items():
    #     print(key, value)
    # print('--------------------')