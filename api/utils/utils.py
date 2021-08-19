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
