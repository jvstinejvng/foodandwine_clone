import { useState } from 'react'
import { FaStar } from 'react-icons/fa'
import { useDispatch, useSelector } from 'react-redux'
import EditReview from './EditReview'

import { deleteCommentThunk } from '../../store/comment'
import { getRecipesThunk } from '../../store/recipe'

import '../CSS/UserReview.css'

function UserReview( {comment} ) {

    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)

    const [showEdit, setShowEdit] = useState(false)

    const handleDelete = async(e) => {
        e.preventDefault()

        try {
            await dispatch(deleteCommentThunk(comment))
            await dispatch(getRecipesThunk())

        } catch (e) {
            alert('Delete Failed!' + e)
        }
    }

    return (
        (showEdit ?
                <EditReview
                    comment={comment}
                    sessionUser={sessionUser}
                    showEdit={showEdit}
                    setShowEdit={setShowEdit}/>
                :
            <div className='UserReviewDiv'>
                <div className='UserReviewUser'>
                    <div>
                        {comment.user.username}
                    </div>
                </div>
                <div className='UserReviewInput'>
                    <div className='UserReviewText'>
                        {/* <div>{ comment.user.username }</div> */}
                        <div className='UserReviewSubmit'>
                            <span>Posted {comment.created_at.split(' ').slice(1, 4).join(' ')}</span>
                            <p className='UserReviewStars'>{ [...Array(comment.rating)].map(star => <FaStar className='rated' />) }</p>
                            <p className='UserReviewStars'>{ [...Array(5 - comment.rating)].map(star => <FaStar color='#DCDCDC' className='rated'/>) }</p>
                        </div>
                    </div>
                    <div className='UserReviewBodyDiv'>
                        <div className='UserReviewBody'>{ comment.body }</div>
                                {sessionUser && sessionUser.id === comment.user.id &&
                                        <div className='UserReviewButton'>
                                                <button onClick={() => setShowEdit(!showEdit)} className='UserReviewButtonEdit'>edit</button>
                                                <button onClick={handleDelete} className='UserReviewButtonDelete'>delete</button>
                                        </div>
                                }
                    
                    </div>
                </div>
            </div>

        )
    )
}

export default UserReview
