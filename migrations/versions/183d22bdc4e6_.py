"""empty message

Revision ID: 183d22bdc4e6
Revises: c82b69608919
Create Date: 2020-06-22 12:20:28.711830

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '183d22bdc4e6'
down_revision = 'c82b69608919'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('article', sa.Column('archived', sa.Boolean(), nullable=True))
    op.add_column('article', sa.Column('source', sa.String(length=500), nullable=True))
    op.add_column('article', sa.Column('source_url', sa.String(length=500), nullable=True))
    op.create_index(op.f('ix_article_archived'), 'article', ['archived'], unique=False)
    op.drop_column('article', 'url')
    op.add_column('highlight', sa.Column('archived', sa.Boolean(), nullable=True))
    op.create_index(op.f('ix_highlight_archived'), 'highlight', ['archived'], unique=False)
    op.add_column('tag', sa.Column('goal', sa.String(length=512), nullable=True))
    op.drop_index('ix_topic_title', table_name='topic')
    op.create_index(op.f('ix_topic_title'), 'topic', ['title'], unique=True)
    op.add_column('user', sa.Column('firstname', sa.String(), nullable=True))
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_firstname'), 'user', ['firstname'], unique=False)
    op.create_index(op.f('ix_user_goog_id'), 'user', ['goog_id'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_goog_id'), table_name='user')
    op.drop_index(op.f('ix_user_firstname'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_column('user', 'firstname')
    op.drop_index(op.f('ix_topic_title'), table_name='topic')
    op.create_index('ix_topic_title', 'topic', ['title'], unique=False)
    op.drop_column('tag', 'goal')
    op.drop_index(op.f('ix_highlight_archived'), table_name='highlight')
    op.drop_column('highlight', 'archived')
    op.add_column('article', sa.Column('url', sa.VARCHAR(length=500), nullable=True))
    op.drop_index(op.f('ix_article_archived'), table_name='article')
    op.drop_column('article', 'source_url')
    op.drop_column('article', 'source')
    op.drop_column('article', 'archived')
    # ### end Alembic commands ###
