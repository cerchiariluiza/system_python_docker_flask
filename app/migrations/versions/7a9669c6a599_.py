"""empty message

Revision ID: 7a9669c6a599
Revises: 
Create Date: 2021-01-15 09:39:46.512509

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7a9669c6a599'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produtos', sa.Column('segmento', sa.String(length=125), nullable=True))
    op.alter_column('produtos', 'nome',
               existing_type=mysql.VARCHAR(length=125),
               nullable=True)
    op.drop_column('produtos', 'tipo')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('produtos', sa.Column('tipo', mysql.VARCHAR(length=125), nullable=True))
    op.alter_column('produtos', 'nome',
               existing_type=mysql.VARCHAR(length=125),
               nullable=False)
    op.drop_column('produtos', 'segmento')
    # ### end Alembic commands ###