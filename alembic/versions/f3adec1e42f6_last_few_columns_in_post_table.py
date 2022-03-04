"""Last few columns in post table

Revision ID: f3adec1e42f6
Revises: f4ba28859d28
Create Date: 2022-03-04 11:27:59.658864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3adec1e42f6'
down_revision = 'f4ba28859d28'
branch_labels = None
depends_on = None

def upgrade():
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass