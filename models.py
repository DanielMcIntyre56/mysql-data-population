#!/usr/bin/env python3
import sqlalchemy

from datetime import date
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """
    This is the base class which keeps track of all
    tables and metadata relating to the database.
    """
    pass


# ORM (object relational mapping) classes
# which represent database tables
class Students(Base):
    __tablename__ = "students"
    student_id: Mapped[int] = mapped_column(sqlalchemy.SMALLINT(), autoincrement=True, nullable=False, primary_key=True)  # SMALLINTs are -32,768 to 32,767
    first_name: Mapped[str] = mapped_column(sqlalchemy.VARCHAR(50), nullable=False)
    last_name: Mapped[str] = mapped_column(sqlalchemy.VARCHAR(50), nullable=False)
    enrollment_date: Mapped[date] = mapped_column(sqlalchemy.DATE(), nullable=False)


class Courses(Base):
    __tablename__ = "courses"
    course_id: Mapped[int] = mapped_column(sqlalchemy.SMALLINT(), autoincrement=True, nullable=False, primary_key=True)
    course_name: Mapped[str] = mapped_column(sqlalchemy.VARCHAR(100), nullable=False)
    credits: Mapped[int] = mapped_column(sqlalchemy.SMALLINT(), nullable=False)
    instructor_id: Mapped[int] = mapped_column(sqlalchemy.SMALLINT(), nullable=False) 


class Instructors(Base):
    __tablename__ = "instructors"
    instructor_id: Mapped[int] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(sqlalchemy.String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(sqlalchemy.String(50), nullable=False)
    department: Mapped[str] = mapped_column(sqlalchemy.String(100), nullable=False)


class Enrollments(Base):
    __tablename__ = "enrollments"
    enrollment_id: Mapped[int] = mapped_column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(sqlalchemy.Integer, nullable=False)
    course_id: Mapped[int] = mapped_column(sqlalchemy.Integer, nullable=False)
    grade: Mapped[str] = mapped_column(sqlalchemy.CHAR(1), nullable=True)
