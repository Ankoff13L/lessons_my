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

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
response = requests.get("https://httpbin.org/get", params=payload)

print(response.url)

