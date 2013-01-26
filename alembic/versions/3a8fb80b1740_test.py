"""test

Revision ID: 3a8fb80b1740
Revises: None
Create Date: 2013-01-25 21:49:48.900894

"""

# revision identifiers, used by Alembic.
revision = '3a8fb80b1740'
down_revision = None

from datetime import datetime

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'expression',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('slug', sa.String(80), unique=True),
        sa.Column('content', sa.Text()),
        sa.Column('title', sa.String(140)),
        sa.Column('link', sa.String(280)),
        sa.Column('draft', sa.Boolean(), default=True),
        sa.Column('style', sa.String(80)),
        sa.Column('graduated', sa.String(280)),
        sa.Column('meta', sa.dialects.postgresql.HSTORE()),
        sa.Column('created', sa.DateTime, default=datetime.now),
        sa.Column('updated', sa.DateTime, default=datetime.now)
    )

    op.create_table(
        'experiment',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('slug', sa.String(80), unique=True),
        sa.Column('content', sa.Text()),
        sa.Column('log', sa.Text()),
        sa.Column('title', sa.String(140)),
        sa.Column('link', sa.String(280)),
        sa.Column('draft', sa.Boolean(), default=True),
        sa.Column('style', sa.String(80)),
        sa.Column('meta', sa.dialects.postgresql.HSTORE()),
        sa.Column('created', sa.DateTime, default=datetime.now),
        sa.Column('updated', sa.DateTime, default=datetime.now)
    )

    op.create_table(
        'exposure',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('slug', sa.String(80), unique=True),
        sa.Column('content', sa.Text()),
        sa.Column('title', sa.String(140)),
        sa.Column('link', sa.String(280)),
        sa.Column('draft', sa.Boolean(), default=True),
        sa.Column('style', sa.String(80)),
        sa.Column('meta', sa.dialects.postgresql.HSTORE()),
        sa.Column('created', sa.DateTime, default=datetime.now),
        sa.Column('updated', sa.DateTime, default=datetime.now)
    )


def downgrade():
    op.drop_table('expression')
    op.drop_table('experiment')
    op.drop_table('exposure')
