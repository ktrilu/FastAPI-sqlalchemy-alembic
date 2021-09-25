"""v2

Revision ID: 9c44cf4d7911
Revises: 9f0e8ca84ab3
Create Date: 2021-09-25 17:43:28.569037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c44cf4d7911'
down_revision = '3b39ef9245ad'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'Empresas',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, nullable=True)
    )


def downgrade():
    op.drop_table('Productos')
