"""Completion status code.

Revision ID: 4fcc053db5cb
Revises: b4a95ca17b0e
Create Date: 2021-08-23 21:22:19.083357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4fcc053db5cb'
down_revision = 'b4a95ca17b0e'
branch_labels = None
depends_on = None


def upgrade():

    op.add_column('completion_status',
     sa.Column('status',
       sa.Unicode(255),
       nullable=False,
       server_default=""
     )
    )
    op.execute("UPDATE completion_status SET status = 'P' WHERE name = 'Pendiente';")
    op.execute("UPDATE completion_status SET status = 'E' WHERE name = 'Cursando';")
    op.execute("UPDATE completion_status SET status = 'C' WHERE name = 'Firmada';")
    op.execute("UPDATE completion_status SET status = 'F' WHERE name = 'Aprobada';")

    op.drop_column('courses_status', 'completion_id')
    op.drop_column('course_prerrequisites', 'completion_id')

    op.drop_constraint('course_status_status_id_fkey', 'course_status')
    op.drop_column('completion_status', 'id')
    op.create_primary_key('pk_completion_status', 'completion_status', ['status'])

    op.add_column('courses_status',
      sa.Column('completion_code',
         sa.Unicode(255),
         sa.ForeignKey("completion_status.status"),
         nullable=False,
         server_default="P"
      )
    )

    op.add_column('course_prerrequisites',
      sa.Column('completion_code',
         sa.Unicode(255),
         sa.ForeignKey("completion_status.status"),
         nullable=False,
         server_default="P"
      )
    )


def downgrade():

    op.drop_column('completion_status', 'status')
    op.add_column('completion_status',
      sa.Column('id',
        sa.Integer,
        primary_key=True
      )
    )
    op.create_primary_key('pk_completion_id', 'completion_status', ['id'])

    op.drop_column('courses_status', 'completion_code')
    op.add_column('courses_status',
     sa.Column('completion_id',
        sa.Integer,
        sa.ForeignKey("completion_status.id"),
        nullable=False
     )
    )

    op.drop_column('course_prerrequisites', 'completion_code')
    op.add_column('course_prerrequisites',
     sa.Column('completion_id',
        sa.Integer,
        sa.ForeignKey("completion_status.id"),
        nullable=False
     )
    )
