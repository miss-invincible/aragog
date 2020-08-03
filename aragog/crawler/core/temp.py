from . import parser
import time
import logging


def crawlTheUrl():
    logger = logging.getLogger(__name__)
    logger.error("heeedcd")
    urlSet = set()
    seed_url = "https://docs.python.org/"
    logger.error("checking for: " + seed_url)
    parser.htmlParse(seed_url, urlSet)
    visited = {seed_url: True}
    while len(urlSet):
        url = urlSet.pop()
        # logger.error("checking for: ", url, "set len ", len(urlSet))
        if url.encode(' ascii', 'ignore') not in visited.keys():
            logger.error("visiting: " + url)
            # print("visiting: ", url, "set len ", len(urlSet))
            for i in range(5):
                print("waiting...", i)
                time.sleep(1)
            parser.htmlParse(url, urlSet)
            visited[url] = True
    return visited
