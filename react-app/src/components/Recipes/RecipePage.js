import { useEffect,useState, useRef } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { useHistory, useParams } from 'react-router-dom'

import { FaStar } from 'react-icons/fa'
import { deleteRecipeThunk } from '../../store/recipe'
import EditRecipe from './EditRecipe'
import CreateIngredient from './CreateIngredient'
import CreateDirection from './CreateDirection'
import Ingredient from './Ingredient'
import Direction from './Direction'
import ReviewContainer from '../Reviews/ReviewContainer'
import SaveRecipe from './SaveRecipe'
import NotFound from '../NotFound.js'
import '../CSS/RecipePage.css'

function RecipePage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const { id } = useParams()
    const scrollToReview = useRef()
    const scrollToReviews = useRef()
    const scrollToRecipe = useRef()
    const sessionUser = useSelector(state => state.session.user)
    const recipe = useSelector(state => state.recipes[id])

    const [showEdit, setShowEdit] = useState(false)
    const [showAddIngredient, setShowAddIngredient] = useState(false)
    const [showAddDirection, setShowAddDirection] = useState(false)
    const [showEditIngredient, setShowEditIngredient] = useState(false)
    const [showEditDirection, setShowEditDirection] = useState(false)
    const [measurementUnits, setMeasurementUnits] = useState('')

    const average_rating = (recipe) => {
        let sum = 0
        recipe.comments.forEach(comment => { sum += comment.rating })
        return Math.round(sum/recipe.comments.length * 10) / 10
    }

    useEffect(() => {
        async function fetchUnits() {
            const res = await fetch('/api/recipes/units')
            const data = await res.json()
            setMeasurementUnits(data.units)
        }
        fetchUnits()
    }, [])

    let ingredient_list
    if (recipe) {
        ingredient_list = Object.values(recipe.ingredients).sort((a, b) => (a.id > b.id ? 1: -1))
    }

    let directional_step
    if (recipe) {
        directional_step = Object.values(recipe.instructions).sort((a, b) => (a.id > b.id ? 1: -1))
    }

    const handleDelete = async(e) => {
        e.preventDefault()

        try {
            await dispatch(deleteRecipeThunk(recipe))
            history.push('/my-recipes')
        } catch (e) {
            return window.alert('Fail to delete recipe. Please Try Again!')
        }
    }



    return (
    <div className='RecipePageContainer' >
    { recipe &&
        <>
        { !showEdit ?
            <div>
            <span className='RecipePageHeader'>
            <span className='RecipePageHeaderText'>{recipe.title}</span> 
            { sessionUser && sessionUser.id === recipe.user.id &&
                <span className='RecipePageEditDeleteDiv'>
                <span className='RecipePageEditDelete' onClick={() => setShowEdit(!showEdit)}>
                    <i class="fa-solid fa-pen-to-square"></i>
                    <span className='RecipePageIconText'>Edit</span>
                </span>
                <span className='RecipePageEditDelete' onClick={handleDelete}>
                    <i class="fa-solid fa-trash-can"></i>
                    <span className='RecipePageIconText'>Delete</span>
                </span>
                </span>    
            }
            </span>
            <div className='RecipePageSubHeaderDiv'>
            { isNaN(average_rating(recipe)) ?
                <div className='RecipePageReviewBox'>
                    <span className='RecipePageSubHeaderBar'onClick={() => scrollToReview.current.scrollIntoView({ behavior: 'smooth' })}>
                        Be the first to rate & review!
                    </span>
                    <span className='RecipePageDividerChar'> | </span>
                    <span onClick={() => scrollToRecipe.current.scrollIntoView({ behavior: 'smooth' })}> 
                    {recipe.ingredient} 
                    <span className='RecipePageRecipeScroll'>Scroll to Recipe</span>
                    </span>
                </div>
                :
                <div className='RecipePageReviewBox'>
                    <span><FaStar/></span>
                    <span className='RecipePageAverageRatingNumber'>{average_rating(recipe)}</span>
                    <span className='RecipePageDividerChar'> | </span>
                    <span className='RecipePageReviews' onClick={() => scrollToReviews.current.scrollIntoView({ behavior: 'smooth' })}>
                        {recipe.comments.length} reviews 
                    </span>
                    <span className='RecipePageDividerChar'> | </span>
                    <span onClick={() => scrollToRecipe.current.scrollIntoView({ behavior: 'smooth' })}> 
                        {recipe.ingredient} 
                        <span className='RecipePageRecipeScroll'>Scroll to Recipe</span>
                    </span>
                </div>      
            }        
            </div>
            <p className='RecipePageDescription'>{recipe.description}</p>
            <div className='RecipePageUser'>
                By <div className='RecipePageUserName'>{recipe.user.first_name} {recipe.user.last_name}</div>
                <span className='RecipePageDividerChar2'> | </span>
                { recipe.created_at === recipe.updated_at ?
                    <span className='RecipePageDate'>Published on {recipe.created_at.split(' ').slice(1, 4).join(' ')}</span>
                    :
                    <span className='RecipePageDate'>Updated on {recipe.updated_at.split(' ').slice(1, 4).join(' ')}</span>
                }
            </div>
            <div>
                <img className='RecipePageImage' src={recipe.image_url} onError={({ currentTarget }) => {
                    currentTarget.onerror = null;
                    currentTarget.src ='../../../../../static/breadbutterimage.png'
                }} alt={`recipe-${recipe.id}`} />
                <div ref={scrollToRecipe}></div>
                <div className='RecipePageServingDiv'>
                    <div className='TimeServingDiv'>
                    <div className='TimeServingHeader'>Total Time:</div>{recipe?.total_time}
                    </div>
                    <div className='TimeServingDiv'>
                        <div className='TimeServingHeader'>Yield:</div>{recipe?.servings}
                    </div>
                </div> 
            </div>
            </div>
            :
            <EditRecipe
                recipe={recipe}
                setShowEditForm={setShowEdit}
            />           
        }
        <>
        <span className='RecipeBodySpanBox'>
        <h2 className='RecipeIngredientHeader'>Ingredients</h2>
            { sessionUser && sessionUser.id === recipe.user.id &&
                <>
                { recipe.ingredients.length > 0 &&
                    <>
                    { showEditIngredient ?
                        <span className='RecipeBodyEdit' onClick={() => setShowEditIngredient(!showEditIngredient)} >
                            <i class="fa-solid fa-list-ul"></i>
                            <span className='RecipePageIconText'>Save</span>
                        </span>
                        : 
                        <span className='RecipeBodyEdit' onClick={() => setShowEditIngredient(!showEditIngredient)}>
                            <i class="fa-solid fa-pen-to-square"></i>
                            <span className='RecipePageIconText'>Edit</span>
                        </span>
                    }   
                    </>
                }
                </>
            }
        </span>
        <ul className='RecipeBodyList'>
            { ingredient_list.map(ingredient => (
                <li className='RecipeBodyText' key={ingredient.id}>
                    <Ingredient
                        ingredient={ingredient}
                        recipe={recipe}
                        showEditIngredient={showEditIngredient}
                        setshowEditIngredient={setShowEditIngredient}
                        measurementUnits={measurementUnits}
                    /> 
                </li>
            ))}
        </ul>
    
            { !sessionUser && recipe.id && !recipe.ingredients.length &&
             <div className='RecipeBodyEmpty'>The owner of this recipe has not yet added the ingredients to this recipe.</div>
            }
            {  sessionUser && sessionUser.id !== recipe.user.id && !recipe.ingredients.length &&
             <div className='RecipeBodyEmpty'>The owner of this recipe has not yet added the ingredients to this recipe.</div>
            }
            { sessionUser && sessionUser.id === recipe.user.id &&
                <div className=''>
                { recipe.ingredients.length > 0 &&
                    <>
                    { showAddIngredient &&
                        <CreateIngredient
                            recipe_id={recipe.id}
                            measurementUnits={measurementUnits}
                            edit={true}/>
                    }
                    { showAddIngredient ?
                        <button onClick={() => setShowAddIngredient(!showAddIngredient)} className=''>Save</button>
                        :
                        <button onClick={() => setShowAddIngredient(!showAddIngredient)} title='Add Ingredients'><i className="fa-solid fa-plus"></i>Add Ingredient</button>
                    }    
                    </>
                }
                </div>
            }
            { sessionUser && sessionUser.id === recipe.user.id &&
                <div className=''> Please add ingredient
                { recipe.ingredients.length === 0 &&
                    <>
                    { showAddIngredient &&
                        <CreateIngredient
                            recipe_id={recipe.id}
                            measurementUnits={measurementUnits}
                            edit={true}/>
                    }
                    { showAddIngredient ?
                        <button onClick={() => setShowAddIngredient(!showAddIngredient)} className=''>Save</button>
                        :
                        <button onClick={() => setShowAddIngredient(!showAddIngredient)} title='Add Ingredients'><i className="fa-solid fa-plus"></i>Add Ingredient</button>
                    }    
                    </>
                }
                </div>
            }
        <span className=''>
        <h2>Directions</h2>
            { sessionUser && sessionUser.id === recipe.user.id &&
                <div className=''>
                { recipe.instructions.length > 0 &&
                    <>
                    { showEditDirection ?
                        <div onClick={() => setShowEditDirection(!showEditDirection)} className=''>Save</div>
                        :
                        <div onClick={() => setShowEditDirection(!showEditDirection)} >Edit</div>
                    }
                    </>
                }
                </div>
            }
         </span>
            { directional_step.map(instruction => (
                <div className='' key={instruction.id}>
                    <Direction
                        key={instruction.id}
                        instruction={instruction}
                        recipe_id={recipe.id}
                        showEditDirection={showEditDirection}
                        setShowEditDirection={setShowEditDirection}
                        currentLength={recipe.instructions.length}
                        directionStep={directional_step.indexOf(instruction)}
                    />
                </div>   
            ))}
            { !sessionUser && recipe.id && !recipe.instructions.length &&
                <div className='RecipeBodyEmpty'>The owner of this recipe has not yet added the directions to this recipe.</div>
            }
            {  sessionUser && sessionUser.id !== recipe.user.id && !recipe.instructions.length &&
                <div className='RecipeBodyEmpty'>The owner of this recipe has not yet added the directions to this recipe.</div>
            }
            { sessionUser && sessionUser.id === recipe.user.id &&
                <div className=''>
                { recipe.instructions.length > 0 &&
                    <>
                    { showAddDirection &&
                        <CreateDirection
                            recipe_id={recipe.id}
                            existing_order={recipe.instructions.length}
                            edit={true}/>
                    }
                    { showAddDirection ?
                        <button onClick={() => setShowAddDirection(!showAddDirection)} className=''>cancel</button>
                        :
                        <button onClick={() => setShowAddDirection(!showAddDirection)}><i className="fa-solid fa-plus"></i>Add Step</button>
                    }
                    </>
                }
                </div>
            }
            { sessionUser && sessionUser.id === recipe.user.id &&
                <div className=''> Please add directions
                { recipe.instructions.length === 0 &&
                       <>
                       { showAddDirection &&
                           <CreateDirection
                               recipe_id={recipe.id}
                               existing_order={recipe.instructions.length}
                               edit={true}/>
                       }
                       { showAddDirection ?
                           <button onClick={() => setShowAddDirection(!showAddDirection)} className=''>cancel</button>
                           :
                           <button onClick={() => setShowAddDirection(!showAddDirection)}><i className="fa-solid fa-plus"></i>Add Step</button>
                       }
                       </>
                }
                </div>
            }
        </>
        <div ref={scrollToReview}></div>
        <div ref={scrollToReviews}></div>
        <div className='RecipePageBottom'><ReviewContainer recipe={recipe} /></div>
    </>    
    }                         
    </div>
    )
}

export default RecipePage
