
const GET_RECIPES = 'recipes/GET_RECIPES'
const POST_RECIPE = 'recipes/POST_RECIPE'
const EDIT_RECIPE = 'recipes/EDIT_RECIPE'
const DELETE_RECIPE ='recipes/DELETE_RECIPE'

const getRecipes = (recipes) => {
    return {
        type: GET_RECIPES,
        recipes
    }
}

const postRecipe = (recipe) => {
    return {
        type: POST_RECIPE,
        recipe
    }
}

const editRecipe = (recipe) => {
    return {
        type: EDIT_RECIPE,
        recipe
    }
}

const deleteRecipe = (recipe) => {
    return {
        type: DELETE_RECIPE,
        recipe
    }
}

export const getRecipesThunk = () => async (dispatch) => {
    const res = await fetch('/api/recipes')
    if (res.ok) {
        const data = await res.json()
        dispatch(getRecipes(data.recipes))
    } else {
        const error = await res.json()
        throw error
    }
}

export const postRecipeThunk = (recipe) => async (dispatch) => {
    const response = await fetch('/api/recipes', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(recipe)
    })

    if (response.ok) {
        const data = await response.json()

        if (data.errors) {
            return
        }
        dispatch(postRecipe(data))
        return data
    }
}

// hello

export const editRecipeThunk = (recipe) => async (dispatch) => {
    console.log(recipe)
    const response = await fetch(`/api/recipes/${recipe.id}`, {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(recipe)
    })

    if (response.ok) {
        const data = await response.json()
        await dispatch(editRecipe(data))

        return data
    } 
}

export const deleteRecipeThunk = (recipe) => async (dispatch) => {
    const res = await fetch(`/api/recipes/${recipe.id}`, {
        method: 'DELETE'
    })

    if (res.ok) {
        const data = await res.json()
        if (data.message === "Recipe Deleted!") {
            dispatch(deleteRecipe(recipe))
        }
        return recipe
    } else {
        const error = await res.json()
        throw error
    }
}

//Reducer
let initialState = {}
export default function recipe_reducer(state = initialState, action) {
    let newState = {}
    switch(action.type){
        case GET_RECIPES:
            newState = { ...state }
            action.recipes.forEach(recipe => newState[recipe.id] = recipe)
            return newState
        case POST_RECIPE:
            newState = { ...state }
            newState[action.recipe.id] = action.recipe
            return newState
        case EDIT_RECIPE:
            newState = { ...state };
            newState[action.recipe.id] = action.recipe
            return newState
        case DELETE_RECIPE:
            newState = { ...state }
            delete newState[action.recipe.id]
            return newState
        default:
            return state;
    }
}
