import { useEffect } from 'react'
import { useDispatch, useSelector} from 'react-redux'
import { NavLink } from 'react-router-dom';
import { getAllRecipesThunk } from '../store/recipes'
import './CSS/Homepage.css'

function Homepage() {
    const dispatch = useDispatch()
    const recipes = useSelector(state => Object.values(state.recipes).slice(0, 3))


    useEffect(() => {
        dispatch(getAllRecipesThunk())
    }, [dispatch])

    if (!recipes) return null;

    return (
     <>
        <div className='HomepageMainDiv'>
            <div className='HomepageTopHalf'>
                <div className='HomepageMainRecipe-RightDiv'>

                </div>
                <div className='HomepageDevelopersPanel'>

                </div>
            </div>
            <div className='HomepageMiddleRecipe'>

            </div>
            <div className='HomepageBottomHalf'>
            <div className="HomepageRecipeCardGrid"> 
                { recipes &&
                    recipes?.map((recipe) => (
                  <div className='HomepageRecipeCardDiv' key={recipe.id}>
                        <NavLink className="HomepageRecipeCardLink" to={`/recipes/${recipe.id}`}>
                            <div className="HomepageRecipeCard">
                            <div className='HomepageRecipeCardImg'>
                                <img className="HomepageRecipeCarmImgUrl" src={recipe.image_url} alt={`${recipe.title} Recipe`} />
                            </div>
                            <div className='HomepageRecipeCardText'>
                                <div className='HomepageRecipeCardTitle'>{recipe.title}</div>
                                <div className='HomepageRecipeCardTime'>{recipe.total_time}</div>   
                                <div className='HomepageRecipeCardUser'>By {recipe.user.first_name}</div>
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

export default Homepage
