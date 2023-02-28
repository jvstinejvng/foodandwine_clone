from app.models import db, Ingredient, measurement_units

def seed_ingredients():
    ing1 = Ingredient(
        recipe_id = 1,
        amount = '6',
        measurement_unit_id = 7,
        food_stuff = 'soft silken drained tofu',
        )
    ing2 = Ingredient(
        recipe_id = 1,
        amount = '1 1/2',
        measurement_unit_id = 10,
        food_stuff = 'extra-virgin olive oil',
        )
    ing3 = Ingredient(
        recipe_id = 1,
        amount = '1 1/2',
        measurement_unit_id = 10,
        food_stuff = 'fresh lemon juice',
        )
    ing4 = Ingredient(
        recipe_id = 1,
        amount = '1 1/2',
        measurement_unit_id = 10,
        food_stuff = 'freshly grated Parmigiano-Reggiano cheese plus more for serving',
        )
    ing5 = Ingredient(
        recipe_id = 1,
        amount = '1',
        measurement_unit_id = 1,
        food_stuff = 'oil-packed anchovy drained fillet',
        )
    ing6 = Ingredient(
        recipe_id = 1,
        amount = '1',
        measurement_unit_id = 30,
        food_stuff = 'garlic clove',
        )
    ing7 = Ingredient(
        recipe_id = 1,
        amount = '1/2',
        measurement_unit_id = 9,
        food_stuff = 'Worcestershire sauce',
        )
    ing8 = Ingredient(
        recipe_id = 1,
        amount = '1/2',
        measurement_unit_id = 9,
        food_stuff = 'Dijon mustard',
        )
    ing9 = Ingredient(
        recipe_id = 1,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'Salt and freshly ground pepper',
        )
    ing10 = Ingredient(
        recipe_id = 1,
        amount = '14',
        measurement_unit_id = 7,
        food_stuff = 'package firm drained tofu cut into 3/4-inch cubes',
        )
    ing11 = Ingredient(
        recipe_id = 1,
        amount = '',
        measurement_unit_id = 1, 
        food_stuff = 'Vegetable oil for frying' ,
        )
    ing12 = Ingredient(
        recipe_id = 1,
        amount = '1/2',
        measurement_unit_id = 2 ,
        food_stuff = 'cornstarch',
        )
    
    # ing13 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing14 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing15 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing16 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing17 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing19 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )

    
    # ing = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )



    db.session.add(ing1)
    db.session.add(ing2)
    db.session.add(ing3)
    db.session.add(ing4)
    db.session.add(ing5)
    db.session.add(ing6)
    db.session.add(ing7)
    db.session.add(ing8)
    db.session.add(ing9)
    db.session.add(ing10)
    db.session.add(ing11)
    db.session.add(ing12)
    

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
