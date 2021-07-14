# flask_sqlalchemy/models.py
from sqlalchemy import *
from sqlalchemy.orm import (
 scoped_session,
 sessionmaker,
 relationship,
 backref
)
from sqlalchemy.ext.declarative import declarative_base
from .sessionHelper import get_session
from os import path

config_file = '../../config.json'
config_file_path = path.join(path.dirname(__file__), config_file)

db_session = get_session(config_file_path)
Base = declarative_base()
Base.query = db_session.query_property() # We will need this for querying

material_type_association = Table(
  'materials_types',
  Base.metadata,
  Column('class_materials_id', Integer, ForeignKey('class_materials.id')),
  Column('contrib_types_id', Integer, ForeignKey('contrib_types.id'))
)

# If the user uses oauth salt and password are null.
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False)
    avatar = Column(Text, nullable=True)
    username = Column(Unicode(50), nullable=False)
    fullname = Column(Unicode(100), nullable=True)
    email = Column(Unicode(255), nullable=False)
    password = Column(LargeBinary, nullable=True)
    salt = Column(LargeBinary, nullable=True)
    valid = Column(Boolean, nullable=False)
    failed_attempts = Column(Integer, nullable=False)
    lockout_time = Column(DateTime, nullable=True)

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(255), nullable=False)

class ContribType(Base):
    __tablename__ = 'contrib_types'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(255), nullable=False)

# Temporary name (until someone comes up with something better).
class ClassMaterial(Base):
    __tablename__ = 'class_materials'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    file_path = Column(Text, nullable=True)
    course_id = Column(Integer, ForeignKey('courses.id'))
    contrib_types = Column(Text, nullable=False)

    course = relationship("Course", uselist=False)
