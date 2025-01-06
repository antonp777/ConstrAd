"""create table

Revision ID: 7285e064ce23
Revises: 
Create Date: 2025-01-06 11:37:10.437840

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7285e064ce23"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name_user", sa.String(), nullable=False),
        sa.Column("tg_id", sa.BigInteger(), nullable=False),
        sa.Column(
            "role_user",
            sa.Enum("SUPER_ADMIN", "ADMIN", "CLIENT", name="roleuser"),
            nullable=False,
        ),

        sa.PrimaryKeyConstraint("id", name=op.f("pk_users")),
    )
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("district", sa.String(), nullable=False),
        sa.Column("work", sa.String(), nullable=False),
        sa.Column("price_work", sa.Integer(), nullable=False),
        sa.Column("person", sa.Integer(), nullable=False),
        sa.Column("fee", sa.Integer(), nullable=False),
        sa.Column("phone", sa.Integer(), nullable=False),
        sa.Column(
            "status_task",
            sa.Enum("ACTIVE", "NONACTIVE", name="statustask"),
            nullable=False,
        ),

        sa.PrimaryKeyConstraint("id", name=op.f("pk_tasks")),
    )
    op.create_table(
        "orders",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.Column("task_id", sa.Integer(), nullable=False),
        sa.Column("task_fee", sa.Integer(), nullable=False),
        sa.Column("task_person", sa.Integer(), nullable=False),
        sa.Column(
            "date",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),

        sa.ForeignKeyConstraint(
            ["task_id"], ["tasks.id"], name=op.f("fk_orders_task_id_tasks")
        ),
        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_orders_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_orders")),
    )
    op.create_table(
        "payments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("sum", sa.Integer(), nullable=False),
        sa.Column(
            "date",
            sa.DateTime(),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "status_pay",
            sa.Enum("OK", "NOTOK", "WAIT", name="statuspay"),
            nullable=False,
        ),
        sa.Column("user_id", sa.Integer(), nullable=False),

        sa.ForeignKeyConstraint(
            ["user_id"], ["users.id"], name=op.f("fk_payments_user_id_users")
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_payments")),
    )


def downgrade() -> None:
    op.drop_table("payments")
    op.drop_table("orders")
    op.drop_table("users")
    op.drop_table("tasks")
