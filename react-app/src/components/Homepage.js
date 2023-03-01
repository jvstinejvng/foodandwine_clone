import { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { NavLink } from 'react-router-dom';
import { getRecipesThunk } from '../store/recipe'

import RecipeCard from  './Recipes/RecipeCard'
import FeaturedRecipe from './HomepageRecipe'
import bannerdefault from '../images/homepagedefault.jpg'

import './CSS/Homepage.css'

function Homepage() {
    
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)

    const newestRecipe = useSelector(state => Object.values(state.recipes).slice(-1))
    const bannerRecipes = Object.values(useSelector(state => state.recipes))
    const randomRecipe = Math.floor(Math.random() * bannerRecipes.length)
    const cookingRecipes = useSelector(state => Object.values(state.recipes).slice(0, 3))

    useEffect(() => {
        const searchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        searchRecipes().catch(console.error)
    }, [dispatch])

    
    const month = ["January","February","March","April","May","June","July","August","September","October","November","December"]; 
    const current = new Date();
    const date = `${month[current.getMonth()]} ${current.getDate()}, ${current.getFullYear()}`;
  
    return (
        <div className='HomepageContainer'>
            { !sessionUser && 
                <div className="HomepageSessionUser">
                    <div className='HomepageHeaderText' >Unleash your inner chef and spice up your life - with our recipes, culinary adventures are always in sight!</div>
                    <div className="HomepageSessionUserSub">Discover, cook, and share your favorite recipes with our community of food lovers.</div>
                </div>
            }
            { sessionUser && 
                <div className="HomepageSessionUser">
                    <div className='HomepageHeaderText'>Today is {date}</div>
                    <div className="HomepageSessionUserSub">Sharing the joy of cooking!</div>
                </div>
                }
        <div className='HomepageMainRecipe'>
            <div className='HomepageFirstDiv'>
                <div className='HomepageNewRecipeAlert'>Our newest recipe</div>
                    <div className='HomepageNewestRecipeFeature'>
                        <div className='HomepageNewRecipeDiv'>
                            {newestRecipe && (
                                newestRecipe.map(recipe => (
                                    <FeaturedRecipe key={recipe.id} recipe={recipe} />
                            )))}
                        </div>
                    </div> 
                    
                </div>        
            </div>

            <div className='HomepageBanner'>
                        <NavLink to={bannerRecipes.length > 0 && `/recipes/${bannerRecipes[randomRecipe].id}`}  style={{textDecoration: 'none'}}>
                    <div className='HomepageBannerDiv'>
                        <div className='HomepageBannerImageDiv'>
                                <img 
                                    onError={e => e.currentTarget.src=bannerdefault} 
                                    className='HomepageBannerImage' 
                                    src={bannerRecipes.length > 0 && bannerRecipes[randomRecipe].image_url } />
                        </div>
                            <div className='HomepageBannerInfo'>
                                    {bannerRecipes.length > 0 && <div className='HomeBannerTitle'>{bannerRecipes[randomRecipe].title}</div>}
                                    {bannerRecipes.length > 0 && <div className='HomeBannerUser'>{bannerRecipes[randomRecipe].user.first_name} {bannerRecipes[randomRecipe].user.last_name}</div>}
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
        </div>
    )
}

export default Homepage
