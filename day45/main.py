from bs4 import BeautifulSoup
import requests

response = requests.get('https://news.ycombinator.com/')
html_data = response.text

soup = BeautifulSoup(html_data, 'html.parser')

news_list = soup.select(selector='.athing')

for elem in news_list:
    print(elem.select_one(selector='.rank').text, elem.select_one(selector='.titlelink').text)

# with open('day45/website.html') as f:
#     content = f.read()

# soup = BeautifulSoup(content, 'html.parser')

# a_tag = soup.find_all(name='a')

# for tag in a_tag:
#     print(tag.get('href'))

# liste = [(att, 'func' if callable(getattr(tag, att)) else 'attr') for att in dir(tag)]
# func_liste = [elem for elem in liste if elem[1] == 'func']
# attr_liste = [elem for elem in liste if elem[1] == 'attr']