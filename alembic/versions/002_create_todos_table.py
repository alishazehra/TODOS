"""create todos table

Revision ID: 002
Revises: 001
Create Date: 2025-12-29

"""
from typing import Union
from alembic import op
import sqlalchemy as sa
import sqlmodel as sm

# revision identifiers, used by Alembic.
revision: str = '002'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, None] = None
depends_on: Union[str, None] = None


def upgrade() -> None:
    # Create todos table
    op.create_table(
        'todos',
        sa.Column('id', sa.String(length=36), nullable=False),
        sa.Column('user_id', sa.String(length=36), nullable=False),
        sa.Column('description', sa.String(length=1000), nullable=False),
        sa.Column('completed', sa.Boolean(), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_todos_user_id', 'todos', ['user_id'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_todos_user_id', table_name='todos')
    op.drop_table('todos')
