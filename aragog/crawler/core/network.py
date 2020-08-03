import requests
import logging
from requests.exceptions import HTTPError
from ..constants import error
from ..constants import network


def makeGetRequest(url):
    logger = logging.getLogger(__name__)
    response = requests.get(url=url, headers=getRequestHeaders())
    logger.error(response)
    response.raise_for_status()
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
