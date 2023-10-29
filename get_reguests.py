import requests
# print(requests.__version__) # так с помощью .__version__ можно смотреть версии установленных библиотек

# r = requests.get('https://api.github.com/events')
# print(r.status_code)
# print(r.headers['content-type'])
# print(r.encoding)
# print(r.text)
# print(r.json())
# print(r)

# response = requests.get("https://httpbin.org/get")

# if response.status_code == 200:
#     print("OK!")

# if response.ok:
#     print("OK!")

# response.raise_for_status()

# print(response)

# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# response = requests.get("https://httpbin.org/get", params=payload)

# response.text
# print(response.url)

# url = 'https://httpbin.org/get'
# url = 'https://api.github.com/events'

# response = requests.get(url)
# print(response.encoding)
# response.encoding = 'ISO-8859-1'

# print(response.encoding)
# print(response.content)
# print(response.text)
# print(response.json)
# r = response.json

# print(response.raise_for_status)
# print(response.status_code)

# response = requests.get('https://api.github.com', stream=True)
# response.raw
# # response.raw.read(10)
# print(response)

url = 'https://api.github.com/some/endpoint'
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)

print(r)


