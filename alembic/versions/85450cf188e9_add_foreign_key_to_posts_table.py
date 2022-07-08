"""add foreign-key to posts table

Revision ID: 85450cf188e9
Revises: 1113f35870d8
Create Date: 2022-06-29 22:03:54.221705

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85450cf188e9'
down_revision = '1113f35870d8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('posts_users_fk', source_table="posts", referent_table="users", local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
