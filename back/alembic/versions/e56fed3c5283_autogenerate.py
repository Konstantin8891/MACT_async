from alembic import op
import sqlalchemy as sa

revision = 'e56fed3c5283'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'museums',
        sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
        sa.Column('service', sa.Text(), nullable=False),
        sa.Column('title', sa.Text(), nullable=False),
        sa.Column('link', sa.Text(), nullable=False),
        sa.Column('content', sa.Text(), nullable=False),
        sa.Column('added', sa.DateTime(), nullable=False)
    )
    op.create_index(op.f('ix_museums_id'), 'museums', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_museums_id'), table_name='museums')
    op.drop_table('museums')
