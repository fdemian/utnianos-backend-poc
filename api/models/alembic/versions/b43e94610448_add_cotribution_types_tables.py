"""Add cotribution types tables.

Revision ID: b43e94610448
Revises: 69cc07327cb9
Create Date: 2021-07-11 13:52:34.223833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b43e94610448'
down_revision = '69cc07327cb9'
branch_labels = None
depends_on = None


def upgrade():
    # Materias
    op.create_table(
       'courses',
       sa.Column('id', sa.Integer, primary_key=True, nullable=False),
       sa.Column('name', sa.Unicode(255), nullable=False)
    )

    op.create_table(
       'contrib_types',
       sa.Column('id', sa.Integer, primary_key=True, nullable=False),
       sa.Column('name', sa.Unicode(255), nullable=False)
    )

    op.create_table(
       'class_materials',
       sa.Column('id', sa.Integer, primary_key=True, nullable=False),
       sa.Column('name', sa.Unicode(255), nullable=False),
       sa.Column('file_path', sa.Text, nullable=True),
       sa.Column('course_id', sa.Integer, sa.ForeignKey('courses.id')),
       sa.Column('contrib_types', sa.Text, nullable=False)
    )

    # Association table (class materials / Contrib types)
    # For many-to-many relationship.
    op.create_table(
       'materials_types',
       sa.Column('class_materials_id', sa.Integer, sa.ForeignKey('class_materials.id')),
       sa.Column('contrib_types_id', sa.Integer, sa.ForeignKey('contrib_types.id'))
    )


def downgrade():
    op.drop_table('materials_types')
    op.drop_table('class_materials')
    op.drop_table('courses')
    op.drop_table('contrib_types')
