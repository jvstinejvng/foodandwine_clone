from app.models.review import db, Review

def seed_reviews():
    
    r1 = Review(
        user_id=1,
        recipe_id=1,
        stars=5,
        review='I love this recipe very much. Thanks for posting.'
    )
    r2 = Review(
        user_id=1,
        recipe_id=2,
        stars=5,
        review='​​This recipe has so many layers of flavor.'
    )
    r3 = Review(
        user_id=1,
        recipe_id=3,
        stars=5,
        review='​This recipe is packed full of amazing flavor'
    )
    r4 = Review(
        user_id=1,
        recipe_id=4,
        stars=5,
        review='I made this for the first time recently after a co-worker recommended it — it was delicious!'
    )
    r5 = Review(
        user_id=1,
        recipe_id=5,
        stars=5,
        review='Great and easy recipe. The double frying makes perfect, restaurant-level potatoes.'
    )
    
    db.session.add(r1)
    db.session.add(r2)
    db.session.add(r3)
    db.session.add(r4)
    db.session.add(r5)
    
    db.session.commit()


def undo_reviews():
    db.session.execute('TRUNCATE reviews RESTART IDENTITY CASCADE;')
    db.session.commit()