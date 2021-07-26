"""Add courses/ career plans asociations table.

Revision ID: 8804ed4dfb00
Revises: 12be49cac84b
Create Date: 2021-07-26 02:07:50.508249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8804ed4dfb00'
down_revision = '12be49cac84b'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
      'career_plan_courses',
      sa.Column('career_plan_id', sa.Integer, sa.ForeignKey('career_plans.id')),
      sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id'))
    )
    op.create_table(
      'courses_status',
      sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id')),
      sa.Column('completion_id', sa.Integer, sa.ForeignKey('completion_status.id'))
    )

def downgrade():
    op.drop_table('career_plan_courses')
    op.create_table('courses_status')
