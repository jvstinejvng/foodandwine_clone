import { useEffect, useState } from 'react'
import { useDispatch } from "react-redux"
import StarRating from './StarRating'

import { editCommentThunk } from '../../store/comment'
import { getRecipesThunk } from '../../store/recipe'

import '../CSS/EditReview.css'


function EditCommentForm({ comment, sessionUser, showEdit, setShowEdit }) {
    const dispatch = useDispatch()

    const [rating, setRating] = useState(comment.rating)
    const [body, setBody] = useState(comment.body)
    const [hasSubmitted, setHasSubmitted] = useState(false)
    const [validationErrors, setValidationErrors] = useState([])

    useEffect(() => {
        let errors = []

        if (!rating) errors.push('A rating is required before submitting.')
        if (body.length > 750) errors.push('You\'ve exceeded the 1000 character limit')
        setValidationErrors(errors)
    }, [rating, body])

    const handleSubmit = async(e) => {
        e.preventDefault()

        setHasSubmitted(true)
        if (validationErrors.length) return

        const payload = {
            rating,
            body,
            user_id: sessionUser.id,
            recipe_id: comment.recipe_id,
            id: comment.id
        }

        setShowEdit(!showEdit)

        try {
            const data = await dispatch(editCommentThunk(payload))
            await dispatch(getRecipesThunk())

        } catch (e) {
            setValidationErrors(e.errors)
        }
    }

    return (
        <>
            {hasSubmitted && validationErrors.length > 0 &&
                <ul className='errors'>
                    {validationErrors.map(error => (
                        <li className='error' key={error}>{error}</li>
                    ))}
                </ul>
            }
            <form onSubmit={handleSubmit} className='EditReviewDiv'>
                <div className='ReviewUserName'>
                    <div className="Reviewer">
                    {comment.user.first_name} 
                    </div>
                </div>
                <div className='ReviewDivText'>
                    <div className='ReviewInputDiv'>
                        <div className='ReviewInputStars'>
                                Your Rating
                            <StarRating rating={rating} setRating={setRating} />
                        </div>
                        <div className='ReviewInputTextBox'>
                            Your Review
                            <textarea
                                className='EditReviewInputReview'
                                placeholder='What did you think about this recipe? Did you make any changes or notes?'
                                value={body}
                                onChange={(e) => setBody(e.target.value)}
                                >
                            </textarea>
                        </div>
                    </div>
                    <div className='EditReviewButton'>
                        <button onClick={() => setShowEdit(!showEdit)} className='ReviewCancelButton'>Cancel</button>
                        <button>Submit</button>
                    </div>
                </div>
            </form>
        </>
    )
}

export default EditCommentForm
