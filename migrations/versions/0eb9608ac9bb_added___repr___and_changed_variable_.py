"""added __repr__ and changed variable names

Revision ID: 0eb9608ac9bb
Revises: 
Create Date: 2023-04-08 12:12:40.570628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0eb9608ac9bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('deck', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=100), nullable=True))
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.create_unique_constraint(None, ['name'])
        batch_op.create_foreign_key(None, 'user', ['user_id'], ['id'])
        batch_op.drop_column('date')
        batch_op.drop_column('data')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('deck', schema=None) as batch_op:
        batch_op.add_column(sa.Column('data', sa.VARCHAR(length=1000), nullable=True))
        batch_op.add_column(sa.Column('date', sa.DATETIME(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('user_id')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
