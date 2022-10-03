from flask import Blueprint, request
from app.models import db, Recipe, User
from flask_login import login_required, current_user
from app.forms import CreateRecipe
from app.api.auth_routes import validation_errors_to_error_messages

recipe_routes = Blueprint('recipes', __name__)

# get all recipes
@recipe_routes.route('/')
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}

# add a recipe
@recipe_routes.route('/new-recipe/', methods=['POST'])
@login_required
def add_recipe():
    form = CreateRecipe()
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data

    if form.validate_on_submit():
        recipe = Recipe(
            user_id=current_user.id,
            title=data['title'],
            description=data['description'],
            img_url=data['img_url'],
            total_time=data['total_time'],
            servings=data['servings'],
            ingredients=data['ingredients'],
            directions=data['directions']
        )

        db.session.add(recipe)
        db.session.commit()

        return recipe.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

# edit a recipe
@recipe_routes.route('/<int:id>', methods=['PUT'])
@login_required
def edit_recipe(id):
    form = CreateRecipe();
    form['csrf_token'].data = request.cookies['csrf_token']
    data = form.data

    if form.validate_on_submit():
        recipe = Recipe.query.get(id)
        recipe.title=data['title']
        recipe.description=data['description']
        recipe.img_url=data['img_url']
        recipe.total_time=data['total_time']
        recipe.servings=data['servings']
        recipe.ingredients=data['ingredients']
        recipe.directions=data['directions']

        db.session.commit()
        return recipe.to_dict()

    return {'errors': validation_errors_to_error_messages(form.errors)}, 400

# delete a recipes
@recipe_routes.route('/<int:id>', methods=['DELETE'])
@login_required
def delete_recipe(id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    recipes = Recipe.query.all()
    recipes_dict = {recipe.id: recipe.to_dict() for recipe in recipes}
    return recipes_dict
