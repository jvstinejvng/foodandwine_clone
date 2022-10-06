import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom';

import RecipeCard from  './Recipes/RecipeCard'
import { getRecipesThunk } from '../store/recipe'

import './CSS/Homepage.css'

function Homepage() {
    const dispatch = useDispatch()
    const recipes = useSelector(state => Object.values(state.recipes).slice(0, 4))
    // const sessionUser = useSelector(state => state.session.user)

    useEffect(() => {
        const fetchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        fetchRecipes().catch(console.error)
    }, [dispatch])

    return (
        <div className='HomepageContainer'>
            <div className='HomepageMainRecipe'>
            </div>
            <div className='HomepageSecondRecipeBanner'>
            </div>
            <div className='HomepageTrioRecipe'>
                <NavLink className="HomepageCookingLink" to='/recipes'>
                <h2 className='HomepageCooking'>Cooking ➝</h2>
                </NavLink>
                        <div className='HomepageCookingRecipeDiv'>
                            {recipes && (
                                recipes.map(recipe => (
                                        <RecipeCard key={recipe.id} recipe={recipe} />
                            ))
                            )}
                        </div>
            </div>
            <div>
            </div>
        </div>
    )
}

export default Homepage
