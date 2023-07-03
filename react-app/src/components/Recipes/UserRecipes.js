import { useState, useEffect } from 'react'
import { NavLink, Link } from "react-router-dom"
import { useDispatch, useSelector } from 'react-redux'
import { getRecipesThunk } from '../../store/recipe'
import { getCommentsThunk } from '../../store/comment'
import RecipeCard from './RecipeCard'
import UserReview from '../Reviews/UserReview'
// import CreateRecipe from './CreateRecipe'
import '../CSS/UserRecipes.css'

function UserRecipes() {

    const dispatch = useDispatch()

    const sessionUser = useSelector(state => state.session.user)
    const recipes = useSelector(state => state.recipes)
    const reviews = useSelector(state => state.comments)
    const [myRecipesState, setMyRecipesState] = useState(1)
    const [isLoaded, setIsLoaded] = useState(false);

    useEffect(() => {
        const getUserRecipes = async () => {
            await dispatch(getRecipesThunk())
            .then(() => setIsLoaded(true))
        }
        getUserRecipes().catch(console.error)
    }, [dispatch])

    useEffect(() => {
        const getUserCommentsThunk = async () => {
            await dispatch(getCommentsThunk())
            .then(() => setIsLoaded(true))
        }
        getUserCommentsThunk().catch(console.error)
    }, [dispatch])

    // user's published recipes
    let recipe_sort
    if (recipes && sessionUser) {
        let my_recipes = Object.values(recipes).filter(recipe => {
            return recipe.user.id === sessionUser.id
        })
        recipe_sort = my_recipes.sort(((a, b) => b.id - a.id))
    }

    // user's saved recipes
    let saved_recipes = []
    if (recipes && sessionUser) {
        for (let recipe of Object.values(recipes)) {
            for (let save of recipe.saves) {
                if(save.id === sessionUser.id) { saved_recipes.push(recipe) }
            }
        }
    }

    let user_reviews 
    if (reviews && sessionUser ) {
        let my_reviews = Object.values(reviews).filter(comments => {
            return comments.user.id === sessionUser.id 
        })
        user_reviews = my_reviews.sort(((a, b) => b.id - a.id))
    }

    return (
        <div className='UserRecipeDiv'>
        <div className='RecipePages'>
            <div id='MyUserRecipeTab' className={myRecipesState === 1 ? 'active-tab': 'inactive'}>
                <h2 className='RecipePageTexts' onClick={() => setMyRecipesState(1)}>Your Recipes</h2>
            </div>
            <div id='MyUserRecipeTab' className={myRecipesState === 2 ? 'active-tab': 'inactive'}>
                <h2 className='RecipePageTexts' onClick={() => setMyRecipesState(2)}>Saved Recipes</h2>
            </div>
            <div id='MyUserRecipeTab' className={myRecipesState === 3 ? 'active-tab': 'inactive'}>
                <h2 className='RecipePageTexts' onClick={() => setMyRecipesState(3)}>Your Reviews</h2>
            </div>
        </div>       
        <div className='UserRecipeContainer'>
            { myRecipesState === 1 && 
                <div className='UserRecipeGridDiv'>Recipes you've created on Bread & Butter.
                    <div className='UserRecipeCardGrid'>
                    {recipe_sort && recipe_sort.length > 0 &&
                        Object.values(recipe_sort).map(recipe => ( <RecipeCard key={recipe.id} recipe={recipe} />))}
                    </div>
                    <div className='UserNoRecipeDiv'>
                    {recipe_sort.length === 0 && <div className='UserNoRecipe'>You haven't created any recipes yet. </div>}
                    </div>
                    {recipe_sort && recipe_sort.length > 0 ?
                        <div className='UserRecipeButtonTextDiv'><span className='UserRecipeButtonText'>Ready to Share More Recipes</span>
                            <NavLink  to='/recipes'><button className="UserRecipeButton">Add A Recipe</button></NavLink> 
                        </div>
                        :
                        <div><NavLink to='/new-recipe'><button className='UserRecipeButton'>Add A Recipe</button></NavLink></div> 
                    }    
                </div>
            }
            { myRecipesState === 2 &&
                <div className='UserRecipeGridDiv'>All your saved recipes! 
                    <div className='UserRecipeCardGrid'>
                    {saved_recipes && saved_recipes.length > 0 &&
                        Object.values(saved_recipes).map(recipe => ( <RecipeCard key={recipe.id} recipe={recipe} />))}
                    </div>
                    <div className='UserNoRecipeDiv'>
                    {saved_recipes.length === 0 && <div className='UserNoRecipe'>You don't have anything saved yet. Get cooking! </div>}
                    </div>
                    {saved_recipes && saved_recipes.length > 0 ?
                        <div className='UserRecipeButtonTextDiv'><span className='UserRecipeButtonText'>Hungry for More?</span>
                            <NavLink  to='/recipes'><button className="UserRecipeButton">Find</button></NavLink> 
                        </div>
                        :
                        <div><NavLink  to='/recipes'><button className="FindRecipeButton">Find Recipes</button></NavLink></div>   
                    }      
                </div>      
            }
            { myRecipesState === 3 && 
                <div className='UserRecipeGridDiv'> The following are reviews you have made.
                    <div className='UserReviewGrid'>
                        {user_reviews && user_reviews.length > 0 &&
                            Object.values(user_reviews).map((comment)=> (
                            <Link className="ReviewBox" to={`/recipes/${comment.recipe_id}`}>
                                <div className="ReviewBoxInside">
                                <UserReview key={comment.id} comment={comment}/>
                                </div>
                            </Link>
                        ))}
                    </div>

                        <div className='UserNoRecipeDiv'>
                        {user_reviews.length === 0 && <div className='UserNoRecipe'>You haven't created any reviews yet.</div> }
                        </div>
                        {user_reviews && user_reviews.length > 0 ? 
                            <div className='UserRecipeButtonTextDiv'><span className='UserRecipeButtonText'>Post More Reviews</span>
                                <NavLink  to='/recipes'><button className="FindRecipeButton">Review A Reviews</button></NavLink> 
                            </div>
                            :
                            <div><NavLink to='/recipes'><button className='UserRecipeButton'>Review A Review</button></NavLink></div>   
                        }
                </div>
            }
        </div>        
        </div>
    )
}

export default UserRecipes
