"""empty message

Revision ID: c4ff006df210
Revises: 750265cdfbdf
Create Date: 2023-03-02 20:05:29.175320

"""
from alembic import op
import sqlalchemy as sa
import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = 'c4ff006df210'
down_revision = '750265cdfbdf'
branch_labels = None
depends_on = None


def upgrade():
    pass

    if environment == "production":
        op.execute(f"ALTER TABLE <table_name> SET SCHEMA {SCHEMA};")

def downgrade():
    pass
