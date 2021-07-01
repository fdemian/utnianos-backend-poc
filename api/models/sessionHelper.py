from .configUtils import get_database_url
from sqlalchemy import create_engine
from sqlalchemy.orm import (
 scoped_session,
 sessionmaker,
 relationship,
 backref
)
from os import path
import json

def get_session(config_file):
    connection_string = get_database_url(config_file)
    engine = create_engine(connection_string, convert_unicode=True)
    session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

    return session

def get_global_session(options):
    connection_string = get_database_url(config_file)
    engine = create_engine(connection_string)
    session = sessionmaker(bind=engine)

    return session
