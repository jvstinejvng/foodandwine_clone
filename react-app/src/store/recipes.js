// action
const LOAD_RECIPES = 'recipes/LOAD_RECIPES'
const ADD_RECIPE = 'recipes/ADD_RECIPE'
const EDIT_RECIPE = 'recipes/EDIT_RECIPE'
const DELETE_RECIPE ='recipes/DELETE_RECIPE'

// action creator
const getRecipes = recipes => {
    return {
        type: LOAD_RECIPES,
        recipes
    }
}

const addRecipe = recipe => {
    return {
        type: ADD_RECIPE,
        recipe
    }
}

const editRecipe = recipe => {
    return {
        type: EDIT_RECIPE,
        recipe
    }
}

const deleteRecipe = id => {
    return {
        type: DELETE_RECIPE,
        id
    }
}

// thunk
export const getAllRecipesThunk = () => async (dispatch) => {
    const response = await fetch('/api/recipes/')
    if (response.ok) {
        const data = await response.json()
        dispatch(getRecipes(data));
    };
}

export const addRecipeThunk = (recipe) => async (dispatch) => {
    const response = await fetch('/api/recipes', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(recipe)
    })

    if (response.ok) {
        const newRecipe = await response.json()
        await dispatch(addRecipe(newRecipe));
        return newRecipe;
    };
}

export const editRecipeThunk = (recipe) => async (dispatch) => {
    const response = await fetch(`/api/recipes/${recipe.id}`, {
        method: 'PUT',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(recipe)
    })

    if (response.ok) {
        const updatedRecipe = await response.json();
        await dispatch(editRecipe(updatedRecipe));
        return updatedRecipe;
    };
}

export const deleteRecipeThunk = (id) => async (dispatch) => {
    const response = await fetch(`/api/recipes/${id}`, {
        method: 'DELETE'
    })

    if (response.ok) {
        const removeRecipe = await response.json();
        await dispatch(deleteRecipe(id));
        return removeRecipe;
    };
}

// reducer
const initialState = {}
export default function recipeReducer(state = initialState, action) {
    let newState = {...state}
    switch(action.type){
        case LOAD_RECIPES: 
            newState = {};
            action.recipes.recipes.forEach(recipe => {
                newState[recipe.id] = recipe;
            });
            return newState;
        
        case ADD_RECIPE: 
            newState = {
                ...state,
                [action.recipe.id]: action.recipe
            };
            return newState;
        
        case EDIT_RECIPE: {
            newState = {
                ...state,
                [action.recipe.id]: action.recipe
            };
            return newState;
        }
        case DELETE_RECIPE: {
            delete newState[action.id];
            return newState;
        }

        default:
            return state;
    }
}


