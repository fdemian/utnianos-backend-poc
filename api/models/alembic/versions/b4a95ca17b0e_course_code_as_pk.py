"""Course code as PK

Revision ID: b4a95ca17b0e
Revises: 9528b55d0572
Create Date: 2021-08-20 20:13:05.664554

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'b4a95ca17b0e'
down_revision = '9528b55d0572'
branch_labels = None
depends_on = None


def upgrade():

    # Drop and recreate all columns without non-null constraints.
    op.create_unique_constraint('courses_code_unique',
     'courses',
     ['code']
    )

    op.drop_constraint('class_materials_course_id_fkey', 'class_materials')
    op.drop_constraint('course_status_course_id_fkey', 'course_status')
    op.drop_constraint('course_prerrequisites_course_id_fkey', 'course_prerrequisites')

    op.drop_column('courses_status', 'course_id')
    op.drop_column('course_prerrequisites', 'prerrequisite_id')
    op.drop_column('course_prerrequisites', 'course_id')
    op.drop_column('career_plan_courses', 'career_plan_id')
    #op.drop_column('career_plan_courses', 'course_id')
    op.drop_column('class_materials', 'course_id')

    # Courses status.
    op.add_column('courses_status',
      sa.Column('course_code',
        sa.Unicode(255),
        sa.ForeignKey('courses.code'),
        nullable=False
      )
    )

    # Courses prerrequisites.

    op.add_column('course_prerrequisites',
      sa.Column('prerrequisite_code',
       sa.Unicode(255),
       sa.ForeignKey('courses.code'),
       nullable=False
      )
    )

    op.add_column('course_prerrequisites',
     sa.Column('course_code',
       sa.Unicode(255),
       sa.ForeignKey('courses.code'),
       nullable=False
     )
    )


    op.add_column('career_plan_courses',
      sa.Column('course_code',
        sa.Unicode(255),
        sa.ForeignKey('courses.code'),
        nullable=False
      )
    )

    # Class materials.
    op.add_column('class_materials',
      sa.Column('course_code',
       sa.Unicode(255),
       sa.ForeignKey('courses.code'),
       nullable=False
      )
    )

    # Drops for courses.
    op.drop_column('courses', 'id')
    op.drop_column('courses', 'lecture_time')
    op.drop_column('courses', 'orientation')
    op.drop_column('courses', 'link_to_doc')

    op.add_column('courses', sa.Column('lecture_time', sa.Unicode(255), nullable=True))
    op.add_column('courses', sa.Column('orientation', sa.Unicode(255), nullable=True))
    op.add_column('courses', sa.Column('link_to_doc', sa.Unicode(255), nullable=True))

def downgrade():

    # Drop constraint on cascade.
    op.execute('ALTER TABLE courses DROP CONSTRAINT courses_code_unique CASCADE;');

    op.drop_column('courses', 'lecture_time')
    op.drop_column('courses', 'orientation')
    op.drop_column('courses', 'link_to_doc')

    op.add_column('courses', sa.Column('lecture_time', sa.Unicode(255), nullable=False))
    op.add_column('courses', sa.Column('orientation', sa.Unicode(255), nullable=False))
    op.add_column('courses', sa.Column('link_to_doc', sa.Unicode(255), nullable=False))
    op.add_column('courses',
        sa.Column('id',
          sa.Integer,
          primary_key=True,
          nullable=False
        )
    )
    op.create_primary_key('pk_courses', 'courses', ['id'])

    # Class materials.
    op.drop_column('class_materials', 'course_code')
    op.add_column('class_materials',
       sa.Column('course_id',
        sa.Integer,
        sa.ForeignKey('courses.id'),
        nullable=False
      )
    )

    # Courses status.
    op.drop_column('courses_status', 'course_code')
    op.add_column('courses_status',
      sa.Column('course_id',
       sa.Integer,
       sa.ForeignKey('courses.id'),
       nullable=False
      )
    )

    # Courses prerrequisites.
    op.drop_column('course_prerrequisites', 'prerrequisite_code')
    op.add_column('course_prerrequisites',
      sa.Column('prerrequisite_id',
       sa.Integer,
       sa.ForeignKey('courses.id'),
       nullable=False
      )
    )

    op.drop_column('course_prerrequisites', 'course_code')
    op.add_column('course_prerrequisites',
     sa.Column('course_id',
       sa.Integer,
       sa.ForeignKey('courses.id'),
       nullable=False
     )
    )

    op.drop_column('users', 'career_plan_code')
    op.drop_column('career_plan_courses', 'career_plan_code')
    op.drop_column('career_plan_courses', 'course_code')
    op.drop_column('career_plans', 'code')

    op.add_column('career_plans',
      sa.Column('id',
        sa.Integer,
        primary_key=True,
        nullable=False
      )
    )
    op.create_primary_key('pk_career_plans', 'career_plans', ['id'])

    op.add_column('users', sa.Column('career_plan_id',
       sa.Integer,
       sa.ForeignKey('career_plans.id')
     )
    )

    op.add_column('career_plan_courses',
       sa.Column('course_id',
        sa.Integer,
        sa.ForeignKey('courses.id')
       )
    )

    op.add_column('career_plan_courses',
     sa.Column('career_plan_id',
      sa.Integer,
      sa.ForeignKey('career_plans.id'),
      nullable=False
     )
    )

    # Drop.
    op.drop_column('courses', 'lecture_time')
    op.drop_column('courses', 'orientation')
    op.drop_column('courses', 'link_to_doc')

    op.add_column('courses', sa.Column('lecture_time', sa.Unicode(255), nullable=False, server_default=""))
    op.add_column('courses', sa.Column('orientation', sa.Unicode(255), nullable=False, server_default=""))
    op.add_column('courses', sa.Column('link_to_doc', sa.Unicode(255), nullable=False, server_default=""))
