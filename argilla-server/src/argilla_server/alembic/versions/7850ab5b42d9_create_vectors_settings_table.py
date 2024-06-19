#  Copyright 2021-present, the Recognai S.L. team.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""create vectors settings table

Revision ID: 7850ab5b42d9
Revises: 84f6b9ff6076
Create Date: 2023-09-12 16:21:14.321044

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "7850ab5b42d9"
down_revision = "84f6b9ff6076"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "vectors_settings",
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("dimensions", sa.Integer(), nullable=False),
        sa.Column("dataset_id", sa.Uuid(), nullable=False),
        sa.Column("id", sa.Uuid(), nullable=False),
        sa.Column("inserted_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(["dataset_id"], ["datasets.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("name", "dataset_id", name="vector_settings_name_dataset_id_uq"),
    )
    op.create_index(op.f("ix_vectors_settings_dataset_id"), "vectors_settings", ["dataset_id"], unique=False)
    op.create_index(op.f("ix_vectors_settings_name"), "vectors_settings", ["name"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_vectors_settings_name"), table_name="vectors_settings")
    op.drop_index(op.f("ix_vectors_settings_dataset_id"), table_name="vectors_settings")
    op.drop_table("vectors_settings")
    # ### end Alembic commands ###
