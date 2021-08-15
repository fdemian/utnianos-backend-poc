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

courses_plans = Table('career_plan_courses',
 Base.metadata,
 Column('career_plan_id', ForeignKey('career_plans.id')),
 Column('course_id', ForeignKey('courses.id'))
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
    career_plan_id = Column(Integer, ForeignKey('career_plans.id'), nullable=True)

    career_plan = relationship("CareerPlan", uselist=False)


# Course (e.j) mathematical analysis.
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(255), nullable=False)

    orientation = Column(Unicode(255), nullable=False)
    code = Column(Unicode(255), nullable=False)
    lecture_time = Column(Unicode(255), nullable=False)
    link_to_doc = Column(Unicode(255), nullable=False)
    area_id = Column(Integer, ForeignKey('areas.id'))
    department_id = Column(Integer, ForeignKey('deparments.id'))
    year = Column(Integer, nullable=False)

    # Composiste attributes (w/rel to other tables).
    area = relationship("Area", uselist=False)
    department = relationship("Department", uselist=False)


class CoursePrerrequisites(Base):
  __tablename__ = 'course_prerrequisites'
  id = Column(Integer, primary_key=True, nullable=False)
  course_id = Column(Integer, ForeignKey('courses.id'))
  prerrequisite_id = Column(Integer, ForeignKey('courses.id'))
  type = Column(String(1), nullable=False)
  completion_id = Column(Integer, ForeignKey('completion_status.id'))

class CareerPlan(Base):
  __tablename__ = 'career_plans'
  id = Column(Integer, primary_key=True, nullable=False)
  name = Column(Unicode(255), nullable=False)

  courses = relationship("Course", secondary=courses_plans)

class Department(Base):
    __tablename__ = 'deparments'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(255), nullable=False)

class Area(Base):
    __tablename__ = 'areas'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(255), nullable=False)

class CompletionStatus(Base):
    __tablename__ = 'completion_status'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(255), nullable=False)

class ContribType(Base):
    __tablename__ = 'contrib_types'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Unicode(255), nullable=False)

class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, nullable=False)
    path = Column(Unicode(255), nullable=False)
    type = Column(Unicode(255), nullable=False)
    class_material_id = Column(Integer, ForeignKey('class_materials.id'))

# Temporary name (until someone comes up with something better).
class ClassMaterial(Base):
    __tablename__ = 'class_materials'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'))
    contrib_types = Column(Text, nullable=False)

    files = relationship("File")
    course = relationship("Course", uselist=False)

class CoursesStatus(Base):
    __tablename__ = 'courses_status'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_id = Column(Integer, ForeignKey('courses.id'))
    completion_id = Column(Integer, ForeignKey('completion_status.id'))
