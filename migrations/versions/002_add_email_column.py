"""add email column

Revision ID: 002
Revises: 001
Create Date: 2018-11-08 16:39:57.117605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002'
down_revision = '001'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('account', sa.Column('email', sa.String(50)))


def downgrade():
    op.drop_column('account', 'email')
