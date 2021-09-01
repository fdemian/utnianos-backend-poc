"""Add career plan codes.

Revision ID: 9528b55d0572
Revises: 1254a679757b
Create Date: 2021-08-20 11:31:45.012764

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '9528b55d0572'
down_revision = '1254a679757b'
branch_labels = None
depends_on = None

def upgrade():

    # Drop columns and constraints.
    op.drop_column('career_plan_courses', 'course_id')
    op.drop_column('users', 'career_plan_id')
    op.drop_constraint('career_plan_courses_career_plan_id_fkey', 'career_plan_courses')
    op.drop_column('career_plans', 'id', ondelete='CASCADE')

    # Add new columns and constraints.
    op.add_column('career_plans',
        sa.Column('code',
            sa.Unicode(255),
            nullable=False,
            server_default='-X',
            primary_key=True
        )
    )
    op.create_unique_constraint('plans_unique_code', 'career_plans', ['code'])
    op.add_column('users', sa.Column('career_plan_code',
       sa.Unicode(255),
       sa.ForeignKey('career_plans.code'),
       nullable=True)
    )
    op.add_column('career_plan_courses',
       sa.Column('career_plan_code',
         sa.Unicode(255),
         sa.ForeignKey('career_plans.code'),
         nullable=False
       )
    )

def downgrade():
    op.create_unique_constraint('career_plan_courses_career_plan_id_fkey', 'career_plans', ['id'])
