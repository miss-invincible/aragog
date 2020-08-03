# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from . import parser
import time
import logging

# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
#

# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#     # aragog.aragog("shivangi")
#     # url_fetcher.make_request("https://medium.com/")
#     # data_parser.parse("http://avi.im/stuff/js-or-no-js.html")
#     # print(data_parser.html_parse("https://medium.com/"))
#     seed_url = "https://docs.python.org/"
#     urlSet = set()
#     parser.htmlParse(seed_url, urlSet)
#     visited = {seed_url: True}
#     while len(urlSet):
#         url = urlSet.pop()
#         if url.encode('ascii', 'ignore') not in visited.keys():
#             print("visiting: ", url, "set len ", len(urlSet))
#             for i in range(5):
#                 print("waiting...", i)
#                 time.sleep(1)
#             parser.htmlParse(url, urlSet)
#             visited[url] = True
#     # urls = data_parser.html_parse(seed_url)
#     # while len(urls):


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

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