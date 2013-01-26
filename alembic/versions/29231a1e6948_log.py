"""log

Revision ID: 29231a1e6948
Revises: 55b694e505ee
Create Date: 2013-01-25 22:27:09.067509

"""

# revision identifiers, used by Alembic.
revision = '29231a1e6948'
down_revision = '55b694e505ee'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('experiment',
        sa.Column('status', sa.String(80))
    )


def downgrade():
    op.drop_column('experiment', 'status')
