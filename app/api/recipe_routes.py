from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import db, Recipe
from app.forms import CreateRecipe
from app.api.auth_routes import validation_errors_to_error_messages

recipe_routes = Blueprint('recipes', __name__)

# Get all recipes
@recipe_routes.route('')
def get_recipes():
    recipes = Recipe.query.all()
    return {'recipes': [recipe.to_dict() for recipe in recipes]}

@recipe_routes.route('/', methods=['POST'])
@login_required
def add_user_recipe():
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
        directions=data['directions'],
    )

    db.session.add(recipe)
    db.session.commit()

    return recipe.to_dict()

  return {'errors': validation_errors_to_error_messages(form.errors)}, 400
