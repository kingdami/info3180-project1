"""empty message

Revision ID: 6a27051fd05f
Revises: b3c6c5796f97
Create Date: 2017-03-14 19:53:00.549881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a27051fd05f'
down_revision = 'b3c6c5796f97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('age', sa.Integer(), nullable=True))
    op.create_unique_constraint(None, 'user_profile', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profile', type_='unique')
    op.drop_column('user_profile', 'age')
    # ### end Alembic commands ###
