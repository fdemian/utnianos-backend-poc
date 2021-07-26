"""Add course year.

Revision ID: edea39c1a837
Revises: 8804ed4dfb00
Create Date: 2021-07-26 02:35:38.767405

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'edea39c1a837'
down_revision = '8804ed4dfb00'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('courses',
    sa.Column('year',
        sa.Integer,
        nullable=False,
        server_default="1")
    )

def downgrade():
   op.drop_column('courses', 'year')
