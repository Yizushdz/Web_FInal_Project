""" took away answer and question 

Revision ID: 6bdc8e647116
Revises: fa10c6a931ec
Create Date: 2023-04-13 10:52:45.202069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bdc8e647116'
down_revision = 'fa10c6a931ec'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=10000), nullable=True))
        batch_op.drop_column('answer')
        batch_op.drop_column('question')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('flashcard', schema=None) as batch_op:
        batch_op.add_column(sa.Column('question', sa.VARCHAR(length=10000), nullable=True))
        batch_op.add_column(sa.Column('answer', sa.VARCHAR(length=10000), nullable=True))
        batch_op.drop_column('name')

    # ### end Alembic commands ###
