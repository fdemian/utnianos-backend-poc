"""Career progress tracker tables and columns

Revision ID: 12be49cac84b
Revises: 37e6d71d08ba
Create Date: 2021-07-18 14:02:41.781124

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12be49cac84b'
down_revision = '37e6d71d08ba'
branch_labels = None
depends_on = None

def upgrade():

    op.create_table(
      'completion_status',
      sa.Column('id', sa.Integer, primary_key=True, nullable=False),
      sa.Column('name', sa.Unicode(255), nullable=False)
    )

    op.create_table(
      'areas',
      sa.Column('id', sa.Integer, primary_key=True, nullable=False),
      sa.Column('name', sa.Unicode(255), nullable=False)
    )

    op.create_table(
      'departments',
      sa.Column('id', sa.Integer, primary_key=True, nullable=False),
      sa.Column('name', sa.Unicode(255), nullable=False)
    )

    op.create_table(
      'career_plan',
      sa.Column('id', sa.Integer, primary_key=True, nullable=False),
      sa.Column('name', sa.Unicode(255), nullable=False)
    )

    op.create_table(
     'course_status',
     sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id')),
     sa.Column('status_id', sa.Integer, sa.ForeignKey('completion_status.id'))
    )

    # Career plan column on user.
    op.add_column('users', sa.Column('career_plan_id', sa.Integer, sa.ForeignKey('career_plan.id'), nullable=True))

    # Courses columns.
    op.add_column('courses', sa.Column('code', sa.Unicode(255), nullable=False, server_default=""))
    op.add_column('courses', sa.Column('lecture_time', sa.Unicode(255), nullable=False, server_default=""))
    op.add_column('courses', sa.Column('orientation', sa.Unicode(255), nullable=False, server_default=""))
    op.add_column('courses', sa.Column('link_to_doc', sa.Unicode(255), nullable=False, server_default=""))
    op.add_column('courses', sa.Column('area_id', sa.Integer, sa.ForeignKey('areas.id')))
    op.add_column('courses', sa.Column('department_id', sa.Integer, sa.ForeignKey('departments.id')))


def downgrade():

    # Drop all added columns
    op.drop_column('users', 'career_plan_id')
    op.drop_column('courses', 'code')
    op.drop_column('courses', 'lecture_time')
    op.drop_column('courses', 'orientation')
    op.drop_column('courses', 'link_to_doc')
    op.drop_column('courses', 'area_id')
    op.drop_column('courses', 'department_id')

    # Drop newly created tables.
    op.drop_table('course_status')
    op.drop_table('completion_status')
    op.drop_table('areas')
    op.drop_table('deparments')
    op.drop_table('career_plan')
