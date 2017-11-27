import os
import sys

from datetime import datetime

from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker

from webscraping_model import *

from html_parser import read_generator as get_version_and_time

from pprint import pprint
from prettytable import PrettyTable

#------------------------------------------------------------------------
#   MAIN
#------------------------------------------------------------------------
def main(argv):

    execute_scraper()
    print("\nscraping done\n")

    links = get_json_links()
    dataset = make_dict_for_db(links)
    make_db(dataset)
    print("\nmake db done\n")

    print_values_db()


#------------------------------------------------------------------------
#   Make the db entries
#------------------------------------------------------------------------
def make_db(dataset):

    session = start_db_session()


    for key, value in dataset.items():

        new_domain = Domain(dom_name=key)
        session.add(new_domain)
        session.commit()

        new_generator = Generator(gen_name=value[0], time_visited=value[1], dom_name = new_domain)
        session.add(new_generator)
        session.commit()

#------------------------------------------------------------------------
#   get percent of a whole
#------------------------------------------------------------------------
def percent(part,whole):
    return 100 * float(part)/float(whole)

#------------------------------------------------------------------------
#   print the rate of generator
#------------------------------------------------------------------------
def print_values_db():

    session = start_db_session()

    entries = session.query(func.count(Generator.gen_name)).all()[0][0]
    print("\ninsgesamt {} Domänen gefunden:".format(entries))

    names = session.query(Generator.gen_name).all()
    namelist = []
    for name in names:
        name = name[0]
        namelist.append(name)

    namelist = set(namelist)
    namelist = list(namelist)

    t = PrettyTable(["Rate","in % ","Name Generator"])
    for name in namelist:
        counter = session.query(func.count(Generator.gen_name)).filter(Generator.gen_name == name).first()[0]
        t.add_row([counter,percent(counter,entries),name])

    print(t)
#------------------------------------------------------------------------
#   start the db session
#------------------------------------------------------------------------
def start_db_session():

    config_dict = get_ini()
    db_name = config_dict['db_name']
    engine = create_engine(db_name)
    Base.metadata.bind = engine

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    return session

#------------------------------------------------------------------------
#   make a dict for the db
#------------------------------------------------------------------------
def make_dict_for_db(links):

    ini_dict = get_ini()
    timeout = int(ini_dict['timeout_response'])

    db_dict = {}

    for link in links:
        generator, timestamp = get_version_and_time(link,timeout)
        link = re.sub(r'http://www.','',link)
        db_dict[link] = [generator,timestamp]
        print("link: {} gen: {} time:{}".format(link,db_dict[link][0],db_dict[link][1]))

    return db_dict


#------------------------------------------------------------------------
#   execute the scraper scrapy
#------------------------------------------------------------------------
def execute_scraper():

    path_now = os.getcwd()
    command = "scrapy crawl google -o " + get_ini()['json_name']
    path_execute = "google_scraper" + os.sep + "google_scraper" + os.sep + "spiders" + os.sep
    os.chdir(path_execute)
    os.system(command)
    os.chdir(path_now)



###############################################################
if __name__ == '__main__':
    main(sys.argv)


