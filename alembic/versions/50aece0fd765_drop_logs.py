"""drop logs

Revision ID: 50aece0fd765
Revises: 4eb8f556c009
Create Date: 2013-01-26 11:28:43.514072

"""

# revision identifiers, used by Alembic.
revision = '50aece0fd765'
down_revision = '4eb8f556c009'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_column('experiment', 'log')




def downgrade():
    op.add_column('experiment',
        sa.Column('log', sa.Text())
    )
