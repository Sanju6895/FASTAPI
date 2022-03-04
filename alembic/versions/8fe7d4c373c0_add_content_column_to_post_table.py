"""Add Content column to post table

Revision ID: 8fe7d4c373c0
Revises: 630a5ad977c2
Create Date: 2022-03-04 10:35:55.098200

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8fe7d4c373c0'
down_revision = '630a5ad977c2'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass

def downgrade():
    op.drop_column('posts','content')
    pass
