from sqlalchemy import create_engine
from os import path
from configUtils import get_database_url, parse_config_file

config_file = '../config.json'
config_file_path = path.join(path.dirname(__file__), config_file)

def get_database_url(options):
    user = options['database']['user']
    password = options['database']['password']
    port = options['database']['port']
    return 'postgresql+psycopg2://' + user + ":" + password + "@localhost:" + port

def create_database():
    options = parse_config_file(config_file_path)
    
    connection_string = get_database_url(options)
    database_name = options['database']['name']
    engine = create_engine(connection_string)

    conn = engine.connect()
    conn.execute("commit")
    conn.execute("create database " + database_name)
    conn.close()


create_database()
