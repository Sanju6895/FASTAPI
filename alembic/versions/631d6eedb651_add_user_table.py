"""Add User table

Revision ID: 631d6eedb651
Revises: 8fe7d4c373c0
Create Date: 2022-03-04 10:59:30.487585

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '631d6eedb651'
down_revision = '8fe7d4c373c0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
