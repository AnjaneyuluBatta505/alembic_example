"""create user table

Revision ID: 433af9f41996
Revises: 
Create Date: 2021-11-20 19:17:01.434529

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '433af9f41996'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )


def downgrade():
    op.drop_table('account')
