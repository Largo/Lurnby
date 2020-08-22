"""added account_created_date to user model

Revision ID: 919bd7d1a777
Revises: 91c7ada4b1c0
Create Date: 2020-06-28 11:38:54.331548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '919bd7d1a777'
down_revision = '91c7ada4b1c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.add_column(sa.Column('highlightedText', sa.String(), nullable=True))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_created_date', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('account_created_date')

    with op.batch_alter_table('article', schema=None) as batch_op:
        batch_op.drop_column('highlightedText')

    # ### end Alembic commands ###