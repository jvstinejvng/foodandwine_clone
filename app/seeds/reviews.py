from app.models import db, Review

def seed_reviews():
    reviews = [
    Review(
        user_id=1,
        recipe_id=1,
        stars=5,
        review='I love this recipe very much. Thanks for posting.',
    ),
    Review(
        user_id=1,
        recipe_id=2,
        stars=5,
        review='​​This recipe has so many layers of flavor that create a rich sauce with great nuance. Coconut rice accentuates these flavors without a lot of sweetness. It is one of the best curries I have had, and all my dinner guests asked for the recipe.',
    ),
    Review(
        user_id=1,
        recipe_id=3,
        stars=5,
        review='​This recipe is packed full of amazing flavor',
    ),
    Review(
        user_id=1,
        recipe_id=4,
        stars=5,
        review='I made this for the first time recently after a co-worker recommended it — it was delicious!',
    ),
    Review(
        user_id=1,
        recipe_id=5,
        stars=5,
        review='Great and easy recipe. The double frying makes perfect, restaurant-level potatoes.',
    )
    ]

    for review in reviews:
        db.session.add(review)

    db.session.commit()


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()