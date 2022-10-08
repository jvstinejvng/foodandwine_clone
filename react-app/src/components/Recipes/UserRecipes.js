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


    let recipe_sort
    if (recipes && sessionUser) {
        let my_recipes = Object.values(recipes).filter(recipe => {
            return recipe.user.id === sessionUser.id
        })
        recipe_sort = my_recipes.sort(((a, b) => b.id - a.id))
    }

      useEffect(() => {
        const fetchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        fetchRecipes().catch(console.error)
    }, [dispatch])

    return (
        <div className='UserRecipeDiv'>
                <div className='UserRecipeHeaderDiv' >
                    <h1 className='UserRecipeHeaderText'>Personal Recipes</h1>
                        <p className="UserRecipeSubText">Recipes you have created on Bread & Butter.</p>
                </div>
            <div className='UserRecipeContainer'>
                    {sessionUser &&
                        <div className='UserRecipeCardGrid'>
                            {recipe_sort && recipe_sort.length > 0 ?
                                Object.values(recipe_sort).map(recipe => (
                                    <RecipeCard key={recipe.id} recipe={recipe} />
                            ))
                            :
                            <h3 className='UserRecipeNoRecipe'>You have no recipes</h3>
                            }
                </div>
            }
            </div>
        
        </div>
    )
}

export default UserRecipes
