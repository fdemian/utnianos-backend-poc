"""Course completion status data.

Revision ID: 369cda1e60b2
Revises: 79c45a21882d
Create Date: 2021-07-30 12:12:40.587118

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = '369cda1e60b2'
down_revision = '79c45a21882d'
branch_labels = None
depends_on = None


def upgrade():
     contrib_table = table('completion_status',column('name', sa.String))
     op.bulk_insert(contrib_table,
       [
         {'name': 'Pendiente'},
         {'name': 'Cursando'},
         {'name': 'Firmada'},
         {'name': 'Aprobada'}
       ]
      )


def downgrade():
    op.execute("DELETE FROM completion_status;")
