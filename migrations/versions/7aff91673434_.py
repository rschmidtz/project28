"""empty message

Revision ID: 7aff91673434
Revises: None
Create Date: 2016-10-10 18:56:32.351026

"""

# revision identifiers, used by Alembic.
revision = '7aff91673434'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('email', sa.String(length=40), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    ### end Alembic commands ###
