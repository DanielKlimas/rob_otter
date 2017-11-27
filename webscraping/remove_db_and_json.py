import os
import sys
import re
from webscraping_model import *

json_file = get_ini()['json_name']
db_file = re.sub(r'sqlite:///','',get_ini()['db_name'])

command_db = "rm -rf " + db_file
command_json = "rm -rf " + "google_scraper" + os.sep + "google_scraper" + os.sep + "spiders" + os.sep + json_file

os.system(command_db)
os.system(command_json)

print("removed {} and {}".format(db_file,json_file))
