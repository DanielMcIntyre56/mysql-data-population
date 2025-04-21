"""
Add course_costs table

Revision ID: bcd4080bbe2e
Revises: 1b7b0390244b
Create Date: 2025-04-21 13:22:24.200450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bcd4080bbe2e'
down_revision: Union[str, None] = '1b7b0390244b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('course_costs',
    sa.Column('cost_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('course_id', sa.SmallInteger(), nullable=False),
    sa.Column('cost_per_credit', sa.DECIMAL(precision=8, scale=2), nullable=False),
    sa.Column('currency', sa.CHAR(length=3), nullable=False),
    sa.Column('effective_date', sa.DATE(), nullable=False),
    sa.ForeignKeyConstraint(['course_id'], ['courses.course_id'], ),
    sa.PrimaryKeyConstraint('cost_id')
    )


def downgrade() -> None:
    op.drop_table('course_costs')
