import requests

headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}
url = 'http://maoyan.com/board/4'
response = requests.get(url=url, headers=headers)
print(response.text)
