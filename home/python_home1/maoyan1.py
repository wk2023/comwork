import requests


def get_one_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
        }
    response = requests.get(url, headers=headers)
    return response.text
# return None

def main():
    url = 'http://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

main()
