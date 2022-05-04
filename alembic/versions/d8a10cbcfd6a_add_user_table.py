"""add user table

Revision ID: d8a10cbcfd6a
Revises: f417e1921d4f
Create Date: 2022-05-04 19:38:19.178804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd8a10cbcfd6a'
down_revision = 'f417e1921d4f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',sa.Column('id',sa.Integer(),nullable = False), sa.Column('email', sa.String(), nullable = False), sa.Column('password', sa.String(), nullable=False), sa.Column('created_at',sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'),nullable=False),sa.PrimaryKeyConstraint('id'),sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass
