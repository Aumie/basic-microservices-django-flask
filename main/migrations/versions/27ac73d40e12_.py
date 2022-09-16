"""empty message

Revision ID: 27ac73d40e12
Revises: eb8e1fa948e0
Create Date: 2022-09-15 12:14:33.508753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27ac73d40e12'
down_revision = 'eb8e1fa948e0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'product_user', ['product_id'])
    op.create_unique_constraint(None, 'product_user', ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'product_user', type_='unique')
    op.drop_constraint(None, 'product_user', type_='unique')
    # ### end Alembic commands ###