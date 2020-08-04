from . import parser
import time
import logging
from urllib.parse import urlparse
from ..constants import parser as parser_constants


def crawlTheUrl(url):
    logger = logging.getLogger(__name__)
    parsed_url = urlparse(url)
    if parsed_url.scheme == '':
        parsed_url.scheme = parser_constants.DEFAULT_URL_SCHEME
    seed_url = parsed_url.geturl()
    url_set = set()
    logger.error("checking for: " + seed_url)
    parser.htmlParse(seed_url, seed_url, url_set)
    visited = {seed_url: True}
    result = {}
    cnt = 0
    while len(url_set):
        if cnt == 10:
            break
        logger.error("reached here..." + str(cnt))
        url = url_set.pop()
        if url.encode(parser_constants.URL_DECODING, 'ignore') not in visited.keys():
            logger.error("visiting: " + url)
            # for i in range(5):
            #     logger.error("waiting..." + str(i))
            #     time.sleep(1)
            parser.htmlParse(seed_url, url, url_set, result)
            visited[url] = True
        cnt += 1
    return result
