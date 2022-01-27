import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = 'https://rezka.ag/'
URL = 'https://rezka.ag/series/fantasy/'

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
}


@csrf_exempt
def get_html(url, params=''):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


@csrf_exempt
def get_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='b-content__inline_item')
    series = []

    for item in items:
        series.append(
            {
                'title': item.find('div', class_="b-content__inline_item-link").get_text(strip=True),
                'image': HOST + item.find('div', class_="b-content__inline_item-cover").find('img').get('src')
            }
        )

    return series


@csrf_exempt
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        series = []
        for page in range(0, 1):
            html = get_html(URL, params={'page': page})
            series.extend(get_data(html.text))
            return series
    else:
        raise ValueError('!!!_ERROR_IN_PARSER_!!!')

