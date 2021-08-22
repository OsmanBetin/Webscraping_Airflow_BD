import os
import json

# Name of directories
dir_config = 'Config'
dir_script = 'scripts'
dir_base = 'Webscraping_Airflow_BD'

cur_dir = os.getcwd()

def generate_full_path(curr_dir: str, name_dir_base: str, dir_add: str) -> str:
    try:
        list_cur_dir = curr_dir.split('/')
        index_dir_base = list_cur_dir.index(name_dir_base)
        # Generate new list
        new_dir = list_cur_dir[:index_dir_base + 1]
        # Add the new dir
        new_dir.append(dir_add)

        # Generate the full path for new directory
        return '/'.join(new_dir)
    except ValueError:
        return None

# print(generate_full_path(cur_dir, dir_base, dir_config))
# print(generate_full_path(cur_dir, dir_base, dir_script))
full_path_config = generate_full_path(cur_dir, dir_base, dir_config)
full_path_config = full_path_config + '/' + 'config.json'

# read the config file
with open(full_path_config) as config_file:
    file_json = json.load(config_file)
    print(file_json)
    print()
    print(file_json['web_page'])

