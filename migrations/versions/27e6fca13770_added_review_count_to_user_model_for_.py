"""added review count to user model for determining the number of highlights to show per tier

Revision ID: 27e6fca13770
Revises: 3edaed8395c0
Create Date: 2021-10-12 23:07:44.770245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27e6fca13770'
down_revision = '3edaed8395c0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('review_count', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('review_count')

    # ### end Alembic commands ###