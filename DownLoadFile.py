from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
import requests
try:
    from urllib.request import urlretrieve
except ImportError:  # Python 2
    from urllib import urlretrieve
def download_file(url, filename):
    """
    Downloads a file from the 'url' and saves it under 'filename'.
    """
    sl = BuiltIn().get_library_instance('SeleniumLibrary')
    cookie = dict()
    cookie = sl.get_cookies(True)  # User must have done login before calling this
    # logger.info('cookies %s' % cookie)
    s = requests.Session()
    cj = requests.cookies.cookiejar_from_dict(cookie)
    logger.info('Downloading %s' % url)
    r = s.get(url, cookies=cj)
    # print("response was: %s" % r.text)
    with open(filename, mode='wb') as localfile:
        localfile.write(r.content)
    #sl.go_to(url)
    #urlretrieve(url, filename)
    return filename