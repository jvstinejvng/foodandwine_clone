import { Link } from 'react-router-dom'

import '../CSS/RecipeCard.css'

function FeaturedRecipe( {recipe} ) {

    if(!recipe) return null
    
    return (
        <Link to={`/recipes/${recipe.id}`}>
            <div
            className='FeaturedRecipeDiv'>
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
                            <div className='FeaturedRecipeDescriptiontext'>by {recipe.description}</div>
                        </div>
                    </div>
                </div>
            </div>
        </Link>
    )
}

export default FeaturedRecipe
