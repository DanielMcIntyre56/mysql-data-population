#!/usr/bin/env python3

"""
This script populates the students, courses, instructors,
and enrollments tables with random fake data.
"""

import random

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Students, Courses, Instructors, Enrollments

sql_engine = create_engine("mysql+pymysql://root@localhost/uni")
session = Session(bind=sql_engine)

faker = Faker()

print("Adding 10 instructors")
instructors = []
for _ in range(10):
    instructor = Instructors(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        department=random.choice(["Maths", "Physics", "Computer-Science", "History", "Biology"])
    )
    instructors.append(instructor)
session.add_all(instructors)
session.commit()

print("Adding 20 courses")
courses = []
for _ in range(20):
    course = Courses(
        course_name=faker.catch_phrase(),
        credits=random.randint(1, 10),
        instructor_id=random.choice(instructors).instructor_id
    )
    courses.append(course)
session.add_all(courses)
session.commit()

print("Adding 100 students")
students = []
for _ in range(100):
    student = Students(
        first_name=faker.first_name(),
        last_name=faker.last_name(),
        enrollment_date=faker.date_between(start_date='-4y', end_date='today')
    )
    students.append(student)
session.add_all(students)
session.commit()

print("Adding 200 enrollments")
enrollments = []
for _ in range(200):
    enrollment = Enrollments(
        student_id=random.choice(students).student_id,
        course_id=random.choice(courses).course_id,
        grade=random.choice(["A", "B", "C", "D", "F"])
    )
    enrollments.append(enrollment)
session.add_all(enrollments)
session.commit()

session.close()
print("Tables populated with random data")
