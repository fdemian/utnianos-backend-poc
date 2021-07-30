"""Add user association column.

Revision ID: 79c45a21882d
Revises: edea39c1a837
Create Date: 2021-07-30 01:41:55.438921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79c45a21882d'
down_revision = 'edea39c1a837'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('courses_status', sa.Column('id', sa.Integer, primary_key=True, nullable=False)),
    op.add_column('courses_status', sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')))

def downgrade():
    op.drop_column('courses_status', 'user_id')
    op.drop_column('courses_status', 'id')    
