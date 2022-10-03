import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams } from 'react-router-dom'
import { getOneRecipeThunk } from "../../store/recipes";


function RecipePage(){

    const dispatch = useDispatch();

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

    console.log("THIS IS AN ARRAY", JSON.stringify(recipe.directions))

    return (
        <div className='SingleRecipeContainer'>
            <div className='SingleRecipeContainer'>
                <h1 className='SingleRecipeHeader'>{recipe.title}</h1>
            </div>
            <div className='SingleRecipeSubHeader'>
                <p>{recipe.description}</p>
                <span>By</span>
                <span>{recipe.user.first_name} {recipe.user.last_name}</span>
            </div> 
            <div className='SingleRecipeImage'>
                <img className='recipe-image' src={recipe.img_url}/>
            </div>
            <div className='SingleRecipeTimeServing'>
                <div>
                   <p>Total Time:</p> 
                    {recipe.total_time}
                </div>
                <div>
                    <p>Servings:</p> 
                    {recipe.servings}
                </div>
            </div>
            <div className='SingleRecipeIngredients'>
                <h3>Ingredients</h3>
                <ul>
                {ingredients_list.map((ingredient)=>
                 <li>
                    {ingredient}
                 </li>
                )} 
                </ul>
            </div>    
            <div className='SingleRecipeDirections'>
                <h3>Directions</h3>
                <ol>
                {directions_step.map((steps)=>
                 <li>
                    {steps}
                 </li>
                )} 
                </ol>
            </div>  
        </div>
    )

}

export default RecipePage