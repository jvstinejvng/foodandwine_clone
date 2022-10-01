import { useEffect } from 'react'
import { useDispatch, useSelector} from 'react-redux'
import { NavLink } from 'react-router-dom';
import { getAllRecipesThunk } from '../../store/recipes'


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
                <p>Let us break bread: recipes that bring us together.</p>
                <span>Embracing the flavors of life while making time for what matters. Like butter spread on bread, spread love, joy, and laughter.</span>
            </div>
            <div className='AllRecipeCardContainer'>
                {recipes?.map((recipe) => (
                    <div key={recipe.id}>
                        <NavLink to={`/recipes/${recipe.id}`}>
                            <div>
                            <img src={recipe.img_url} alt='cover' />
                            </div>
                            <div>
                                <h3>{recipe.title}</h3>
                                <p>{recipe.total_time}</p>   
                            </div>
                        </NavLink>
                    </div>
                ))}
            </div>
        </div>
       
     </>
    )
}

export default AllRecipes
