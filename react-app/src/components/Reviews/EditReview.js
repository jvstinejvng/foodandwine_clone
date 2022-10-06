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

    const [submitted, setSubmitted] = useState(false)
    const [validationErrors, setValidationErrors] = useState([])

    useEffect(() => {
        let errors = []
        if (!rating) errors.push('Please leave a rating before submitting!')
        if (body.length > 750) errors.push('Please enter less than 750 characters!')
        setValidationErrors(errors)
    }, [rating, body])

    const handleSubmit = async(e) => {
        e.preventDefault()

        setSubmitted(true)
        if (validationErrors.length) return

        const data = {
            rating,
            body,
            user_id: sessionUser.id,
            recipe_id: comment.recipe_id,
            id: comment.id
        }

        setShowEdit(!showEdit)
        try {
            const updateReview = await dispatch(editCommentThunk(data))
            await dispatch(getRecipesThunk())

        } catch (e) {
            setValidationErrors(e.errors)
        }
    }

    return (
        <>
        <div className='EditReviewDiv'>
            {submitted && validationErrors.length > 0 &&
                <ul className='EditReviewError'>
                    {validationErrors.map(error => (
                        <li className='EditReviewError' key={error}>{error}</li>
                    ))}
                </ul>
            }
            <form onSubmit={handleSubmit} className='EditReviewForm'>
                <div className='EditReviewFormUser'>
                    <div>
                        {comment.user.username}
                    </div>
                </div>
                <div className='EditReviewFormInput'>
                    <div className='EditReviewFormInputDiv'>
                        <div className='EditReviewFormInputText'>
                            <div>Edit review</div>
                            <StarRating rating={rating} setRating={setRating} />
                        </div>
                        <div className='EditReviewFormInputMessage'>
                            <textarea
                                className='EditReviewFormTextArea'
                                placeholder='Write a review'
                                value={body}
                                onChange={(e) => setBody(e.target.value)}
                                >
                            </textarea>
                        </div>
                    </div>
                    <div className='EditReviewFormButton'>
                        <button onClick={() => setShowEdit(!showEdit)} className='EditReviewFormButtonCancel'>Cancel</button>
                        <button>Submit</button>
                    </div>
                </div>
            </form>
            </div>
        </>
    )
}

export default EditCommentForm
