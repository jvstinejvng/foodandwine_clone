import { useEffect, useState } from "react"
import { NavLink } from "react-router-dom"
import { useDispatch, useSelector } from "react-redux"
import RecipeCard from './RecipeCard.js'

import '../CSS/SavedRecipe.css'

function AllSavedRecipes() {

    const dispatch = useDispatch()
    const recipes = useSelector(state => state.recipes)
    const sessionUser = useSelector(state => state.session.user)

    let user_id
    if (sessionUser) { user_id = sessionUser.id }

    let saved_recipes = []
    if (recipes && sessionUser) {
        for (let recipe of Object.values(recipes)) {
            for (let save of recipe.saves) {
                if(save.id === sessionUser.id) { saved_recipes.push(recipe) }
            }
        }
    }

    return (
        <div className='SaveRecipeGridDiv'>
             <p className="SaveRecipeSubText">All Saved Recipes</p>
                <div className='SaveRecipeCardGrid'>
                    {saved_recipes && saved_recipes.length > 0 ?
                    Object.values(saved_recipes).map(recipe => (
                        <RecipeCard key={recipe.id} recipe={recipe} />
                    ))
                    :
                    <h3 id='NoRecipes'>You don't have anything saved yet. Get cooking!</h3>
                    }
                </div>
                <div>
                    Hungry for More?
                        <NavLink  to='/recipes'>
                             <button>Find More Recipes</button>
                        </NavLink>
                </div>
        </div>
    )
}

export default AllSavedRecipes
