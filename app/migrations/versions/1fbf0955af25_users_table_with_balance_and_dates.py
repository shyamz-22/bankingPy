"""users table with balance and dates

Revision ID: 1fbf0955af25
Revises: 29c370c4b39a
Create Date: 2018-11-09 11:11:15.668651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fbf0955af25'
down_revision = '29c370c4b39a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('balance', sa.Numeric(precision=2), nullable=True))
    op.add_column('user', sa.Column('created_date', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('updated_date', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'updated_date')
    op.drop_column('user', 'created_date')
    op.drop_column('user', 'balance')
    # ### end Alembic commands ###
