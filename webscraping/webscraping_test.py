import pytest
import webscraping
from html_parser import read_generator as get_version
from datetime import datetime

def test_get_version():

    timeout = 5
    time_now = datetime.now()

    generator,time = get_version("http://orf.at",timeout)
    assert generator == "O/A"
    assert type(time) == type(time_now)

    generator,time = get_version("http://heise.de",timeout)
    assert generator == "InterRed V16.6, http://www.interred.de/, InterRed GmbH"
    assert type(time) == type(time_now)

    generator,time = get_version("http://swanmay.com",timeout)
    assert generator == "WordPress.com"
    assert type(time) == type(time_now)


def test_make_dict_for_db():

    time_now = datetime.now()

    links = ["http://www.orf.at","http://www.heise.de","http://www.swanmay.com"]

    dict_for_db = webscraping.make_dict_for_db(links)

    assert dict_for_db['orf.at'][0] == "O/A"
    assert type(dict_for_db['orf.at'][1]) == type(time_now)

    assert dict_for_db['heise.de'][0] == "InterRed V16.6, http://www.interred.de/, InterRed GmbH"
    assert type(dict_for_db['heise.de'][1]) == type(time_now)

    assert dict_for_db['swanmay.com'][0] == "WordPress.com"
    assert type(dict_for_db['swanmay.com'][1]) == type(time_now)

def test_percent():

    assert webscraping.percent(1,100) == 1.0
    assert webscraping.percent(1,50) == 2.0
    assert webscraping.percent(5,100) == 5.0
