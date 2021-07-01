"""Add user lockout and salt.

Revision ID: 69cc07327cb9
Revises: beca6288fd5d
Create Date: 2021-06-30 15:39:25.532097

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '69cc07327cb9'
down_revision = 'beca6288fd5d'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('users', sa.Column('failed_attempts', sa.Integer, nullable=False, server_default='0'))
    op.add_column('users', sa.Column('lockout_time', sa.DateTime, nullable=True, server_default=None))
    op.add_column('users', sa.Column('salt', sa.LargeBinary, nullable=True, server_default=None))

def downgrade():
    op.drop_column('users', 'failed_attempts')
    op.drop_column('users', 'lockout_time')
    op.drop_column('users', 'salt')
