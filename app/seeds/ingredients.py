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
    ing13 = Ingredient(
        recipe_id = 2,
        amount = '8',
        measurement_unit_id = 23,
        food_stuff = 'eggs',
        )
    ing14 = Ingredient(
        recipe_id = 2,
        amount = '1/2',
        measurement_unit_id = 2,
        food_stuff = 'cup finely chopped smoked salmon (2 ounces)',
        )
    ing15 = Ingredient(
        recipe_id = 2,
        amount = '1/3',
        measurement_unit_id = 2,
        food_stuff = 'mayonnaise',
        )
    ing16 = Ingredient(
        recipe_id = 2,
        amount = '2',
        measurement_unit_id = 1,
        food_stuff = 'cornichons cut into 1/4-inch dice',
        )
    ing17 = Ingredient(
        recipe_id = 2,
        amount = '2',
        measurement_unit_id = 9,
        food_stuff = 'pickling liquid from the cornichons jar',
        )
    ing18 = Ingredient(
        recipe_id = 2,
        amount = '2',
        measurement_unit_id = 9,
        food_stuff = 'Dijon mustard',
        )
    ing19 = Ingredient(
        recipe_id = 2,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'Salt',
        )
    ing20 = Ingredient(
        recipe_id = 3,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'celery ribs cut into 1/2-inch pieces',
        )
    ing21 = Ingredient(
        recipe_id = 3,
        amount = '4',
        measurement_unit_id = 10,
        food_stuff = 'unsalted butter',
        )
    ing22 = Ingredient(
        recipe_id = 3,
        amount = '2',
        measurement_unit_id = 1,
        food_stuff = 'carrots cut into 1/2-inch pieces',
        )
    ing23 = Ingredient(
        recipe_id = 3,
        amount = '1',
        measurement_unit_id = 24,
        food_stuff = 'chopped onion',
        )
    ing24 = Ingredient(
        recipe_id = 3,
        amount = '1',
        measurement_unit_id = 1,
        food_stuff = 'garlic cloves minced',
        )
    ing25 = Ingredient(
        recipe_id = 3,
        amount = '1 1/2',
        measurement_unit_id = 9,
        food_stuff = 'finely chopped thyme',
        )
    ing26 = Ingredient(
        recipe_id = 3,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'Salt',
        )
    ing27 = Ingredient(
        recipe_id = 3,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'Pepper',
        )
    ing28 = Ingredient(
        recipe_id = 3,
        amount = '1/4',
        measurement_unit_id = 2,
        food_stuff = 'all-purpose flour',
        )
    ing29 = Ingredient(
        recipe_id = 3,
        amount = '1',
        measurement_unit_id = 2,
        food_stuff = 'wild rice (5 ounces)',
        )
    ing30 = Ingredient(
        recipe_id = 3,
        amount = '2',
        measurement_unit_id = 4,
        food_stuff = 'chicken stock or low-sodium broth',
        )
    ing31 = Ingredient(
        recipe_id = 3,
        amount = '2',
        measurement_unit_id = 2,
        food_stuff = 'water',
        )
    ing32 = Ingredient(
        recipe_id = 3,
        amount = '4',
        measurement_unit_id = 2,
        food_stuff = 'bite-size pieces of roasted chicken or turkey',
        )
    ing33 = Ingredient(
        recipe_id = 4,
        amount = '1 1/4',
        measurement_unit_id = 6,
        food_stuff = 'apricots halved and pitted',
        )
    ing34 = Ingredient(
        recipe_id = 4,
        amount = '1/4',
        measurement_unit_id = 2,
        food_stuff = 'extra-virgin olive oil plus more for brushing',
        )
    ing35 = Ingredient(
        recipe_id = 4,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'Sea salt',
        )
    ing36 = Ingredient(
        recipe_id = 4,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'freshly ground pepper',
        )
    ing37 = Ingredient(
        recipe_id = 4,
        amount = '1 1/2',
        measurement_unit_id = 10,
        food_stuff = 'fresh lemon juice',
        )
    ing38 = Ingredient(
        recipe_id = 4,
        amount = '1',
        measurement_unit_id = 30,
        food_stuff = 'head cored and thinly sliced radicchio',
        )
    ing39 = Ingredient(
        recipe_id = 4,
        amount = '5',
        measurement_unit_id = 7,
        food_stuff = 'baby arugula',
        )
    ing40 = Ingredient(
        recipe_id = 5,
        amount = '1/2',
        measurement_unit_id = 2,
        food_stuff = 'butter',
        )
    ing41 = Ingredient(
        recipe_id = 4,
        amount = '1/2',
        measurement_unit_id = 6,
        food_stuff = 'shredded burrata cheese',
        )
    ing42 = Ingredient(
        recipe_id = 4,
        amount = '4',
        measurement_unit_id = 7,
        food_stuff = 'shaved country ham',
        )
 
    ing43 = Ingredient(
        recipe_id = 5,
        amount = '4',
        measurement_unit_id = 1,
        food_stuff = 'cloves garlic (minced)',
        )
    ing24 = Ingredient(
        recipe_id = 5,
        amount = '1/2',
        measurement_unit_id = 2,
        food_stuff = 'mustard',
        )
    ing25 = Ingredient(
        recipe_id = 5,
        amount = '1/3',
        measurement_unit_id = 2,
        food_stuff = 'honey',
        )
    ing26 = Ingredient(
        recipe_id = 5,
        amount = '1',
        measurement_unit_id = 10,
        food_stuff = 'Worcestershire sauce',
        )
    ing27 = Ingredient(
        recipe_id = 5,
        amount = '1',
        measurement_unit_id = 9,
        food_stuff = 'apple cider vinegar',
        )
    ing28 = Ingredient(
        recipe_id = 5,
        amount = '1/2',
        measurement_unit_id = 9,
        food_stuff = 'kosher or sea salt (plus more for seasoning)',
        )
    ing29 = Ingredient(
        recipe_id = 5,
        amount = '1/2',
        measurement_unit_id = 9,
        food_stuff = 'black pepper (plus more for seasoning)',
        )
    ing30 = Ingredient(
        recipe_id = 5,
        amount = '2',
        measurement_unit_id = 6,
        food_stuff = 'chicken wings (split)',
        )
    ing31 = Ingredient(
        recipe_id = 5,
        amount = '1',
        measurement_unit_id = 2,
        food_stuff = 'all-purpose flour (for dredging)',
        )
    ing32 = Ingredient(
        recipe_id = 6,
        amount = '1 1/2',
        measurement_unit_id = 2,
        food_stuff = 'packed light brown sugar',
        )
    ing33 = Ingredient(
        recipe_id = 6,
        amount = '1/2',
        measurement_unit_id = 2,
        food_stuff = 'honey',
        )
    ing34 = Ingredient(
        recipe_id = 6,
        amount = '1/4',
        measurement_unit_id = 2,
        food_stuff = 'Dijon mustard',
        )
    ing35 = Ingredient(
        recipe_id = 6,
        amount = '1/2',
        measurement_unit_id = 9,
        food_stuff = 'kosher salt',
        )
    ing36 = Ingredient(
        recipe_id = 6,
        amount = '1/2',
        measurement_unit_id = 9,
        food_stuff = 'black pepper',
        )
    ing37 = Ingredient(
        recipe_id = 6,
        amount = '1',
        measurement_unit_id = 2,
        food_stuff = 'apple cider divided',
        )
    ing38 = Ingredient(
        recipe_id = 6,
        amount = '9',
        measurement_unit_id = 6,
        food_stuff = 'fully cooked bone-in spiral-cut ham half',
        )
    ing39 = Ingredient(
        recipe_id = 7,
        amount = '1',
        measurement_unit_id = 6,
        food_stuff = 'beef flat iron steak',
        )
    ing40 = Ingredient(
        recipe_id = 7,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'Salt',
        )
    ing41 = Ingredient(
        recipe_id = 7,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'Freshly ground pepper',
        )
    ing42 = Ingredient(
        recipe_id = 7,
        amount = '2',
        measurement_unit_id = 10,
        food_stuff = 'extra-virgin olive oil',
        )
 
    ing43 = Ingredient(
        recipe_id = 7,
        amount = '2',
        measurement_unit_id = 1,
        food_stuff = 'garlic cloves, minced',
        )
    ing44 = Ingredient(
        recipe_id = 7,
        amount = '4',
        measurement_unit_id = 1,
        food_stuff = 'scallions, chopped',
        )
    ing45 = Ingredient(
        recipe_id = 7,
        amount = '4',
        measurement_unit_id = 1,
        food_stuff = 'bay leaves, broken into pieces',
        )
    ing46 = Ingredient(
        recipe_id = 7,
        amount = '2',
        measurement_unit_id = 1,
        food_stuff = 'lemons, very thinly sliced',
        )
    ing47 = Ingredient(
        recipe_id = 7,
        amount = '',
        measurement_unit_id = 1,
        food_stuff = 'Vegetable oil, for brushing',
        )
    # ing48 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing49 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing50 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing51 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing52 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing53 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing54 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing55 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing56 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing57 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing58 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing59 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing60 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing61 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing62 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
 
    # ing63 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing64 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing65 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing66 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing67 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing68 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing69 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing70 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing71 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing72 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing73 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing74 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing75 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing76 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing77 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing78 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing79 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing80 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing81 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing82 = Ingredient(
    #     recipe_id = ,
    #     amount = ,
    #     measurement_unit_id = ,
    #     food_stuff = ,
    #     )
    # ing83 = Ingredient(
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
    db.session.add(ing13)
    db.session.add(ing14)
    db.session.add(ing15)
    db.session.add(ing16)
    db.session.add(ing17)
    db.session.add(ing18)
    db.session.add(ing19)
    db.session.add(ing20)
    db.session.add(ing21)
    db.session.add(ing22)
    db.session.add(ing23)
    db.session.add(ing24)
    db.session.add(ing25)
    db.session.add(ing26)
    db.session.add(ing27)
    db.session.add(ing28)
    db.session.add(ing29)
    db.session.add(ing30)
    db.session.add(ing31)
    db.session.add(ing32)
    db.session.add(ing33)
    db.session.add(ing34)
    db.session.add(ing35)
    db.session.add(ing36)
    db.session.add(ing37)
    db.session.add(ing38)
    db.session.add(ing39)
    db.session.add(ing40)
    db.session.add(ing41)
    db.session.add(ing42)
    db.session.add(ing43)
    db.session.add(ing44)
    db.session.add(ing45)
    db.session.add(ing46)
    db.session.add(ing47)
    # db.session.add(ing48)
    # db.session.add(ing49)
    # db.session.add(ing50)
    # db.session.add(ing51)
    # db.session.add(ing52)
    # db.session.add(ing53)
    # db.session.add(ing54)
    # db.session.add(ing55)
    # db.session.add(ing56)
    # db.session.add(ing57)
    # db.session.add(ing58)
    # db.session.add(ing59)
    # db.session.add(ing50)
    # db.session.add(ing51)
    # db.session.add(ing52)
    # db.session.add(ing53)
    # db.session.add(ing54)
    # db.session.add(ing55)
    # db.session.add(ing56)
    # db.session.add(ing57)
    # db.session.add(ing58)
    # db.session.add(ing59)
    # db.session.add(ing60)
    # db.session.add(ing61)
    # db.session.add(ing62)
    # db.session.add(ing63)
    # db.session.add(ing64)
    # db.session.add(ing65)
    # db.session.add(ing66)
    # db.session.add(ing67)
    # db.session.add(ing68)
    # db.session.add(ing69)
    # db.session.add(ing70)
    # db.session.add(ing71)
    # db.session.add(ing72)
    # db.session.add(ing73)
    # db.session.add(ing74)
    # db.session.add(ing75)
    # db.session.add(ing76)
    # db.session.add(ing77)
    # db.session.add(ing78)
    # db.session.add(ing79)
    # db.session.add(ing80)
    # db.session.add(ing81)
    # db.session.add(ing82)
    # db.session.add(ing83)
    # db.session.add(ing84)
    # db.session.add(ing85)
    # db.session.add(ing86)
    # db.session.add(ing87)
    # db.session.add(ing88)
    # db.session.add(ing89)
    # db.session.add(ing90)
    # db.session.add(ing91)
    # db.session.add(ing92)
    

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_ingredients():
    db.session.execute('TRUNCATE ingredients RESTART IDENTITY CASCADE;')
    db.session.commit()
