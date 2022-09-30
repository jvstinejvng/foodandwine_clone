from app.models import db, Review

def seed_reviews():
    reviews = [
    Review(
        user_id=1,
        recipe_id=1,
        stars=5,
        comment='I love this recipe very much. Thanks for posting.',
    ),
    Review(
        user_id=1,
        recipe_id=2,
        stars=5,
        comment='​​This recipe has so many layers of flavor.',
    ),
    Review(
        user_id=1,
        recipe_id=3,
        stars=5,
        comment='​This recipe is packed full of amazing flavor',
    ),
    Review(
        user_id=1,
        recipe_id=4,
        stars=5,
        comment='I made this for the first time recently after a co-worker recommended it — it was delicious!',
    ),
    Review(
        user_id=1,
        recipe_id=5,
        stars=5,
        comment='Great and easy recipe. The double frying makes perfect, restaurant-level potatoes.',
    )
    ]

    for review in reviews:
        db.session.add(review)

    db.session.commit()


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()