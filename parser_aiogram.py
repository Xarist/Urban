import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
count = 0
for k, v in links_dict.items():
    count += 1
    print(f'Страница №{count} {k} - адресс {v}')

with open('links_data.txt', 'w', encoding='UTF-8') as file:
    count = 0
    for key, value in links_dict.items():
        count += 1
        file.write(f'Страница №{count} {key} имеет адрес {value}\n')

print('Данные успешно записаны в файл links_data.txt')
# print(links_dict)
