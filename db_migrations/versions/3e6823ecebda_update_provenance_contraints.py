"""update provenance contraints

Revision ID: 3e6823ecebda
Revises: 573f9ca528eb
Create Date: 2017-01-12 14:52:12.903195

"""

# revision identifiers, used by Alembic.
revision = '3e6823ecebda'
down_revision = '573f9ca528eb'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'processing_step', ['name'])
    op.alter_column('provenance', 'fn_called',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('provenance', 'fn_version',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('provenance', 'matlab_version',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('provenance', 'spm_revision',
               existing_type=sa.TEXT(),
               nullable=True)
    op.alter_column('provenance', 'spm_version',
               existing_type=sa.TEXT(),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('provenance', 'spm_version',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('provenance', 'spm_revision',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('provenance', 'matlab_version',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('provenance', 'fn_version',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('provenance', 'fn_called',
               existing_type=sa.TEXT(),
               nullable=False)
    op.drop_constraint(None, 'processing_step', type_='unique')
    ### end Alembic commands ###
