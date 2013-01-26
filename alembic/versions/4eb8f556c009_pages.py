"""pages

Revision ID: 4eb8f556c009
Revises: 29231a1e6948
Create Date: 2013-01-26 08:58:16.624929

"""

# revision identifiers, used by Alembic.
revision = '4eb8f556c009'
down_revision = '29231a1e6948'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'page',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('slug', sa.String(80), unique=True),
        sa.Column('content', sa.Text()),
        sa.Column('title', sa.String(140)),
        sa.Column('draft', sa.Boolean(), default=True)
    )


def downgrade():
    op.drop_table('page')
