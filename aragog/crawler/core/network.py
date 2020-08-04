import requests
import logging
from requests.exceptions import HTTPError
from ..constants import error
from ..constants import network


def makeGetRequest(url):
    logger = logging.getLogger(__name__)
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                             'AppleWebKit/537.11 (KHTML, like Gecko) '
                             'Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
    response = requests.get(url=url, headers=headers)
    logger.error(response)
    # response.raise_for_status()
    try:
        logger.error(error.SUCCESS)
        return response.content
    except HTTPError:
        logger.error(error.RESPONSE_WITH_ERROR, HTTPError)
        return None
    except Exception as err:
        logger.error(error.UNEXPECTED_ERROR, err)
        return None


def getRequestHeaders():
    return {'User-Agent': network.USER_AGENT,
            'Accept': network.ACCEPT,
            'Accept-Charset': network.ACCEPT_CHARACTER_SET,
            'Accept-Encoding': network.ACCEPT_ENCODING,
            'Accept-Language': network.ACCEPT_LANGUAGE,
            'Connection': network.CONNECTION}
