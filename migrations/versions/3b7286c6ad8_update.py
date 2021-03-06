"""update

Revision ID: 3b7286c6ad8
Revises: 4c0fcbe4629
Create Date: 2014-10-14 19:32:15.349273

"""

# revision identifiers, used by Alembic.
revision = '3b7286c6ad8'
down_revision = '4c0fcbe4629'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_tags_url'), 'tags', ['url'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tags_url'), table_name='tags')
    ### end Alembic commands ###
