"""empty message

Revision ID: 030e26393cc3
Revises: 60109a6eae5d
Create Date: 2020-08-22 14:59:38.970973

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '030e26393cc3'
down_revision = '60109a6eae5d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ORDERITEM', 'pid',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('ORDERITEM', 'pid',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###