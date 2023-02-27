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
import NotFound from '../NotFound.js'
import '../CSS/RecipePage.css'

function RecipePage() {

    const dispatch = useDispatch()
    const history = useHistory()
    const { id } = useParams()
    const scrollToReview = useRef()
    const sessionUser = useSelector(state => state.session.user)
    const recipe = useSelector(state => state.recipes[id])

    const [showEdit, setShowEdit] = useState(false)
    const [showAddIngredient, setShowAddIngredient] = useState(false)
    const [showAddInstruction, setShowAddInstruction] = useState(false)
    const [showEditIngredientredient, setshowEditIngredientredient] = useState(false)
    const [showEditInstruction, setShowEditInstruction] = useState(false)
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

    let instruction_step
    if (recipe) {
        instruction_step = Object.values(recipe.instructions).sort((a, b) => (a.list_order > b.list_order ? 1: -1))
    }

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
                    { isNaN(average_rating(recipe)) ?
                    <div className='RecipePageNoReview'
                        onClick={() => scrollToReview.current.scrollIntoView({ behavior: 'smooth' })}>
                            Be the first to rate & review!
                    </div>
                    :
                    <div className='RecipePageWithReview'>
                        <span><FaStar/></span>
                            {average_rating(recipe)} 
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
                { recipe.created_at === recipe.updated_at ?
                    <span className='RecipePageCreateAt'>Published on {recipe.created_at.split(' ').slice(1, 4).join(' ')}</span>
                    :
                     <span className='RecipePageCreateAt'>Updated on {recipe.updated_at.split(' ').slice(1, 4).join(' ')}</span>
                }
            </div>
        </div>
            <div className='RecipePageBody'>
                { !showEdit ?
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
                    </div>
                    :
                    <div className='RecipePageEditRecipe'>
                        <EditRecipe
                            recipe={recipe}
                            setShowEditForm={setShowEdit}
                        />           
                    </div>
                }
            <div>
                <div className='header-button-container-ing'>
                    <h3 id='ingredients' className='straight-underline'>Ingredients</h3>
                    { sessionUser && sessionUser.id === recipe.user.id &&
                        <div className='edit-button-container'>
                            { recipe.ingredients.length > 0 &&
                            <>
                            {showEditIngredientredient ?
                                <span 
                                    onClick={() => setshowEditIngredientredient(!showEditIngredientredient)}
                                    className='done'>Done Editing
                                </span>
                                :
                                <div
                                    onClick={() => setshowEditIngredientredient(!showEditIngredientredient)}
                                    className='edit-pen'
                                    title='Edit Ingredients'>
                                    <i className="fa-solid fa-pen"></i>
                                </div>
                            }
                            {showAddIngredient ?
                                <span
                                    onClick={() => setShowAddIngredient(!showAddIngredient)}
                                    className='done'>Done Adding</span>
                                :
                                <div
                                    onClick={() => setShowAddIngredient(!showAddIngredient)}
                                    title='Add Ingredients'><i className="fa-solid fa-plus"></i>
                                </div>
                            }
                            </>
                            }
                        </div>
                    }
                </div>
                <div>
                    { sessionUser && sessionUser.id === recipe.user.id && !recipe.ingredients.length && !showAddIngredient &&
                        <div className='add-info' onClick={() => setShowAddIngredient(!showAddIngredient)}>
                            <h2>Click here to add Ingredients to your recipe!</h2>
                        </div>
                    }
                    <ul>
                        {ingredient_list.map(ingredient => (
                            <li key={ingredient.id}>
                                <Ingredient
                                    ingredient={ingredient}
                                    recipe={recipe}
                                    showEditIngredient={showEditIngredientredient}
                                    setshowEditIngredient={setshowEditIngredientredient}
                                    measurementUnits={measurementUnits}
                                />
                            </li>
                        ))}
                    </ul>
                </div>
                { showAddIngredient &&
                    <div>
                    <CreateIngredient
                        recipe_id={recipe.id}
                        measurementUnits={measurementUnits}
                        edit={true}/>
                    </div>
                }
            </div>
            <div>
                <div className='header-button-container inst'>
                    <h3 id='instructions' className='straight-underline'>Instructions</h3>
                    { sessionUser && sessionUser.id === recipe.user.id &&
                        <div className='edit-button-container'>
                            { recipe.instructions.length > 0 &&
                                <>
                                { showEditInstruction ?
                                    <span
                                        onClick={() => setShowEditInstruction(!showEditInstruction)}
                                        className='done'>Done editing
                                    </span>
                                    :
                                    <div
                                        onClick={() => setShowEditInstruction(!showEditInstruction)}
                                        title='Edit Instructions'>
                                        <i className="fa-solid fa-pen"></i>
                                    </div>
                                }
                                { showAddInstruction ?
                                    <span 
                                        onClick={() => setShowAddInstruction(!showAddInstruction)} 
                                        className='done'>Done Adding
                                    </span>
                                    :
                                    <div
                                        onClick={() => setShowAddInstruction(!showAddInstruction)}
                                        title='Add Instructions'>
                                        <i className="fa-solid fa-plus"></i>
                                    </div>
                                }
                                </>
                            }
                        </div>
                    }
                    </div>
                    <div>
                    { sessionUser && sessionUser.id === recipe.user.id && !recipe.instructions.length && !showAddInstruction &&
                        <div className='add-info' onClick={() => setShowAddInstruction(!showAddInstruction)}>
                            <h2>Click here to add Instructions to your recipe!</h2>
                        </div>
                    }
                    { instruction_step.map(instruction => (
                        <Direction
                            key={instruction.id}
                            instruction={instruction}
                            recipe_id={recipe.id}
                            showEditInst={showEditInstruction}
                            setShowEditInst={setShowEditInstruction}
                            urrentLength={recipe.instructions.length}
                            />
                    ))}
                    </div>
                    { showAddInstruction &&
                        <div>
                        < CreateDirection
                            recipe_id={recipe.id}
                            existing_order={recipe.instructions.length}
                            edit={true}/>
                        </div>
                    }
            </div>
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
