import os

import requests
import bs4

headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://pixmafia.ru/humor/625-do-slez-smeshnye-memy-i-kartinki.html'

response = requests.get(url, headers=headers)

soup = bs4.BeautifulSoup(response.text, 'lxml')
container = soup.select_one('article', class_='article')
images = container.find('div', class_='fdesc full-text video-box clearfix').find_all('img')


images_path = 'my_images'
if not os.path.exists(images_path):
    os.mkdir(images_path)

# Рабочий код, загружает все картинки в нужную папку('my_images')
img_list = []
for image in images:
    src = image.get('src')
    img_list.append(src)

for pic_link in img_list:
    with open('my_images/' + pic_link.split('/')[-1], 'wb') as f:
        f.write(requests.get('https://pixmafia.ru/' + pic_link).content)


# Рабочий код, загружает все картинки, но в текущую директорию
# img_list = []
# for image in images:
#     src = image.get('src')
#     img_list.append(src)
# print(img_list)

# через urlretrieve
# for i in img_list:
#     content = urlretrieve('https://pixmafia.ru/' + i, i[34:])
#     print(i[34:], 'скачано')

# через requests
# for i in img_list:
#     p = requests.get('https://pixmafia.ru/' + i)
#     out = open(i[34:], "wb")
#     out.write(p.content)
#     out.close()