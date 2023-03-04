"""empty message

Revision ID: 833eba1f3928
Revises: 62695497e424
Create Date: 2023-03-04 21:22:48.685297

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '833eba1f3928'
down_revision = '62695497e424'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.drop_column('lastname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lastname', sa.VARCHAR(length=80), autoincrement=False, nullable=False))

    # ### end Alembic commands ###