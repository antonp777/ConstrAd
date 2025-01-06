"""upgrade table

Revision ID: 5b0d056bbbaf
Revises: 7285e064ce23
Create Date: 2025-01-06 17:09:18.142038

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5b0d056bbbaf"
down_revision: Union[str, None] = "7285e064ce23"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:

    op.alter_column(
        "tasks",
        "phone",
        existing_type=sa.INTEGER(),
        type_=sa.String(),
        existing_nullable=False,
    )



def downgrade() -> None:

    op.alter_column(
        "tasks",
        "phone",
        existing_type=sa.String(),
        type_=sa.INTEGER(),
        existing_nullable=False,
    )

