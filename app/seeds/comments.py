from app.models import db, Comment

def seed_comments():

    c1 = Comment(
        rating = 5,
        body = 'This recipe was really tasty.',
        user_id = 2,
        recipe_id = 1
        )
    c2 = Comment(
        rating = 2,
        body = 'This recipe has so many layers of flavor.',
        user_id = 3,
        recipe_id = 1
        )
    c3 = Comment(
        rating = 4,
        body = 'Love this recipe very much. Thanks for posting.',
        user_id = 3,
        recipe_id = 2
        )
    c4 = Comment(
        rating = 5,
        body = 'I have been making this recipe for the past five years on Christmas Eve for lunch. It is such a fantastic recipe.',
        user_id = 2,
        recipe_id = 2
        )
    c5 = Comment(
        rating = 5,
        body = 'The Holy Grail of recipes: easy, fast, delicious, healthy',
        user_id = 2,
        recipe_id = 13
        )
    c6 = Comment(
        rating = 2,
        body = 'This recipe is my favorite thing about 2020.',
        user_id = 3,
        recipe_id = 3
        )
    c7 = Comment(
        rating = 3,
        body = 'This was ok, but not great, I\'ve had better.',
        user_id = 4,
        recipe_id = 25
        )
    c8 = Comment(
        rating = 5,
        body = 'We loved this meal! Simple to prepare but feels very special.',
        user_id = 5,
        recipe_id = 16
        )
    c9 = Comment(
        rating = 2,
        body = 'Disappointed with the flavor. Would not make again.',
        user_id = 6,
        recipe_id = 28
        )
    c10 = Comment(
        rating = 5,
        body = 'This is best recipe I have made so far this year!! If you are making jams as gifts you should add this to your list for sure! It is amazing!!',
        user_id = 7,
        recipe_id = 23
        )
    c11 = Comment(
        rating = 5,
        body = 'Super easy to make. Delicious and great flavor',
        user_id = 8,
        recipe_id = 5
        )
    c12 = Comment(
        rating = 1,
        body = 'This recipe stinks. I followed it to the letter, and what I got was flabby, almost tasteless bacon with a hint of sweetness to it. I don\'t know if the writer actually used thick cut bacon (I did), but it took a LOT longer than the recipe stated, and the bacon was still flabby. And nearly set my oven on fire, with all the smoke from the melted, burned sugar on the bottom of the pan. Don\'t waste your time or bacon on this.',
        user_id = 9,
        recipe_id = 15
        )
    c13 = Comment(
        rating = 1,
        body = 'Don\'t make this cake. We were so excited to see this on the website. Extremely disappointed. It was so so dry.',
        user_id = 10,
        recipe_id = 19
        )
    c14 = Comment(
        rating = 4,
        body = 'Good use of our leftover, but my children did not like that there was canberry sauce mixed-in.',
        user_id = 9,
        recipe_id = 26
        )
    c15 = Comment(
        rating = 5,
        body = 'This was a very creative way to use leftover turkey. We had almost everything on hand. Totally recommend this for the family!!!',
        user_id = 8,
        recipe_id = 26
        )
    c16 = Comment(
        rating = 4,
        body = 'Not really the way I do salmon, but I was impressed when I made it the other night!',
        user_id = 4,
        recipe_id = 8
        )
    c17 = Comment(
        rating = 5,
        body = 'Rave reviews on this from my guests. DELICIOUS. I used a bit more zest and a bit less lemon juice.',
        user_id = 7,
        recipe_id = 14
        )
    c18 = Comment(
        rating = 2,
        body = 'I followed the directions to a tee but this cut of meat is not tender at all. Will definitely not make it again.',
        user_id = 5,
        recipe_id = 7
        )


    db.session.add(c1)
    db.session.add(c2)
    db.session.add(c3)
    db.session.add(c4)
    db.session.add(c5)
    db.session.add(c6)
    db.session.add(c7)
    db.session.add(c8)
    db.session.add(c9)
    db.session.add(c10)
    db.session.add(c11)
    db.session.add(c12)
    db.session.add(c13)
    db.session.add(c14)
    db.session.add(c15)
    db.session.add(c16)
    db.session.add(c17)
    db.session.add(c18)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_comments():
    db.session.execute('TRUNCATE comments RESTART IDENTITY CASCADE;')
    db.session.commit()
