"""empty message

Revision ID: f3ad008e8cbe
Revises: 3c160bd44927
Create Date: 2025-02-05 17:58:27.660040

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3ad008e8cbe'
down_revision = '3c160bd44927'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(),
               nullable=True)

    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('restaurants', schema=None) as batch_op:
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    with op.batch_alter_table('restaurant_pizzas', schema=None) as batch_op:
        batch_op.alter_column('pizza_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('restaurant_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('pizzas', schema=None) as batch_op:
        batch_op.alter_column('ingredients',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###
