"""previous_step put as nullable

Revision ID: 9a6fc5dc19c5
Revises: dc5e2b38cbc8
Create Date: 2017-01-12 11:44:41.808421

"""

# revision identifiers, used by Alembic.
revision = '9a6fc5dc19c5'
down_revision = 'dc5e2b38cbc8'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('processing_step', 'previous_step_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('processing_step', 'previous_step_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###