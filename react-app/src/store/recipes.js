// action
const LOAD_RECIPES = 'recipes/LOAD_RECIPES'
const LOAD_ONE_RECIPE = 'recipes/LOAD_ONE_RECIPE'
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

const getOneRecipe = recipe => ({
    type: LOAD_ONE_RECIPE,
    recipe
});

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
export const getAllRecipesThunk = () => async dispatch => {
    const response = await fetch('/api/recipes/')
    if (response.ok) {
        const data = await response.json()
        dispatch(getRecipes(data));
    };
}

export const getOneRecipeThunk = (id) => async dispatch => {
    const response = await fetch(`/api/recipes/${id}/`);
    if (response.ok) {
        const recipe = await response.json();
        dispatch(getOneRecipe(recipe));
    };
};

export const addRecipeThunk = (recipe) => async dispatch => {
    const response = await fetch('/api/new-recipe/', {
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

export const editRecipeThunk = (recipe) => async dispatch => {
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
    switch(action.type){
        case LOAD_RECIPES: {
            const newState = {};
            action.recipes.recipes.forEach(recipe => {
            newState[recipe.id] = recipe;
            });
            return newState;
        }
        case LOAD_ONE_RECIPE: {
            const newState = {};
            newState[action.recipe.id] = action.recipe;
            return newState;
            };
        case ADD_RECIPE: {
            const newState = { ...state };
            newState[action.recipe.id] = action.recipe;
            return newState;
        }  
        case EDIT_RECIPE: {
            return {
                ...state,
                [action.recipe.id]: action.recipe
            }
        }
        case DELETE_RECIPE: {
            const newState = { ...state };
            delete newState[action.recipeId];
            return newState;
        }
        default:
            return state;
    }
}


