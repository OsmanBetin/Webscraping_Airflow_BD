import os
from functions import generate_full_path, get_value_from_config

# Name of directories
dir_config = 'Config'
dir_script = 'scripts'
dir_base = 'Webscraping_Airflow_BD'

cur_dir = os.getcwd()

full_path_config = generate_full_path(cur_dir, dir_base, dir_config)
full_path_config = full_path_config + '/' + 'config.json'
print('Full Config path ', full_path_config)

def get_value_config(key):
    try:
        value_config = get_value_from_config(full_path_config, key)
        # print('Value Config ', value_config)
        return value_config
    except TypeError as e:
        print('Missing required positional argument ', e)
        return None

