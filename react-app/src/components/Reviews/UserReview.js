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
            alert('Failed to delete. Please try again!' + e)
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
                <div className='ReviewDiv'>
                        <div className='ReviewDivText'>
                            <div className='ReviewUsernameDiv'>
                                 <div className='ReviewUser'>{ comment.user.username }</div>
                                        <div className='ReviewDivRating'>
                                            <div>{ [...Array(comment.rating)].map(star => <FaStar className='StarRating' />) }</div>
                                            <div>{ [...Array(5 - comment.rating)].map(star => <FaStar color='#DCDCDC' className='StarRating'/>) }</div>
                                            <div> {comment.created_at.split(' ').slice(1, 4).join(' ')}</div>
                    
                                </div>
                        </div>
                    <div className='ReviewUserDiv'>
                        <div className='ReviewUserDivMessage'>
                            <div className='ReviewText'>{ comment.body }</div>
                            {sessionUser && sessionUser.id === comment.user.id &&
                                <div className='ReviewButtonDiv'>
                                    <div onClick={() => setShowEdit(!showEdit)}>
                                        <span>
                                        <button className='edit'>edit</button>
                                        </span>
                                    </div>
                                    <div onClick={handleDelete} >
                                        <span>
                                        <button className='ReviewCancelButton'>delete</button>
                                        </span>
                                    </div>
                                </div>
                            }
                        </div>
                    </div>
                </div>
            </div>
        )
        
    )
}

export default UserReview
