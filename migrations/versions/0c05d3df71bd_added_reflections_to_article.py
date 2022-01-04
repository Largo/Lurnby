"""added reflections to article

Revision ID: 0c05d3df71bd
Revises: 12f7ab99d9d2
Create Date: 2022-01-04 18:39:55.804465

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0c05d3df71bd'
down_revision = '12f7ab99d9d2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('reflections', sa.Text(), nullable=True))


    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.DATETIME(),
               type_=sa.Date(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('message', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('reflections')

    # ### end Alembic commands ###
