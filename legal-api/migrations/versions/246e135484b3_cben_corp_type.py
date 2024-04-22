"""CBEN corp type

Revision ID: 246e135484b3
Revises: 146e135484b2
Create Date: 2024-04-19

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '246e135484b3'
down_revision = '146e135484b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("""insert into corp_types (corp_type_cd, colin_ind, corp_class, short_desc, full_desc, legislation) 
               values('CBEN', 'Y', 'BC', 'BENEFIT COMPANY', 'BC Benefit Company', 'BC Business Corporations Act')""")
    op.execute("update corp_types set full_desc='BC Unlimited Liability Company' where corp_type_cd = 'CUL'")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("delete from corp_types where corp_type_cd = 'CBEN'")
    # ### end Alembic commands ###
