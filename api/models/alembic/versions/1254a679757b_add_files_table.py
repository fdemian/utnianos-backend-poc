"""Add files table.

Revision ID: 1254a679757b
Revises: 004a8271477c
Create Date: 2021-08-14 14:32:54.417828

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1254a679757b'
down_revision = '004a8271477c'
branch_labels = None
depends_on = None

def upgrade():
    op.drop_column('class_materials', 'file_path')
    op.create_table(
      'files',
      sa.Column('id', sa.Integer, primary_key=True, nullable=False),
      sa.Column('path', sa.Unicode(255), nullable=False),
      sa.Column('type', sa.Unicode(255), nullable=False),
      sa.Column('class_material_id', sa.Integer, sa.ForeignKey('class_materials.id'))
    )

def downgrade():
    op.add_column('class_materials', sa.Column('file_path', sa.Text, nullable=True))
    op.drop_table('files')
