import requests
url="http://www.centor.cn"

response=requests.get(url)
print(response.text)