"""add content column to posts table

Revision ID: f417e1921d4f
Revises: 4c6e25ce2c82
Create Date: 2022-05-04 19:34:06.810846

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f417e1921d4f'
down_revision = '4c6e25ce2c82'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
