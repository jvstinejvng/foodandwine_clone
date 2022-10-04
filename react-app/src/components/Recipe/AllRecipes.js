import { useEffect } from 'react'
import { useDispatch, useSelector} from 'react-redux'
import { NavLink } from 'react-router-dom';
import { getAllRecipesThunk } from '../../store/recipes'
import '../CSS/AllRecipes.css'

function AllRecipes() {
    const dispatch = useDispatch()
    const recipes = Object.values(useSelector(state => state.recipes));

    useEffect(() => {
        dispatch(getAllRecipesThunk())
    }, [dispatch])

    if (!recipes) return null;

    return (
     <>
        <div className='AllRecipeContainer'>
            <div className='AllRecipeHeader'>
                <h1 className='RecipeText'>Recipes</h1>
                <p className="BreakBreadText">Let us break bread: recipes that bring us together. Embracing the flavors of life while making time for what matters. Like butter spread on bread, spread love, joy, and laughter.</p>
            </div>
            <div className='AllRecipeCardContainer'>
                <div className="AllRecipeCardGrid">
                {recipes?.map((recipe) => (
                    <div className='RecipeContainer' key={recipe.id}>
                        <NavLink className="AllRecipeNavLink" to={`/recipes/${recipe.id}`}>
                            <div className="RecipeCard">
                            <div className='RecipeCardImageContainer'>
                                <img className="RecipeCardImage" src={recipe.img_url} alt={`${recipe.title} Recipe`} />
                            </div>
                            <div className='RecipeCardText'>
                                <div className='RecipeCardTitle'>{recipe.title}</div>
                                <div className='RecipeCardTime'>{recipe.total_time}</div>   
                                <div className='RecipeCardUser'>By {recipe.user.first_name}</div>
                            </div>
                            </div>
                        </NavLink>
                    </div>
                ))}
                </div>
            </div>
        </div> 
     </>
    )
}

export default AllRecipes
