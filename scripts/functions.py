import json

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

def get_value_from_config(full_path: str, key: str) -> str:
    try:
        with open(full_path) as f:
            file_json = json.load(f)
            return file_json[key]
    except KeyError:
        print('Key not in Config file')
        return None
    except FileNotFoundError:
        print('File Not found in the directory passed')
        return None

