"""
Initial migration

Revision ID: 1b7b0390244b
Revises: 
Create Date: 2025-04-18 11:06:41.166008

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1b7b0390244b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('courses',
    sa.Column('course_id', sa.SMALLINT(), autoincrement=True, nullable=False),
    sa.Column('course_name', sa.VARCHAR(length=100), nullable=False),
    sa.Column('credits', sa.SMALLINT(), nullable=False),
    sa.Column('instructor_id', sa.SMALLINT(), nullable=False),
    sa.PrimaryKeyConstraint('course_id')
    )

    op.create_table('enrollments',
    sa.Column('enrollment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('student_id', sa.Integer(), nullable=False),
    sa.Column('course_id', sa.Integer(), nullable=False),
    sa.Column('grade', sa.CHAR(length=1), nullable=True),
    sa.PrimaryKeyConstraint('enrollment_id')
    )

    op.create_table('instructors',
    sa.Column('instructor_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=False),
    sa.Column('last_name', sa.String(length=50), nullable=False),
    sa.Column('department', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('instructor_id')
    )

    op.create_table('students',
    sa.Column('student_id', sa.SMALLINT(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=50), nullable=False),
    sa.Column('enrollment_date', sa.DATE(), nullable=False),
    sa.PrimaryKeyConstraint('student_id')
    )


def downgrade() -> None:
    op.drop_table('students')
    op.drop_table('instructors')
    op.drop_table('enrollments')
    op.drop_table('courses')
