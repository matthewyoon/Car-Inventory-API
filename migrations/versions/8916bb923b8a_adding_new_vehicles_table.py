"""Adding New Vehicles Table

Revision ID: 8916bb923b8a
Revises: 4f162f0bf728
Create Date: 2021-04-14 21:51:56.054821

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8916bb923b8a'
down_revision = '4f162f0bf728'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicle',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('vehicle_type', sa.String(length=100), nullable=True),
    sa.Column('make', sa.String(length=100), nullable=True),
    sa.Column('model', sa.String(length=100), nullable=True),
    sa.Column('year', sa.Numeric(precision=4, scale=0), nullable=True),
    sa.Column('color', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Numeric(precision=9, scale=2), nullable=True),
    sa.Column('engine', sa.String(length=100), nullable=True),
    sa.Column('fuel', sa.String(length=100), nullable=True),
    sa.Column('msrp', sa.Numeric(precision=9, scale=2), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicle')
    # ### end Alembic commands ###
