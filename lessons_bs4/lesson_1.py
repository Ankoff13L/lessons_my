from bs4 import BeautifulSoup

"""Передача открытого объекта файла"""
with open("index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

"""Передача строки"""
soup = BeautifulSoup("<html>a web page</html>", 'html.parser')
















html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.a)
# print(soup.a.name)
# print(soup.a.string)
# print(soup.a.parent.name)
# print(soup.find_all('a'))
# print(soup.find(id='link3'))



# print(soup.p)
# print(soup.p['class'])

"""Найти и извлечь все URL-адреса"""
# for link in soup.find_all('a'):
#     print(link.get('href'))

"""Извлесь весь текст со страницы"""
print(soup.get_text())











