"""account created data and tags_articles table

Revision ID: 70bcbe039951
Revises: 4103eb54fb5f
Create Date: 2020-06-29 16:33:30.131183

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70bcbe039951'
down_revision = '4103eb54fb5f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags_articles',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['article.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags_articles')
    # ### end Alembic commands ###
