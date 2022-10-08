import { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getRecipesThunk } from '../../store/recipe'
import RecipeCard from './RecipeCard'
import CreateRecipe from './CreateRecipe'

import '../CSS/UserRecipes.css'

function UserRecipes() {
    
    const dispatch = useDispatch()
    const recipes = useSelector(state => state.recipes)
    const sessionUser = useSelector(state => state.session.user)
    const [isLoaded, setIsLoaded] = useState(false);



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

    return (
        <div className='UserRecipeDiv'>
                <div className='UserRecipeHeaderDiv' >
                    <h1 className='UserRecipeHeaderText'>Personal Recipes</h1>
                        <p className="UserRecipeSubText">Recipes you have created on Bread & Butter.</p>
                </div>
            <div className='UserRecipeContainer'>
                    {isLoaded && sessionUser &&
                        <div className='UserRecipeCardGrid'>
                            {recipe_sort && recipe_sort.length > 0 &&
                                Object.values(recipe_sort).map(recipe => (
                                    <RecipeCard key={recipe.id} recipe={recipe} />
                                ))
                            }
                        </div>
                    }
                    
                    {isLoaded &&  sessionUser &&
                       <div className='UserRecipeCardGrid'>
                            {recipe_sort && !recipe_sort.length  && 
                                ( 
                                    <div className='UserNoRecipesDiv'>
                                        <div className='UserNoRecipes'>You have no recipes</div>
                                        <div className='UserNoRecipesSubtext'> To add a recipe click the button below </div>
                                        <button className='UserNoRecipesButton'>Add A Recipe</button>
                                    </div>
                                )
                            
                            }
                        </div>
                    }
            </div>        
        
        </div>
    )
}

export default UserRecipes
