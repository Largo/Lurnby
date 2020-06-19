"""added goals to tags

Revision ID: 3781f53962d3
Revises: 294aec5ede40
Create Date: 2020-06-17 13:19:23.563936

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3781f53962d3'
down_revision = '294aec5ede40'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('goal', sa.String(length=512), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.drop_column('goal')

    # ### end Alembic commands ###