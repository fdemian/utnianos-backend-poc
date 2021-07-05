import json
from time import sleep
from os import path

def delay_time(delay_per_try, tries):
    seconds = delay_per_try * tries
    sleep(seconds)
    return

def parse_config_file(config_file_path):
    f = open(config_file_path)
    data = json.load(f)
    return data

"""
def get_context(config_path):
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    settings = parse_config_file(config_file_path)
    db_session = get_session(config_file_path)

    return {
      'settings': settings,
      'db_session': db_session
    }
"""
