from pydoc import resolve
from socket import timeout
import requests

URL = "https://www.yahoo.co.jp"

# response = requests.get(URL)
# print(response.status_code)
# print(response.text)

# print(response.content)
# print(response.encoding)
# print(response.headers)
# for key, value in response.headers.items():
#     print(key, "  ", value)

# print(response.cookies)

user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36"
header = {"user_agent": user_agent}

response = requests.get(URL, headers=header)
print(response.status_code)
# for key, value in response.headers.items():
#     print(key, "  ", value)

response = requests.get(URL, headers=header, timeout=5)
print(response.status_code)

URL2 = "https://www.google.com/search"
param = {"q": "python"}

response = requests.get(URL2, params=param)
print(response.status_code)
print(response.text)