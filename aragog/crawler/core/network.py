import requests


def make_request(url):
    headers = {
        'User - Agent': 'Mozilla / 5.0(WindowsNT6.1) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 41.0.2228.0Safari / 537.3'}
    reg_url = 'https:XXXXOOOO'
    # req = Request(url=url, headers=headers)
    html = requests.get(url, headers)
    print html.content
