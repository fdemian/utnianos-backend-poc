"""Add description column to class materials.

Revision ID: 37e6d71d08ba
Revises: d9faf0b21d6e
Create Date: 2021-07-18 12:41:42.842215

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37e6d71d08ba'
down_revision = 'd9faf0b21d6e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('class_materials', sa.Column('description', sa.Text, nullable=False, server_default=""))


def downgrade():
    op.drop_column('class_materials', 'description')
