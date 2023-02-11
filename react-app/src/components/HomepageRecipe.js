import { Link } from 'react-router-dom'

import './CSS/FeatureRecipe.css'

function FeaturedRecipe( {recipe} ) {


    if(!recipe) return null
    
    return (
        <>
        <Link to={`/recipes/${recipe.id}`}  style={{textDecoration: 'none'}}>
            <div className='FeaturedRecipeDiv'>
                <div className='FeaturedRecipeCard'>
                    <img  className='FeaturedRecipeImage' src={recipe.image_url} onError={({ currentTarget }) => {
                        currentTarget.onerror = null;
                        currentTarget.src ='../../../../../static/buttertoast.png'
                    }} alt={`recipe-${recipe.id}`} />
                </div>
                <div className='FeaturedRecipeInfo'>
                    <div className='FeaturedRecipeTitle'>
                        <div className='FeaturedRecipeText'>{recipe.title}</div>
                        <div className='FeaturedRecipeDescription'>
                            <div className='FeaturedRecipeDescriptiontext'>{recipe.description}</div>
                        </div>
                        <div className='FeaturedRecipeUser'>
                            <div className='FeaturedRecipeUsertext'>By {recipe.user.first_name}  {recipe.user.last_name}</div>
                        </div>
                    </div>
                </div>
            </div>
        </Link>
        </>
    )
}

export default FeaturedRecipe
