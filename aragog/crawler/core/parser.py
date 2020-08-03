from bs4 import BeautifulSoup
import urljoin
from urllib.parse import urlparse
import logging
from ..constants import parser
from . import network


def htmlParse(url, st=None):
    logger = logging.getLogger(__name__)
    if st is None:
        st = set()
    content = network.makeGetRequest(url)
    if content is None:
        return None
    soup = BeautifulSoup(content, parser.SOUP_DECODER)
    base_url = "https://docs.python.org"
    for tag in soup.find_all(href=True):
        if is_internal_link(tag[parser.LINK_ATTR]):
            if urlparse(tag[parser.LINK_ATTR]).netloc == '':
                url = urljoin.url_path_join(base_url, tag[parser.LINK_ATTR])
                st.add(url)
            else:
                st.add(tag[parser.LINK_ATTR])
    return st


def is_internal_link(link):
    return urlparse(link).netloc == "docs.python.org" or urlparse(link).netloc == ''
