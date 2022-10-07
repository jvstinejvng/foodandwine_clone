from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import User, Recipe, db
from ..forms import RecipeForm
from .auth_routes import validation_errors_to_error_messages

recipe_routes = Blueprint('recipes', __name__)

# all recipes
@recipe_routes.route('')
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}

# add a recipe
@recipe_routes.route('', methods=['POST'])
def post_recipe():
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        recipe = Recipe(
            
            user_id = form.data['user_id'],
            title = form.data['title'],
            description = form.data['description'],
            image_url = form.data['image_url'],
            total_time = form.data['total_time'],
            servings = form.data['servings'],
            ingredients = form.data['ingredients'],
            directions = form.data['directions']
        )

        db.session.add(recipe)
        db.session.commit()
        return recipe.to_dict()

    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

# edit a recipe
@recipe_routes.route('/<int:recipe_id>', methods=['PUT'])
@login_required
def edit_recipe(recipe_id):
    print(recipe_id)
    recipe = Recipe.query.get(recipe_id)
    form = RecipeForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    print(recipe , "inside")

    if form.validate_on_submit():
        recipe.user_id = form.data['user_id'],
        recipe.title = form.data['title'],
        recipe.description = form.data['description'],
        recipe.image_url = form.data['image_url'],
        recipe.total_time = form.data['total_time'],
        recipe.servings = form.data['servings'],
        recipe.ingredients = form.data['ingredients'],
        recipe.directions = form.data['directions']



        db.session.commit()
        return recipe.to_dict()

    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

# delete a recipe
@recipe_routes.route('/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return { "message": "Recipe Deleted!" }

