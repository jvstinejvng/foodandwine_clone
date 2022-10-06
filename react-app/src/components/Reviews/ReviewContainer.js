import { useSelector } from 'react-redux'

import CreateReview from './CreateReview'
import UserReview from "./UserReview"

function ReviewContainer( {recipe} ) {

    const sessionUser = useSelector(state => state.session.user)
    return (
        <>
            {sessionUser ?
                <CreateReview recipe={recipe}/>
                :
                <h3>Login to leave a review!</h3>
            }
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
