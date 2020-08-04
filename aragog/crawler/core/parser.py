from bs4 import BeautifulSoup
import urljoin
from urllib.parse import urlparse
import logging
from ..constants import parser
from . import network


def htmlParse(seed_url, url, st=None, result={}):
    logger = logging.getLogger(__name__)
    if st is None:
        st = set()
    current_page_children = set()
    logger.error("Making network call for url: " + url)
    content = network.makeGetRequest(url)

    if content is None:
        return None
    logger.error("Request done successfully")
    soup = BeautifulSoup(content, parser.SOUP_DECODER)
    for tag in soup.find_all(href=True):
        if is_internal_link(tag[parser.LINK_ATTR]):
            if urlparse(tag[parser.LINK_ATTR]).netloc == '':
                url = urljoin.url_path_join("https://docs.python.org/", tag[parser.LINK_ATTR])
                st.add(url)
                current_page_children.add(url)
            else:
                st.add(tag[parser.LINK_ATTR])
                current_page_children.add(tag[parser.LINK_ATTR])
    result[url] = current_page_children
    return st


def is_internal_link(link):
    return urlparse(link).netloc == "docs.python.org" or urlparse(link).netloc == ''
