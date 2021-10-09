"""hange hash field x3

Revision ID: 3f7082264564
Revises: cae261c4805c
Create Date: 2021-10-09 22:21:30.369097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f7082264564'
down_revision = 'cae261c4805c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('domains', sa.Column('fqdn_hash', sa.String(length=120), nullable=True))
    op.drop_column('domains', 'hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('domains', sa.Column('hash', sa.VARCHAR(length=40), autoincrement=False, nullable=True))
    op.drop_column('domains', 'fqdn_hash')
    # ### end Alembic commands ###
