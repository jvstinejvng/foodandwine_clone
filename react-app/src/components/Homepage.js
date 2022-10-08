import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom';

import RecipeCard from  './Recipes/RecipeCard'
import { getRecipesThunk } from '../store/recipe'
import defaultimg from '../images/breadcrumb.png'

import './CSS/Homepage.css'

function Homepage() {
    
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)
    
    const newestRecipe = useSelector(state => Object.values(state.recipes).slice(-1))
    
    const bannerRecipes = Object.values(useSelector(state => state.recipes))
    const randomRecipe = Math.floor(Math.random() * bannerRecipes.length)

    const cookingRecipes = useSelector(state => Object.values(state.recipes).slice(0, 3))

    useEffect(() => {
        const fetchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        fetchRecipes().catch(console.error)
    }, [dispatch])


    const month = ["January","February","March","April","May","June","July","August","September","October","November","December"]; 
    const current = new Date();
    let monthName = month[current.getMonth()+1];
    const date = `${month[current.getMonth()]}/${current.getDate()}/${current.getFullYear()}`;
  

    return (
        <div className='HomepageContainer'>
                { sessionUser && 
                    <div className="HomepageSessionUser">
                        <h1 className='HomepageHeaderText'>Today is {date}</h1>
                        <p className="AllRecipeSubText"></p>
                    </div>

                }
            <div className='HomepageMainRecipe'>
                <div className='HomepageFirstDiv'>
                        <div className='HomepageNewestRecipeDiv'>
                                <div className='HomepageNewestRecipeLeft'>
                                    <div className='HomepageNewestRecipeFeature'>
                                            <div className='HomepageCookingRecipeDiv'>
                                                {newestRecipe && (
                                                    newestRecipe.map(recipe => (
                                                        <RecipeCard key={recipe.id} recipe={recipe} />
                                                    ))
                                                )}
                                            </div>
                                    </div>       
                                </div>
                        </div>
                </div>
            </div>
            <div className='HomepageBanner'>
                        <NavLink to={bannerRecipes.length > 0 && `/recipes/${bannerRecipes[randomRecipe].id}`}>
                    <div className='HomepageBannerInfo'>
                        <div className='HomepageBannerImageDiv'>
                                <img 
                                    onError={e => e.currentTarget.src=defaultimg} 
                                    className='HomepageBannerImage' 
                                    src={bannerRecipes.length > 0 && bannerRecipes[randomRecipe].image_url } />
                        </div>
                            <div className='HomepageBannerInfo'>
                                    {bannerRecipes.length > 0 && <h2 id='1'>{bannerRecipes[randomRecipe].title}</h2>}
                                    {bannerRecipes.length > 0 && <h4 id='2'>{bannerRecipes[randomRecipe].user.username}&nbsp;{bannerRecipes[randomRecipe].user.last_name}</h4>}
                            </div>
                    </div>
                        </NavLink>
            </div>     
                <div className='HomepageTrioRecipe'>
                    <NavLink className="HomepageCookingLink" to='/recipes'>
                        <div className='HomepageCooking'>
                            <span className='HomepageCookingText'>Cooking</span>
                            <span className='HomepageArrow'>➝</span>
                        </div>
                    </NavLink>
                        <div className='HomepageCookingRecipeDiv'>
                                {cookingRecipes && (
                                    cookingRecipes.map(recipe => (
                                        <RecipeCard key={recipe.id} recipe={recipe} />
                                    ))
                                )}
                        </div>
                </div>
                        <div>
                        </div>
        </div>
    )
}

export default Homepage
