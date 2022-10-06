import { useSelector } from 'react-redux'

import '../CSS/RecipePage.css'

import CreateReview from './CreateReview'
import UserReview from "./UserReview"

function CommentSection({ recipe }) {
    const sessionUser = useSelector(state => state.session.user)

    return (
        <>
            {sessionUser ?
                <CreateReview recipe={recipe}/>
                :
                <h3>Login to leave a comment!</h3>
            }
            {recipe.comments.length > 0 ?
                Object.values(recipe.comments).map(comment => (
                    <UserReview comment={comment} />
                ))
                :
                <h3>Looks like no one has left a comment yet, be the first!</h3>
            }

        </>
    )
};

export default CommentSection;
