"""added last_used to topic model

Revision ID: 3edaed8395c0
Revises: cdddbf0edeb6
Create Date: 2021-09-18 12:35:31.915289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3edaed8395c0'
down_revision = 'cdddbf0edeb6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('topic', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_used', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('topic', schema=None) as batch_op:
        batch_op.drop_column('last_used')

    # ### end Alembic commands ###
