"""create users table.

Revision ID: beca6288fd5d
Revises:
Create Date: 2021-06-29 01:02:16.653212

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'beca6288fd5d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, nullable=False),
        sa.Column('avatar', sa.Text, nullable=True),
        sa.Column('username', sa.Unicode(100), nullable=False),
        sa.Column('fullname', sa.Unicode(255), nullable=False),
        sa.Column('email', sa.Unicode(255), nullable=False),
        sa.Column('password', sa.LargeBinary, nullable=True),
        sa.Column('valid', sa.Boolean, nullable=True),
    )

def downgrade():
    op.drop_table('users')
