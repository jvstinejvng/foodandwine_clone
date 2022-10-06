import { useState, useRef } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useHistory, useParams } from 'react-router-dom'

import { deleteRecipeThunk } from '../../store/recipe'
import EditRecipe from './EditRecipe'
import ReviewContainer from '../Reviews/ReviewContainer'

import '../CSS/RecipePage.css'

function RecipePage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const { id } = useParams()
    const sessionUser = useSelector(state => state.session.user)
    const recipe = useSelector(state => state.recipes[id])
    
    const reviewRef = useRef()

    const [showEdit, setShowEdit] = useState(false)

    const rating_average = (recipe) => {
        let sum = 0
        recipe.comments.forEach(comment => {
            sum += comment.rating
        })
        return Math.round(sum/recipe.comments.length * 10) / 10
    }

    const handleDelete = async(e) => {
        e.preventDefault()

        try {
            await dispatch(deleteRecipeThunk(recipe))
            history.push('/my-recipes')

        } catch (e) {
            return window.alert('Fail to delete. Try again!')
        }
    }

    return (
        <div className='RecipePageContainer' >
            <div className='RecipePageDiv'>
                {recipe ?
                    <>
                    <div className='RecipePageHeader'>
                            <h1 className='RecipePageHeaderText'>{recipe.title}</h1>
                        <div className='RecipePageAverageRatingDiv'>
                                <div className='RecipePageAverageRating'>
                                    {isNaN(rating_average(recipe)) ?
                                        <div className='RecipePageReviwNumer'> 0/5 ({recipe.comments.length} reviews)</div>
                                        :
                                        <div className='RecipePageReviwNumer' >{rating_average(recipe)}/5 ({recipe.comments.length} reviews)</div>
                                    }
                                </div>
                        </div>
                    <p className='RecipePageDescription'>{recipe.description}</p>
                        <div className='RecipePageUser'>
                            <div className='RecipePageUserName'>by {recipe.user.username}</div>
                                {recipe.created_at === recipe.updated_at ?
                                    <span className='RecipePageCreateAt'>Published on {recipe.created_at.split(' ').slice(1, 4).join(' ')}</span>
                                    :
                                    <span className='RecipePageCreateAt'>Updated on {recipe.updated_at.split(' ').slice(1, 4).join(' ')}</span>
                                }
                        </div>
                    </div>
                {!showEdit ?
                        <div className='RecipePageRecipeCard'>
                            {sessionUser && sessionUser.id === recipe.user.id &&
                                    <div className='RecipePageRecipeCardButton'>
                                        <button className='RecipePageRecipeCardEdit' onClick={() => setShowEdit(!showEdit)} title='Edit Recipe'>Edit</button>
                                        <button className='RecipePageRecipeCardDelete' onClick={handleDelete} title='Delete Recipe'>Delete</button>
                                    </div>
                            }
                        <div className='RecipePageImageDiv'>
                                <img src={recipe.image_url} onError={({ currentTarget }) => {
                                        currentTarget.onerror = null;
                                        // currentTarget.src ='../../../../../static/default-bread.jpg'
                                }} alt={`recipe-${recipe.id}`} />
                        </div>
                        <div>
                                <div className='RecipePageIngredients'>Ingredients</div>     
                                    {recipe.description}
                                </div>
                        </div>
                    :
                        <div>
                            <EditRecipe
                                recipe={recipe}
                                setShowEditForm={setShowEdit}
                                />
                    </div>
                }
                <div className='ReviewContainer' ref={reviewRef}>Reviews</div>
                    <ReviewContainer recipe={recipe} />
                </>
                :
                <div className="404Page">This recipe was sent back to the kitchen!</div>
                
            }
        </div>
        </div>
    )
}

export default RecipePage