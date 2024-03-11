import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os

url = 'https://docs.aiogram.dev/en/latest/api/bot.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

sidebar_tree = soup.find('div', class_='sidebar-tree')
if not sidebar_tree:
    print("Ветвь <div class='sidebar-tree'> не найдена на странице.")
    exit()

links = sidebar_tree.find_all('a', class_='reference internal')
links_dict = {}

for link in links:
    title = link.text
    href = link.get('href')
    full_url = urljoin(url, href)
    links_dict[title] = full_url

# count = 0
# for k, v in links_dict.items():
#     count += 1
#     print(f'Страница №{count} {k} - адресс {v}')

with open('links_data.txt', 'w', encoding='UTF-8') as file:
    count = 0
    for key, value in links_dict.items():
        count += 1
        file.write(f'Страница №{count} {key} имеет адрес {value}\n')

print('Данные успешно записаны в файл links_data.txt')

# Создаем папку data_files, если она еще не существует
if not os.path.exists('data_files'):
    os.makedirs('data_files')

for title, url in links_dict.items():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    article_main = soup.find('article', role='main')
    if article_main:
        text_content = article_main.get_text()

        # Очищаем название страницы от недопустимых символов
        clean_title = title.replace("(", "").replace(")", "").replace(">", "").replace("<", "").replace("?", "_")

        file_path = os.path.join('data_files', f'{clean_title}.txt')
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_content)

        print(f'Текст с {title} успешно сохранен в файл {file_path}')
    else:
        print(f'На странице {url} не найден элемент <div class=\'content\'>')

print('Процесс завершен.')
