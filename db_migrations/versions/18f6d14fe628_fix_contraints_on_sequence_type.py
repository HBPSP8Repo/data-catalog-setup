"""fix contraints on sequence_type

Revision ID: 18f6d14fe628
Revises: c1ca632c3d16
Create Date: 2017-01-19 12:54:27.682051

"""

# revision identifiers, used by Alembic.
revision = '18f6d14fe628'
down_revision = 'c1ca632c3d16'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sequence_type', 'institution_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('sequence_type', 'manufacturer',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('sequence_type', 'manufacturer_model_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('sequence_type', 'manufacturer_model_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('sequence_type', 'manufacturer',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('sequence_type', 'institution_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
