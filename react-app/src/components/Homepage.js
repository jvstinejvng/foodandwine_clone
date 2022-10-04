import { useEffect } from 'react'
import { useDispatch, useSelector} from 'react-redux'
import { NavLink } from 'react-router-dom';
import { getAllRecipesThunk } from '../store/recipes'
import './CSS/AllRecipes.css'

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
                <p className="BreakBreadText">Let us break bread: recipes that bring us together.</p>
                <span className="BreakBreadSubText">Embracing the flavors of life while making time for what matters. Like butter spread on bread, spread love, joy, and laughter.</span>
            </div>
            <div className='AllRecipeCardContainer'>
                <div className="AllRecipeCardGrid">
                {recipes?.map((recipe) => (
                    <div className='RecipeContainer' key={recipe.id}>
                        <NavLink to={`/recipes/${recipe.id}`}>
                            <div className="RecipeCard">
                            <div className='RecipeCardImageContainer'>
                                <img className="RecipeCardImage" src={recipe.image_url} alt={`${recipe.title} Recipe`} />
                            </div>
                            <div className='RecipeCardText'>
                                <h3>{recipe.title}</h3>
                                <p>{recipe.total_time}</p>   
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
