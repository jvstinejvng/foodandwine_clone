from app.seeds.recipes import undo_recipes
from app.models.db import db, environment, SCHEMA

from flask.cli import AppGroup
from .users import seed_users, undo_users
from .recipes import seed_recipes, undo_recipes
from .comments import seed_comments, undo_comments

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding, truncate all tables prefixed with schema name
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
        # Add a truncate command here for every table that will be seeded.
        db.session.commit()
    seed_users()

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_users()
    seed_recipes()
    seed_comments()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_recipes()
    undo_comments()
    # Add other undo functions here
