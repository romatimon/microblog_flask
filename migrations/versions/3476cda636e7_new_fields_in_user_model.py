"""new fields in user model

Revision ID: 3476cda636e7
Revises: b50fbc3f468d
Create Date: 2024-06-08 22:05:14.009618

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3476cda636e7'
down_revision = 'b50fbc3f468d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(length=140), nullable=True))
        batch_op.add_column(sa.Column('last_seen', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_seen')
        batch_op.drop_column('about_me')

    # ### end Alembic commands ###
