import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useHistory } from 'react-router-dom'
import { getOneRecipeThunk, deleteRecipeThunk } from "../../store/recipes";
import '../CSS/SingleRecipe.css'

function RecipePage(){

    const dispatch = useDispatch();
    const history = useHistory();
    const sessionUser = useSelector(state => state.session.user);


    const { id } = useParams();
    const recipe = useSelector(state => state.recipes)[id];

    useEffect(() => {
        dispatch(getOneRecipeThunk(id));
    }, [dispatch, id]);

    let ingredients_list
    if(recipe) {
        ingredients_list = JSON.stringify(recipe.ingredients).split(',').slice(1,-1)
    }

    let directions_step
    if(recipe) {
        directions_step = JSON.stringify(recipe.directions).split('.').slice(1,-1)
    }

    const handleDelete = async e => {
        e.preventDefault();
        await dispatch(deleteRecipeThunk(recipe.id));
        history.push(`/`);
    }


    return (
        <div className='SingleRecipeContainer'>
            <div className='SingleRecipeDiv'>
                <h1 className='SingleRecipeHeader'>{recipe.title}</h1>
            </div>
            {sessionUser?.id === recipe.user_id && 
                <button 
                    className="SingleRecipeDelete" 
                     onClick={handleDelete}
                >Delete Recipe
                </button>}
            <div className='SingleRecipeSubHeader'>
                <p className='SingleRecipeDescription'>{recipe.description}</p>
                <span className='SingleRecipeBy'>By </span>
                <span className='SingleRecipeUser'>{recipe.user.first_name} {recipe.user.last_name}</span>
            </div> 
            <div className='SingleRecipeImage'>
                <img className='SingleRecipeImageImg' src={recipe.img_url}/>
            </div>
            <div className='SingleRecipeTimeServing'>
                <div className='TimeServingDiv'>
                   <h3 className='TimeServingHeader'>Total Time:</h3> 
                    {recipe.total_time}
                </div>
                <div className='TimeServingDiv'>
                    <h3 className='TimeServingHeader'>Servings:</h3> 
                    {recipe.servings}
                </div>
            </div>
            <div className='SingleRecipeIngredients'>
                <h2 className='SingleRecipeIngredientHeader'>Ingredients</h2>
                <ul>
                {ingredients_list.map((ingredient)=>
                 <li className='SingleRecipeIngredientList'>
                    {ingredient}
                 </li>
                )} 
                </ul>
            </div>    
            <div className='SingleRecipeDirections'>
                <h2 className='SingleRecipeDirectionsHeader'>Directions</h2>
                <ol>
                {directions_step.map((steps)=>
                 <li className='SingleRecipeDirectionsList' >
                    {steps}
                 </li>
                )} 
                </ol>
            </div>  
        </div>
    )

}

export default RecipePage