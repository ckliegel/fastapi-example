"""create posts table

Revision ID: 18be1393b66e
Revises: 
Create Date: 2022-06-29 21:07:40.993603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18be1393b66e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True)
    , sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
