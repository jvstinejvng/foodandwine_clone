import { useState, useEffect } from 'react'
import { NavLink } from "react-router-dom"
import { useDispatch, useSelector } from 'react-redux'

import { getRecipesThunk } from '../../store/recipe'
import { getCommentsThunk } from '../../store/comment'

import RecipeCard from './RecipeCard'
import UserReview from '../Reviews/UserReview'
import CreateRecipe from './CreateRecipe'

import '../CSS/UserRecipes.css'

function UserRecipes() {
    
    const sessionUser = useSelector(state => state.session.user)
    const recipes = useSelector(state => state.recipes)
    const reviews = useSelector(state => state.comments)

    const dispatch = useDispatch()

    const [isLoaded, setIsLoaded] = useState(false);
    const [myRecipesState, setMyRecipesState] = useState(1)

    // user's published recipes
    let recipe_sort
    if (recipes && sessionUser) {
        let my_recipes = Object.values(recipes).filter(recipe => {
            return recipe.user.id === sessionUser.id
        })
        recipe_sort = my_recipes.sort(((a, b) => b.id - a.id))
    }

    useEffect(() => {
        const getUserRecipes = async () => {
            await dispatch(getRecipesThunk())
            .then(() => setIsLoaded(true))
        }
        getUserRecipes().catch(console.error)
    }, [dispatch])


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
    if (reviews && sessionUser) {
        let my_reviews = Object.values(reviews).filter(comments => {
            return comments.user.id === sessionUser.id
        })
        user_reviews = my_reviews.sort(((a, b) => b.id - a.id))
        console.log(user_reviews)
    }

    useEffect(() => {
        const getUserCommentsThunk = async () => {
            await dispatch(getCommentsThunk())
            .then(() => setIsLoaded(true))
        }
        getUserCommentsThunk().catch(console.error)
    }, [dispatch])



    return (
        <div className='UserRecipeDiv'>
            <div className='RecipePages'>
                <div className={myRecipesState === 1 ? 'active-tab': 'inactive'}>
                    <h2 className='RecipePageTexts' onClick={() => setMyRecipesState(1)}>Personal Recipes</h2>
                </div>
                <div className={myRecipesState === 2 ? 'active-tab': 'inactive'}>
                    <h2 className='RecipePageTexts' onClick={() => setMyRecipesState(2)}>Saved Recipes</h2>
                </div>
                <div className={myRecipesState === 3 ? 'active-tab': 'inactive'}>
                    <h2 className='RecipePageTexts' onClick={() => setMyRecipesState(3)}>Recipe Reviews</h2>
                </div>
            </div>
                
            <div className='UserRecipeContainer'>
                { myRecipesState === 1 && 
                    <div className='UserRecipeGridDiv'> 
                        <p className="UserRecipeSubText">Recipes you have created on Bread & Butter.</p>
                        <div className='UserRecipeCardGrid'>
                            {recipe_sort && recipe_sort.length > 0 &&
                                Object.values(recipe_sort).map(recipe => (
                                    <RecipeCard key={recipe.id} recipe={recipe} />
                                ))
                            }
                        </div>
                        <div>
                            <NavLink to='/new-recipe'>
                                <button>Add A Recipe</button>
                            </NavLink>
                        </div>
                    </div>
                }
                { myRecipesState === 1 && 
                    <div className='UserRecipeCardGrid'>
                        {recipe_sort && !recipe_sort.length  && 
                            ( <div className='UserNoRecipesDiv'>
                                <div className='UserNoRecipes'>You have no recipes</div>
                                    {/* <div className='UserNoRecipesSubtext'> To add a recipe click the button below </div>
                                        <button className='UserNoRecipesButton'>Add A Recipe</button> */}
                                </div>
                            )   
                        }
                    </div>
                }
                { myRecipesState === 2 &&
                    <div className='UserRecipeGridDiv'> 
                        <p className="UserRecipeSubText">All Saved Recipes</p>
                        <div className='UserRecipeCardGrid'>
                            {saved_recipes && saved_recipes.length > 0 ?
                                Object.values(saved_recipes).map(recipe => (
                                    <RecipeCard key={recipe.id} recipe={recipe} />
                                ))
                                :
                                <h3>You don't have anything saved yet. Get cooking!</h3>
                            }
                        </div>
                        <div>
                            Hungry for More?
                            <NavLink  to='/recipes'>
                                <button>Find More Recipes</button>
                            </NavLink>
                        </div>
                    </div>      
                }
                  { myRecipesState === 3 && 
                    <div className='UserRecipeGridDiv'> 
                        <p className="UserRecipeSubText">Review</p>
                        <div className='UserRecipeCardGrid'>
                            {user_reviews && user_reviews.length > 0 &&
                                Object.values(user_reviews).map(comment => (
                                    <div>
                                    <UserReview 
                                        key={comment.id} 
                                        comment={comment}
                                        
                                    />
                                    </div>
                                    
                                ))
                            }
                        </div>
                        <div>
                            <NavLink to='/new-recipe'>
                                <button>Add A Recipe</button>
                            </NavLink>
                        </div>
                    </div>
                }

                
            </div>        
        </div>
    )
}

export default UserRecipes
