from flask import Blueprint, request
from flask_login import login_required, current_user
from app.models import User, Recipe, db
from app.models import User, Recipe, Ingredient, Instruction, MeasurementUnit, db
from ..forms import RecipeForm, IngredientForm, InstructionForm
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
            # ingredients = form.data['ingredients'],
            # directions = form.data['directions']
        )

        db.session.add(recipe)
        db.session.commit()
        return recipe.to_dict()

    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

# add ingredients
@recipe_routes.route('/ingredients', methods=['POST'])
def post_ingredient():
    form = IngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        ingredient = Ingredient(
            amount = form.data['amount'],
            food_stuff = form.data['food_stuff'],
            measurement_unit_id = form.data['measurement_unit_id'],
            recipe_id = form.data['recipe_id']
        )

        db.session.add(ingredient)
        db.session.commit()
        return ingredient.to_dict()

    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

# add instructions
@recipe_routes.route('/instructions', methods=['POST'])
def post_instruction():
    form = InstructionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        instruction = Instruction(
            list_order = form.data['list_order'],
            specification = form.data['specification'],
            recipe_id = form.data['recipe_id']
        )

        db.session.add(instruction)
        db.session.commit()
        return instruction.to_dict()

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
        # recipe.ingredients = form.data['ingredients'],
        # recipe.directions = form.data['directions']

        db.session.commit()
        return recipe.to_dict()

    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

# edit ingredients
@recipe_routes.route('/ingredients/<int:ing_id>', methods=['PUT'])
def edit_ingredient(ing_id):
    ingredient = Ingredient.query.get(ing_id)

    form = IngredientForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        amount = form.data['amount'],
        food_stuff = form.data['food_stuff'],
        measurement_unit_id = form.data['measurement_unit_id'],
        recipe_id = form.data['recipe_id']

        ingredient.amount = amount
        ingredient.food_stuff = food_stuff
        ingredient.measurement_unit_id = measurement_unit_id
        ingredient.recipe_id = recipe_id

        db.session.commit()
        return ingredient.to_dict()

    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

# edit instructions
@recipe_routes.route('/instructions/<int:inst_id>', methods=['PUT'])
def edit_instruction(inst_id):
    instruction = Instruction.query.get(inst_id)

    form = InstructionForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        list_order = form.data['list_order'],
        specification = form.data['specification'],
        recipe_id = form.data['recipe_id']

        instruction.list_order = list_order
        instruction.specification = specification
        instruction.recipe_id = recipe_id

        db.session.commit()
        return instruction.to_dict()

    return {'errors': [validation_errors_to_error_messages(form.errors)]}, 401

# delete a recipe
@recipe_routes.route('/<int:recipe_id>', methods=['DELETE'])
def delete_recipe(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return { "message": "Recipe Deleted!" }

# delete an ingredient
@recipe_routes.route('/ingredients/<int:ing_id>', methods=['DELETE'])
def delete_ingredient(ing_id):
    ingredient = Ingredient.query.get(ing_id)
    db.session.delete(ingredient)
    db.session.commit()
    return { "message": "Ingredient Deleted!" }

# delete an instruction
@recipe_routes.route('/instructions/<int:inst_id>', methods=['DELETE'])
def delete_instruction(inst_id):
    instruction = Instruction.query.get(inst_id)
    db.session.delete(instruction)
    db.session.commit()
    return { "message": "Instruction Deleted!" }

# measurement units
@recipe_routes.route('/units')
def get_measurement_units():
    units = MeasurementUnit.query.all()
    return {"units": [unit.to_dict() for unit in units]}


#SAVES
# save a recipe
@recipe_routes.route('/<int:recipe_id>/save', methods=['PUT'])
def save_a_recipe(recipe_id):
    data = request.json
    user_id = data['user_id']

    recipe = Recipe.query.get(recipe_id)
    user = User.query.get(user_id)

    recipe.save_recipe(user)
    db.session.commit()

    return recipe.to_dict()

# unsave a recipe
@recipe_routes.route('/<int:recipe_id>/unsave', methods=['PUT'])
def forget_a_recipe(recipe_id):
    data = request.json
    user_id = data['user_id']

    recipe = Recipe.query.get(recipe_id)
    user = User.query.get(user_id)

    recipe.unsave_recipe(user)
    db.session.commit()

    return recipe.to_dict()
