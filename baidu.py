import requests
url = "https://www.baidu.com"
response = requests.get(url)
print(type(response))
print(type(response.text))
print(response.text)
