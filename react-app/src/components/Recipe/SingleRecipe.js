import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useParams, useHistory } from 'react-router-dom'
import { getOneRecipeThunk, deleteRecipeThunk } from "../../store/recipes";
import { getAllReviewsThunk } from '../../store/reviews'
import Review from '../Review/Review'
import '../CSS/SingleRecipe.css'

function RecipePage(){

    const dispatch = useDispatch();
    const history = useHistory();
    const currentUser = useSelector((state) => (state?.session?.user))
    const [dropToggle, setDropToggle] = useState(false)

    const { id } = useParams();
    const recipe = useSelector(state => state.recipes)[id];
    const booksArray = useSelector((state) => Object.values(state?.recipes))

    const reviewsArray = useSelector((state) => Object.values(state?.reviews))
    const reviewsByBookId = reviewsArray.filter(review => review.recipe_id === Number(id))
    const [display, setDisplay] = useState('landing')

    const bookIdArray = []
    booksArray.map((recipes) => bookIdArray.push(recipes.id))
    console.log(bookIdArray.includes(Number(id)), 'TRUE OR FALSE>>')

    useEffect(() => {
        dispatch(getOneRecipeThunk())
        dispatch(getAllReviewsThunk())
    }, [dispatch])

    let allStarRatings = [];
    reviewsByBookId.forEach((review) => allStarRatings.push(review.stars))
    const allStarsSum = allStarRatings.reduce((prev, curr) => prev + curr, 0);
    let avgStarRating = parseFloat(allStarsSum / allStarRatings.length)

    const currentUserId = currentUser.id
    const reviewOfCurrentUser = reviewsByBookId.filter(review => review.user_id == currentUserId)
    const currentUserRating = reviewOfCurrentUser[0]?.stars

    function currentUserStarRating() {
        if (currentUserRating > 0) {
            return (
                <div className='SingleRecipeRating'>Your Rating: {currentUserRating}/5</div>
            )
        }
    }


    let ingredients_list
    if(recipe) {
        ingredients_list = (recipe.ingredients).split(',').slice(0,-1)
    }

    let directions_step
    if(recipe) {
        directions_step = (recipe.directions).split('.').slice(0,-1)
    }


    const handleDelete = async e => {
        e.preventDefault();
        await dispatch(deleteRecipeThunk(recipe.id));
        history.push(`/`);
    }


    return (
        <div className='SingleRecipeContainer'>
            <div className='SingleRecipeDiv'>
                <h1 className='SingleRecipeHeader'>{recipe?.title}</h1>
            </div>
            {currentUser?.id === recipe?.user_id && 
                <button 
                    className="SingleRecipeDelete" 
                     onClick={handleDelete}
                >Delete Recipe
                </button>}
            <div className='SingleRecipeSubHeader'>
                <p className='SingleRecipeDescription'>{recipe?.description}</p>
                <span className='SingleRecipeBy'>By </span>
                <span className='SingleRecipeUser'>{recipe?.user.first_name} {recipe?.user.last_name}</span>
            </div> 
            <div className='SingleRecipeImage'>
                <img className='SingleRecipeImageImg' src={recipe?.image_url}/>
            </div>
            <div className='SingleRecipeTimeServing'>
                <div className='TimeServingDiv'>
                   <h3 className='TimeServingHeader'>Total Time:</h3> 
                    {recipe?.total_time}
                </div>
                <div className='TimeServingDiv'>
                    <h3 className='TimeServingHeader'>Servings:</h3> 
                    {recipe?.servings}
                </div>
            </div>
            <div className='SingleRecipeIngredients'>
                <h2 className='SingleRecipeIngredientHeader'>Ingredients</h2>
                <ul>
                {ingredients_list?.map((ingredient)=>
                 <li className='SingleRecipeIngredientList'>
                    {ingredient}
                 </li>
                )} 
                </ul>
            </div>    
            <div className='SingleRecipeDirections'>
                <h2 className='SingleRecipeDirectionsHeader'>Directions</h2>
                <ol>
                {directions_step?.map((steps)=>
                 <li className='SingleRecipeDirectionsList' >
                    {steps}.
                 </li>
                )} 
                </ol>
            </div>  
            <div>
            {reviewsByBookId.length > 0 ? (
                <div>
                  <div className="alex_merriweather_300 alex_font_16">
                    Average Rating: {avgStarRating.toFixed(2)}/5
                  </div>
                  <div className="alex_merriweather_300 alex_font_16">
                    {currentUserStarRating()}
                  </div>
                </div>
              ) : (
                <div className="alex_merriweather_300 alex_font_14">
                  This book hasn't been rated yet
                </div>
              )}

            <Review
                display={display}
                setDisplay={setDisplay}
                dropToggle={dropToggle}
                setDropToggle={setDropToggle}
              />
        
            </div>
            <div>
            </div>
        </div>
    )

}

export default RecipePage