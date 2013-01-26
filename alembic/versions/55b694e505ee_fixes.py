"""fixes

Revision ID: 55b694e505ee
Revises: 3a8fb80b1740
Create Date: 2013-01-25 22:01:22.619692

"""

# revision identifiers, used by Alembic.
revision = '55b694e505ee'
down_revision = '3a8fb80b1740'

from alembic import op
import sqlalchemy as sa


def upgrade():

    op.drop_column('expression', 'graduated')

    op.add_column('experiment',
        sa.Column('graduated', sa.String(280))
    )



def downgrade():

    op.drop_column('experiment', 'graduated')

    op.add_column('expression',
        sa.Column('graduated', sa.String(280))
    )
