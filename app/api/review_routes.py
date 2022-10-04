from flask import Blueprint, request
from app.api.auth_routes import validation_errors_to_error_messages
from app.models import Review, db
from app.forms import CreateReview
from .auth_routes import validation_errors_to_error_messages

reviews_route = Blueprint('reviews', __name__)

# load all reviews
@reviews_route.route('/')
def get_reviews():
    reviews = Review.query.all()
    return {'reviews': [review.to_dict() for review in reviews]}

# create a review 
@reviews_route.route('/', methods=['POST'])
def add_review():
    form = CreateReview()
    form['csrf_token'].data = request.cookies['csrf_token']
    if (form.validate_on_submit()):
        review = Review(
            user_id = form.data['user_id'],
            recipe_id = form.data['recipe_id'],
            stars = form.data['stars'],
            review = form.data['review'],
        )

        db.session.add(review)
        db.session.commit()
        return review.to_dict()
    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

@reviews_route.route('/<int:review_id>', methods=['PUT'])
def edit_review(review_id):
    review = Review.query.get(review_id)
    form = CreateReview()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user_id = form.data['user_id'],
        recipe_id = form.data['recipe_id']
        stars = form.data['stars'],
        body = form.data['review'],
  
        review.user_id = user_id
        review.recipe_id = recipe_id
        review.stars = stars
        review.review = body

        db.session.commit()
        return review.to_dict()
    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

@reviews_route.route('/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    review = Review.query.get(review_id)
    db.session.delete(review)
    db.session.commit()
    return { 'message': 'Review Deleted!' }
