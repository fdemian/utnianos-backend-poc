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
 Column('career_plan_code', ForeignKey('career_plans.code')),
 Column('course_code', ForeignKey('courses.code'))
)

class CoursesPlans(Base):
    __tablename__ = 'career_plan_courses'
    __table_args__ = {'extend_existing': True}

    career_plan_code = Column(
      Unicode(255),
      ForeignKey('career_plans.code'),
      nullable=False,
      primary_key=True
    )
    course_code = Column(
      Unicode(255),
      ForeignKey('courses.code'),
      nullable=False,
      primary_key=True
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
    career_plan_code = Column(Unicode(255), ForeignKey('career_plans.code'), nullable=True)

    career_plan = relationship("CareerPlan", uselist=False)


# Course (e.j) mathematical analysis.
class Course(Base):
    __tablename__ = 'courses'

    name = Column(Unicode(255), nullable=False)
    code = Column(Unicode(255), nullable=False, primary_key=True)
    year = Column(Integer, nullable=False)
    orientation = Column(Unicode(255), nullable=True)
    lecture_time = Column(Unicode(255), nullable=True)
    link_to_doc = Column(Unicode(255), nullable=True)
    area_id = Column(Integer, ForeignKey('areas.id'))
    department_id = Column(Integer, ForeignKey('deparments.id'))

    # Composiste attributes (w/rel to other tables).
    area = relationship("Area", uselist=False)
    department = relationship("Department", uselist=False)


class CoursePrerrequisites(Base):
  __tablename__ = 'course_prerrequisites'
  id = Column(Integer, primary_key=True, nullable=False)
  course_code = Column(Unicode(255), ForeignKey('courses.code'))
  prerrequisite_code = Column(Unicode(255), ForeignKey('courses.code'))
  type = Column(String(1), nullable=False)
  completion_code = Column(Integer, ForeignKey('completion_status.status'))

class CareerPlan(Base):
  __tablename__ = 'career_plans'
  code = Column(Unicode(255), nullable=False, primary_key=True)
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
    status = Column(Unicode(255), primary_key=True, nullable=False)
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
    course_code = Column(Integer, ForeignKey('courses.code'))
    contrib_types = Column(Text, nullable=False)

    files = relationship("File")
    course = relationship("Course", uselist=False)

class CoursesStatus(Base):
    __tablename__ = 'courses_status'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    course_code = Column(Integer, ForeignKey('courses.code'))
    completion_code = Column(Integer, ForeignKey('completion_status.status'))
