# pip3 install beautifulsoup4 lxml
from bs4 import BeautifulSoup



# tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
# tag['id'] = 'verybold'
# tag['another-attribute'] = 1

# del tag['id']
# del tag['another-attribute']

# print(tag)

# css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
# print(css_soup.p['class'])

# id_soup = BeautifulSoup('<p id="my id"></p>', 'html.parser')
# # print(id_soup.p['id'])
# print(id_soup.p.get_attribute_list('id'))


# rel_soup = BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'html.parser')
# print(rel_soup.a['rel'])

# rel_soup.a['rel'] = ['index', 'contents']
# print(rel_soup.p)

# no_list_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser', multi_valued_attributes=None)
# print(no_list_soup.p['class'])

# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
# print(xml_soup.p['class'])

class_is_multi= { '*' : 'class'}
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
print(xml_soup.p['class'])






"""Найти и извлечь все URL-адреса"""
# for link in soup.find_all('a'):
#     print(link.get('href'))

"""Извлесь весь текст со страницы"""
# print(soup.get_text())


"""Из Python2day"""


# with open("index.html") as file:
#     src = file.read()

# print(src)

# soup = BeautifulSoup(src, "lxml")

# title = soup.title
# print(title)
# print(title.text)
# print(title.string)k

"методы find() и find_all()"

# page_h1 = soup.find("h1")
# print(page_h1)
# print(page_h1.text)


# tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b

# class_is_multi= { '*' : 'class'}
# xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml', multi_valued_attributes=class_is_multi)
# xml_soup.p['class']
# ['body', 'strikeout']


