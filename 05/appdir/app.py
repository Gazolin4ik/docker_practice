import requests

url = 'https://google.com'
response = requests.get(url)
print(f'Статус ответа: {response.status_code}')