"""Insert data on contribution tables.

Revision ID: d9faf0b21d6e
Revises: b43e94610448
Create Date: 2021-07-11 15:28:27.006477

"""
from alembic import op
from os import path
from sqlalchemy.sql import table, column
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'd9faf0b21d6e'
down_revision = 'b43e94610448'
branch_labels = None
depends_on = None

def upgrade():
   contrib_table = table('contrib_types',column('name', sa.String))
   op.bulk_insert(contrib_table,
     [
       {'name': 'Parcial'},
       {'name': 'Final'},
       {'name': 'Trabajo Práctico'},
       {'name': 'Apunte/Guia'},
       {'name': 'Libro'},
       {'name': 'Profesores'},
       {'name': 'Ejercicios'},
       {'name': 'Dudas y recomendaciones'},
       {'name': 'Consultas administratias'},
       {'name': 'Otro'},
       {'name': 'Guias CEIT'},
     ]
    )

def downgrade():
    op.execute("DELETE FROM materials_types;")
    op.execute("DELETE FROM contrib_types;")
