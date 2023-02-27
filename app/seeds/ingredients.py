from app.models import db, Ingredient, measurement_units

def seed_ingredients():
    ing1 = Ingredient(
        recipe_id = 1
        amount = 250,
        food_stuff = 'sourdough starter',
        measurement_unit_id = 1,
        )
    

    db.session.add(ing1)
    db.session.add(ing2)
    db.session.add(ing3)
    db.session.add(ing4)
    db.session.add(ing5)
    db.session.add(ing6)
    db.session.add(ing7)
    db.session.add(ing8)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
