import { NavLink } from "react-router-dom"
import { useSelector } from "react-redux"
import RecipeCard from './RecipeCard.js'

import '../CSS/SavedRecipe.css'

function AllSavedRecipes() {

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
            <div className="SaveRecipeSubText">All Saved Recipes</div>
            <div className='SaveRecipeCardGrid'>
                {saved_recipes && saved_recipes.length > 0 &&
                    Object.values(saved_recipes).map(recipe => (
                        <RecipeCard key={recipe.id} recipe={recipe} />
                    ))
                }
            </div>
            <div className='NoRecipes'>
                {saved_recipes.length === 0 && 
                   <p>You don't have anything saved yet. Get cooking!</p>
                }
            </div>

            <div>
                {saved_recipes && saved_recipes.length > 0 ? 
                    <div className='HungryForMore'><span className='HungryForMoreText'>Hungry for More?</span>
                    <NavLink  to='/recipes'><button className="FindRecipeButton">Find More Recipes</button></NavLink> 
                    </div>
                     :
                     <div>
                     <NavLink  to='/recipes'><button className="FindRecipeButton">Find Recipes</button></NavLink> 
                    </div>
                }
            </div>     
        </div>
    )
}

export default AllSavedRecipes
