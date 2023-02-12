import { useSelector } from 'react-redux'

import '../CSS/RecipePage.css'

import CreateReview from './CreateReview'
import UserReview from "./UserReview"

function ReviewContainer( { recipe })  {
    const sessionUser = useSelector(state => state.session.user)

    return (
        <>
        <div>
            {sessionUser ?
                <CreateReview recipe={recipe}/>
                :
                <div className='LeaveAReview'>
                    Log in to leave a review!
                </div>
            }
            </div>
            {recipe.comments.length > 0 ?
                Object.values(recipe.comments).map(comment => (
                    <UserReview comment={comment} />
                ))
                :
                <h3>Be the first to review!</h3>
            }

        </>
    )
};

export default ReviewContainer;
