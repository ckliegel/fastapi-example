"""add content column to posts table

Revision ID: d6d2da69e8b2
Revises: 18be1393b66e
Create Date: 2022-06-29 21:41:38.347918

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6d2da69e8b2'
down_revision = '18be1393b66e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
