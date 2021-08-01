"""Add course prerrequisites table.

Revision ID: 004a8271477c
Revises: 369cda1e60b2
Create Date: 2021-07-31 12:54:09.611575

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '004a8271477c'
down_revision = '369cda1e60b2'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
      'course_prerrequisites',
      sa.Column('id', sa.Integer, primary_key=True, nullable=False),
      sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id')),
      sa.Column('prerrequisite_id', sa.Integer, sa.ForeignKey('courses.id')),
      sa.Column('type', sa.String(1), nullable=False),
      sa.Column('completion_id', sa.Integer, sa.ForeignKey('completion_status.id'))
    )

def downgrade():
    op.drop_table('course_prerrequisites')
