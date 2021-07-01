import json

def parse_config_file(config_file_path):
    f = open(config_file_path)
    data = json.load(f)
    return data

def get_database_url(config_file_path):
    options = parse_config_file(config_file_path)
    user = options['database']['user']
    name = options['database']['name']
    port = options['database']['port']
    password = options['database']['password']

    return 'postgresql+psycopg2://' + user + ":" + password + "@localhost:" + port + "/" + name
