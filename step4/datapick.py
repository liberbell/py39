from pydoc import resolve
import requests

URL = "https://www.yahoo.co.jp"

response = requests.get(URL)
print(response.status_code)
# print(response.text)

# print(response.content)
print(response.encoding)
print(response.headers)