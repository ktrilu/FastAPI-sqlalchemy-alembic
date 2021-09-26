"""init

Revision ID: 3b39ef9245ad
Revises: 
Create Date: 2021-09-25 16:54:10.393551

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.sql.traversals import COMPARE_FAILED


# revision identifiers, used by Alembic.
revision = '3b39ef9245ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():

    op.create_table(
        'Productos',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=True),
        sa.Column('description', sa.String, nullable=True),
    )


def downgrade():
    op.drop_table('Productos')
