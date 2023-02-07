import { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getRecipesThunk } from '../../store/recipe'

import RecipeCard from './RecipeCard'
import CreateRecipe from './CreateRecipe'

import '../CSS/UserRecipes.css'

function UserRecipes() {
    
    const sessionUser = useSelector(state => state.session.user)
    const recipes = useSelector(state => state.recipes)

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

    return (
        <div className='UserRecipeDiv'>
                {/* <div className='UserRecipeHeaderDiv' >
                    <h1 className='UserRecipeHeaderText'>Personal Recipes</h1>
                        <p className="UserRecipeSubText">Recipes you have published on Bread & Butter.</p>
                </div> */}
                <div className='my-recipe-tabs'>
                <div className={myRecipesState === 1 ? 'active-tab': 'inactive'}>
                    <h2 onClick={() => setMyRecipesState(1)}>My recipes</h2>
                </div>
                <div className={myRecipesState === 2 ? 'active-tab': 'inactive'}>
                    <h2 onClick={() => setMyRecipesState(2)}>Saved Recipes</h2>
                </div>
                <div className={myRecipesState === 3 ? 'active-tab': 'inactive'}>
                    <h2 onClick={() => setMyRecipesState(3)}>Favorite Recipes</h2>
                </div>
            </div>
                
            <div className='UserRecipeContainer'>
                    {myRecipesState === 1 && 
                        <div className='UserRecipeCardGrid'>
                            {recipe_sort && recipe_sort.length > 0 &&
                                Object.values(recipe_sort).map(recipe => (
                                    <RecipeCard key={recipe.id} recipe={recipe} />
                                ))
                            }
                        </div>
                    }
                    
                    {myRecipesState === 1 && 
                       <div className='UserRecipeCardGrid'>
                            {recipe_sort && !recipe_sort.length  && 
                                ( 
                                    <div className='UserNoRecipesDiv'>
                                        <div className='UserNoRecipes'>You have no recipes</div>
                                        {/* <div className='UserNoRecipesSubtext'> To add a recipe click the button below </div>
                                        <button className='UserNoRecipesButton'>Add A Recipe</button> */}
                                    </div>
                                )
                            
                            }
                        </div>
                    }

            {myRecipesState === 2 &&
                <div className='recipes-container'>
                    {saved_recipes && saved_recipes.length > 0 ?
                        Object.values(saved_recipes).map(recipe => (
                            <RecipeCard key={recipe.id} recipe={recipe} />
                        ))
                    :
                    <h3 id='no-recipes'>Looks like you haven't saved any recipes!</h3>
                    }
                </div>
            }


            </div>        
        
        </div>
    )
}

export default UserRecipes
