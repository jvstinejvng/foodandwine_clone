import { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'

import { getRecipesThunk } from '../../store/recipe'
import RecipeCard from './RecipeCard'
import CreateRecipe from './CreateRecipe'

import '../CSS/UserRecipes.css'

function UserRecipes() {
    
    const dispatch = useDispatch()
    const recipes = useSelector(state => state.recipes)
    const sessionUser = useSelector(state => state.session.user)

    const [myRecipesState, setMyRecipesState] = useState(1)


    let sorted_recipes
    if (recipes && sessionUser) {
        let my_recipes = Object.values(recipes).filter(recipe => {
            return recipe.user.id === sessionUser.id
        })
        sorted_recipes = my_recipes.sort(((a, b) => b.id - a.id))
    }

      useEffect(() => {
        const fetchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        fetchRecipes().catch(console.error)
    }, [dispatch])


    return (
        <div className='UserRecipeDiv'>
            <h1>My Recipes</h1>
            <div className='UserRecipeContainer'>
            {sessionUser &&
                <div className='UserRecipeCards'>
                    {sorted_recipes && sorted_recipes.length > 0 ?
                        Object.values(sorted_recipes).map(recipe => (
                            <RecipeCard key={recipe.id} recipe={recipe} />
                        ))
                    :
                    <h3 className='UserRecipeNoRecide'>You have no recipes</h3>
                    }
                </div>
            }
            </div>
        </div>
    )
}

export default UserRecipes
