import { Link } from 'react-router-dom'

import '../CSS/RecipeCard.css'

function RecipeCard( {recipe} ) {

    if(!recipe) return null
    
    return (
        <Link to={`/recipes/${recipe.id}`}>
            <div
            className='RecipeCardDiv'>
                <div className='RecipeCardImageDiv'>
                    <img  className='RecipeCardImage' src={recipe.image_url} onError={({ currentTarget }) => {
                        currentTarget.onerror = null;
                        currentTarget.src ='../../../../../static/buttertoast.png'
                    }} alt={`recipe-${recipe.id}`} />
                </div>
                <div className='RecipeCardInfo'>
                    <div className='RecipeCardTitle'>
                        <h3 className='RecipeCardTitleText'>{recipe.title}</h3>
                        <div className='RecipeCardUser'>
                            <h4 className='RecipeCardUserName'>by {recipe.user.first_name}</h4>
                        </div>
                    </div>
                </div>
            </div>
        </Link>
    )
}

export default RecipeCard
