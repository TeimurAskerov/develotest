"""empty message

Revision ID: a3fe567b740f
Revises: 819d679d25f3
Create Date: 2019-04-29 12:56:32.719838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a3fe567b740f'
down_revision = '819d679d25f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('card', sa.Column('amount', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('card', 'amount')
    # ### end Alembic commands ###
