import { useState, useRef } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useHistory, useParams, NavLink } from 'react-router-dom'
import { FaStar } from 'react-icons/fa'
import NotFound from '../NotFound.js'

import { deleteRecipeThunk } from '../../store/recipe'
import EditRecipe from './EditRecipe'
import ReviewContainer from '../Reviews/ReviewContainer'

import '../CSS/RecipePage.css'

function RecipePage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const { id } = useParams()
    const scrollToReview = useRef()

    const sessionUser = useSelector(state => state.session.user)
    const recipe = useSelector(state => state.recipes[id])

    const [showEdit, setShowEdit] = useState(false)

    const average_rating = (recipe) => {
        let sum = 0
        recipe.comments.forEach(comment => { sum += comment.rating })
        return Math.round(sum/recipe.comments.length * 10) / 10
    }

    let ingredients_list
        if(recipe) { ingredients_list = (recipe.ingredients).split(',').slice(0,-1)}

    let directions_step
        if(recipe) { directions_step = (recipe.directions).split('.').slice(0,-1)}

    const handleDelete = async(e) => {

        e.preventDefault()

        try {
            await dispatch(deleteRecipeThunk(recipe))
            history.push('/my-recipes')
        } catch (e) {
            return window.alert('Fail to delete. Please Try Again')
        }
    }

    return (
        <div className='RecipePageContainer' >
        <div className='RecipePageDiv'>
            {recipe &&
                <>
                <div className='RecipePageHeader'>
                <h1 className='RecipePageHeaderText'>{recipe.title}</h1>
                    <div className='RecipePageAverageRatingDiv'>
                        <div className='RecipePageAverageRating'>
                            {isNaN(average_rating(recipe)) ?
                                <div className='RecipePageNoReview'
                                    onClick={() => scrollToReview.current.scrollIntoView({ behavior: 'smooth' })}>
                                    Be the first to rate & review!
                                </div>
                                :
                                <div className='RecipePageWithReview'>
                                    {average_rating(recipe)}
                                    <span><FaStar/></span>
                                    <span className='RecipePageDividerChar'> | </span>
                                    {recipe.comments.length} reviews 
                                </div>
                            }
                        </div>
                    </div>
                    <p className='RecipePageDescription'>{recipe.description}</p>
                    <div className='RecipePageUser'>
                        By <div className='RecipePageUserName'>{recipe.user.first_name} {recipe.user.last_name}</div>
                        <span className='RecipePageDividerChar2'> | </span>
                            {recipe.created_at === recipe.updated_at ?
                                <span className='RecipePageCreateAt'>Published on {recipe.created_at.split(' ').slice(1, 4).join(' ')}</span>
                                :
                                <span className='RecipePageCreateAt'>Updated on {recipe.updated_at.split(' ').slice(1, 4).join(' ')}</span>
                            }
                    </div>
                    </div>
                    <div className='RecipePageBody'>
                        {!showEdit ?
                            <div className='RecipePageRecipeCard'>
                                { sessionUser && sessionUser.id === recipe.user.id &&
                                    <div className='RecipePageRecipeCardButtonDiv'>
                                        <button className='RecipePageRecipeCardButton' onClick={() => setShowEdit(!showEdit)} title='Edit Recipe'>Edit</button>
                                        <button className='RecipePageRecipeCardButton' onClick={handleDelete} title='Delete Recipe'>Delete</button>
                                    </div>
                                }
                            <div className='RecipePageImageDiv'>
                                    <img className='RecipePageImage' src={recipe.image_url} onError={({ currentTarget }) => {
                                            currentTarget.onerror = null;
                                            currentTarget.src ='../../../../../static/buttertoast.png'
                                    }} alt={`recipe-${recipe.id}`} />
                            </div>
                            <div className='RecipePageServing'>
                                <div className='TimeServingDiv'>
                                    <div className='TimeServingHeader'>Total Time:</div>{recipe?.total_time}</div>
                                <div className='TimeServingDiv'>
                                    <div className='TimeServingHeader'>Yield:</div>{recipe?.servings}</div>
                            </div>
                            <div className='RecipePageIngredientsDirections'>
                                <div className='RecipePageIngredients'>Ingredients</div>     
                                    <ul className='RecipeIngredientList'>
                                        { ingredients_list?.map((ingredient)=>
                                            <li  key={ingredient} className='RecipePageIngredientsText'> {ingredient} </li>
                                        )} 
                                        </ul>
                                <div className='RecipePageDirections'>Directions</div>
                                    <ol className='RecipePageDirectionContainer'>
                                        { directions_step?.map((steps)=> 
                                            <li key={steps} className='RecipePageDirectionsStep' >
                                               <div className='RecipePageEachStep'>{steps}. </div> 
                                            </li >
                                        )} 
                                    </ol>
                                </div>
                            </div>
                            :
                            <div className='RecipePageEditRecipe'>
                                <EditRecipe
                                    recipe={recipe}
                                    setShowEditForm={setShowEdit}
                                />
                            </div>
                        }
                    </div>
                    <div className='ScrollToReview' ref={scrollToReview}></div>
                    <div className='RecipePageBottom'>
                        <ReviewContainer recipe={recipe} />
                    </div>
                </>    
            }                         
            </div>
        </div>
    )
}

export default RecipePage
