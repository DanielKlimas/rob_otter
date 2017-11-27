import requests
from lxml import html
from pprint import pprint
from datetime import datetime



def read_generator(url,timeout_response):

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'

    headers = {'User-Agent': user_agent}

    try: response = requests.get(url, headers = headers, timeout = timeout_response)
    except: return ("response error", datetime.now())

    try: tree = html.fromstring(response.text)
    except ValueError: return ("Unicode String", datetime.now())

    try: version = tree.xpath("//meta[@name='generator']/@content")[0]
    except IndexError: version = "O/A"


    return (version, datetime.now())



