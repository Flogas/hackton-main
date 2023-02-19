import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

conn = sqlite3.connect('db.db')
curs = conn.cursor()
curs.execute("DELETE FROM hack")
#curs.execute("INSERT INTO hack VALUES ('NULL','NULL','NULL','NULL') ")

url = 'https://practicum.yandex.ru/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name = soup.select('u')
description = soup.find_all('div', class_='skills-section__card-description')
#date = soup.select('u')
price = soup.find_all('span', class_='skills-section__card-additional-info')
links = soup.find_all('a', class_='link link_theme_normal header__catalog-link')

ol = []
for i in links:
    ol.append(i['href'])

ol = [item.replace("https://practicum.yandex.ru/", "") for item in ol]
ol = [item.replace("https://praktikum.yandex.ru", "") for item in ol]

for i in range(0, len(name)):
    print(name[i].text)
    print('https://practicum.yandex.ru' + ol[i])
    print(description[i].text)
    print(price[i].text)
    curs.execute("INSERT INTO hack VALUES ('{0}','{1}','{2}','{3}') ".format(name[i].text,'https://practicum.yandex.ru'
                                                                             + ol[i],description[i].text,price[i].text))
    conn.commit()
    #print(date[i].text)
    print('\n')

#Geekbrains

print("Geekbrains")

url = 'https://gb.ru/courses?tab=courses'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name = soup.find_all('span', class_='gb-course-card__title-text')
links = soup.find_all('a', class_='gb-course-card__wrapper')

ol = []
for i in links:
    ol.append(i['href'])
+
for i in range(0, len(name)):
    print(name[i].text)
    print('https://gb.ru' + ol[i])
    curs.execute(
        "INSERT INTO hack VALUES ('{0}','{1}','{2}','{3}') ".format(name[i].text, 'https://gb.ru' + ol[i],
                                                                    'NULL','NULL'))
    conn.commit()
    print('\n')

#skillfactory

"""
print("skill factory")

url = 'https://skillfactory.ru/catalogue'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
name = soup.find_all('div', class_='js-store-prod-descr t-store__card__descr t-descr t-descr_xxs')
#links = soup.find_all('a', class_='gb-gu-card__content')

#ol = []
#for i in links:
#    ol.append(i['href'])

for i in range(0, len(name)):
    print(name[i].text)
    #print('https://gb.ru' + ol[i])
    #curs.execute(
       # "INSERT INTO hack VALUES ('{0}','{1}','{2}','{3}') ".format(name[i].text, 'https://gb.ru' + ol[i],
                                                                  #  'NULL','NULL'))
    #conn.commit()
    print('\n')
"""