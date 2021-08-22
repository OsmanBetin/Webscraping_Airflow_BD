import os
import json
from functions import generate_full_path

# Name of directories
dir_config = 'Config'
dir_script = 'scripts'
dir_base = 'Webscraping_Airflow_BD'

cur_dir = os.getcwd()

full_path_config = generate_full_path(cur_dir, dir_base, dir_config)
full_path_config = full_path_config + '/' + 'config.json'

# read the config file
with open(full_path_config) as config_file:
    file_json = json.load(config_file)
    print(file_json)
    print()
    print(file_json['web_page'])

