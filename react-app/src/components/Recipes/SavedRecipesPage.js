import { useEffect, useState } from "react"
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
        <div className='AllRecipeContainer'>
            {saved_recipes && saved_recipes.length > 0 ?
                Object.values(saved_recipes).map(recipe => (
                    <RecipeCard key={recipe.id} recipe={recipe} />
            ))
            :
            <h3 id='NoRecipes'>You haven't saved any recipes, yet</h3>
            }
        </div>
    )
}

export default AllSavedRecipes
