#!/usr/bin/env python3

import random
import argparse
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Students, Courses, Instructors, Enrollments, CourseCosts

sql_engine = create_engine("mysql+pymysql://root@localhost/uni")
session = Session(bind=sql_engine)

faker = Faker()


def add_instructors():
    print("Adding 10 instructors")
    instructors = []

    for _ in range(10):
        instructor = Instructors(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            department=random.choice(["Maths", "Physics", "Computer-Science", "History", "Biology"]),
        )
        instructors.append(instructor)

    session.add_all(instructors)
    session.commit()


def add_courses():
    print("Adding 20 courses")
    instructors = session.query(Instructors).all()
    courses = []

    for _ in range(20):
        course = Courses(
            course_name=faker.catch_phrase(),
            credits=random.randint(1, 10),
            instructor_id=random.choice(instructors).instructor_id,
        )
        courses.append(course)

    session.add_all(courses)
    session.commit()


def add_students():
    print("Adding 100 students")
    students = []

    for _ in range(100):
        student = Students(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            enrollment_date=faker.date_between(start_date='-4y', end_date='today'),
        )
        students.append(student)

    session.add_all(students)
    session.commit()


def add_enrollments():
    print("Adding 200 enrollments")
    students = session.query(Students).all()
    courses = session.query(Courses).all()
    enrollments = []

    for _ in range(200):
        enrollment = Enrollments(
            student_id=random.choice(students).student_id,
            course_id=random.choice(courses).course_id,
            grade=random.choice(["A", "B", "C", "D", "F"]),
        )
        enrollments.append(enrollment)

    session.add_all(enrollments)
    session.commit()


def add_course_costs():
    print("Adding 20 course costs")
    courses = session.query(Courses).all()
    course_costs = []

    for _ in range(20):
        course_cost = CourseCosts(
            course_id=random.choice(courses).course_id,
            cost_per_credit=random.uniform(100.00, 500.00),
            currency=random.choice(["USD", "GBP", "EUR"]),
            effective_date=faker.date_between(start_date='-4y', end_date='today'),
        )
        course_costs.append(course_cost)

    session.add_all(course_costs)
    session.commit()


def main():
    parser = argparse.ArgumentParser(description="Populate the database with fake data.")
    parser.add_argument('-i', '--instructors', action='store_true', help="Add instructors data")
    parser.add_argument('-c', '--courses', action='store_true', help="Add courses data")
    parser.add_argument('-s', '--students', action='store_true', help="Add students data")
    parser.add_argument('-e', '--enrollments', action='store_true', help="Add enrollments data")
    parser.add_argument('-cc', '--course_costs', action='store_true', help="Add course costs data")

    args = parser.parse_args()

    if args.instructors:
        add_instructors()
    if args.courses:
        add_courses()
    if args.students:
        add_students()
    if args.enrollments:
        add_enrollments()
    if args.course_costs:
        add_course_costs()

    if not any([args.instructors, args.courses, args.students, args.enrollments, args.course_costs]):
        add_instructors()
        add_courses()
        add_students()
        add_enrollments()
        add_course_costs()

    session.close()
    print("Tables populated with random data")

if __name__ == "__main__":
    main()
