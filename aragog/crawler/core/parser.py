from bs4 import BeautifulSoup
import urljoin
import requests
from urllib.parse import urlparse
import logging
from requests.exceptions import HTTPError


# def js_parse(url):
#     cap = {"marionette": False}
#     driver = webdriver.Firefox(capabilities=cap)
#     # driver = webdriver.Firefox()
#     driver.get(url)
#     result = driver.execute_script('var text = document.title ; return var')
#     print(result)


def htmlParse(url, st=None):
    logger = logging.getLogger(__name__)
    if st is None:
        st = set()
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                             'AppleWebKit/537.11 (KHTML, like Gecko) '
                             'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
    reg_url = "https:XXXXOOOO"
    response = requests.get(url=url, headers=headers)
    logger.error(response)
    response.raise_for_status()
    try:
        logger.error("Success")
    except HTTPError:
        return
    except Exception as err:
        logger.error(Exception)
        print("Unusual exception occurred", err)
        return

    html = response.content
    soup = BeautifulSoup(html, 'html5lib')
    base_url = "https://docs.python.org"
    for tag in soup.find_all(href=True):
        if is_internal_link(tag['href']):
            if urlparse(tag['href']).netloc == '':
                url = urljoin.url_path_join(base_url, tag['href'])
                print(url)
                st.add(url)
            else:
                st.add(tag['href'])
    return st


def is_internal_link(link):
    return urlparse(link).netloc == "docs.python.org" or urlparse(link).netloc == ''
