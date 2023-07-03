import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import RecipeCard from './RecipeCard'
import { getRecipesThunk } from '../../store/recipe'
import '../CSS/AllRecipes.css'

function AllRecipes() {

    const dispatch = useDispatch()
    const recipes = useSelector(state => state.recipes)
   
    useEffect(() => {
        const searchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        searchRecipes().catch(console.error)
    }, [dispatch])

    let recipes_order
    if (recipes) {
        recipes_order = Object.values(recipes).sort((a, b) => a.id > b.id ? -1 : 1)
    }

    if (!recipes) return null;

    return (
        <>
        <div className='AllRecipeContainer'>
            <div  className='AllRecipeHeader'>
                <h1 className='AllRecipeHeaderText'>All Recipes</h1>
                <p className="AllRecipeSubText">Let us break bread: recipes that bring us together. Embracing the flavors of life while making time for what matters. Like butter spread on bread, spread love, joy, and laughter.</p>
            </div>
            <div className='AllRecipeCardContainer'>
                <div className='AllRecipeCardGrid'>
                    {recipes_order &&
                        Object.values(recipes_order).map(recipe => (
                        <RecipeCard  key={recipe.id} recipe={recipe} />
                    ))}
                </div>
            </div>
        </div>
        </>
    )
}

export default AllRecipes
