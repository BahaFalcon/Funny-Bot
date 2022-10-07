import requests
import bs4


headers = {'User-Agent': 'Mozilla/5.0'}
url = 'https://www.anekdot.ru/author-best/years/?years=anekdot'

response = requests.get(url)
soup = bs4.BeautifulSoup(response.text, 'lxml')
container = soup.select_one('div', class_='topicbox')
texts = list(soup.find_all('div', class_='text'))

lst_text =[]
for u in range(len(texts)):
    content = texts[u]
    con = content.text,
    lst_text.append(con)
