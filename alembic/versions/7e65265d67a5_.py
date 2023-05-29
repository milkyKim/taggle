"""empty message

Revision ID: 7e65265d67a5
Revises: 
Create Date: 2023-05-30 01:23:39.003968

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e65265d67a5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('arn', sa.String(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('region', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('key', sa.String(), nullable=False),
    sa.Column('value', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('association',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('resource_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['resource_id'], ['resource.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('tag_id', 'resource_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('association')
    op.drop_table('tag')
    op.drop_table('resource')
    # ### end Alembic commands ###
