"""Purge inexistent table.

Revision ID: 550c530f6472
Revises: 4fcc053db5cb
Create Date: 2021-08-26 10:56:30.707809

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '550c530f6472'
down_revision = '4fcc053db5cb'
branch_labels = None
depends_on = None


def upgrade():
    op.drop_table('course_status')

def downgrade():
    op.create_table(
     'course_status',
     sa.Column('course_id', sa.Integer),
     sa.Column('status_id', sa.Integer)
    )
