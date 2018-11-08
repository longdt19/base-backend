"""create user table

Revision ID: 001
Revises: 
Create Date: 2018-11-08 16:28:50.985872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.String, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(200)),
    )

def downgrade():
    op.drop_table('account')
