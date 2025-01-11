"""refresh token table created

Revision ID: 0e71a5abe935
Revises: 6b90de1b7dd0
Create Date: 2025-01-12 00:19:55.137517

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = '0e71a5abe935'
down_revision: Union[str, None] = '6b90de1b7dd0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('refresh_token',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('token', sa.VARCHAR(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.Integer(), nullable=False),
    sa.Column('issued_at', sa.DateTime(), nullable=False),
    sa.Column('expires_at', sa.DateTime(), nullable=False),
    sa.Column('revoked', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['application_id'], ['secure.application.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['secure.user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token'),
    schema='secure'
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('refresh_token', schema='secure')
    # ### end Alembic commands ###
