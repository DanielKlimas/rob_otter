import configparser
import json
import re
import os

from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#-----------------------------------------------------------
#   Get ini db name
#-----------------------------------------------------------
def get_ini():

    config = configparser.ConfigParser()
    config.read("webscraping.ini")
    config.sections()
    config_dict = dict(config['config'])


    return config_dict
#----------------------------------------------------------
#   Get the json file in a list of links with http:// in front
#----------------------------------------------------------
def get_json_links():


    old_path = os.getcwd()
    path = os.getcwd() + os.sep + "google_scraper" + os.sep + "google_scraper" + os.sep + "spiders" + os.sep
    json_file = get_ini()['json_name']

    os.chdir(path)
    link_dict_list = json.load(open(json_file))
    os.chdir(old_path)

    links =[]

    for link in link_dict_list:

        link = link['link']
        link = re.sub(r'^https://',"",link)
        link = re.sub(r'^www.',"",link)
        link = link.split("/")[0]
        link = link.split(" ")[0]
        link = "http://www." + link
        links.append(link)

    links = set(links)
    links = list(links)

    return links




Base = declarative_base()

#-----------------------------------------------------------
#   Classes
#-----------------------------------------------------------
class Domain(Base):
    __tablename__ = 'domain'
    dom_id = Column(Integer, primary_key=True)
    dom_name = Column(String(250), nullable=False)

class Generator(Base):
    __tablename__ = 'generator'
    dom_id = Column(Integer, ForeignKey('domain.dom_id'))
    gen_id = Column(Integer, primary_key=True)
    gen_name = Column(String(250), nullable=False)
    time_visited = Column(DateTime)
    dom_name = relationship(Domain)


#-----------------------------------------------------------
#   generation db
#-----------------------------------------------------------
config_dict = get_ini()
engine = create_engine(config_dict['db_name'])

Base.metadata.create_all(engine)
