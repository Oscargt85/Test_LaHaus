"""empty message

Revision ID: 98258071123a
Revises: 
Create Date: 2022-04-04 20:29:52.848217

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98258071123a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('money', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clients')
    # ### end Alembic commands ###
