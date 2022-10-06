import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from "react-redux"
import StarRating from './StarRating'

import { postCommentThunk } from '../../store/comment'
import { getRecipesThunk } from '../../store/recipe'

import '../CSS/CreateReview.css'

function CreateReview({ recipe }) {
    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)

    const [rating, setRating] = useState(null)
    const [body, setBody] = useState('')

    const [submitted, setSubmitted] = useState(false)
    const [validationErrors, setValidationErrors] = useState([])

    //validations
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

        const payload = {
            rating,
            body,
            user_id: sessionUser.id,
            recipe_id: recipe.id
        }
        try {
            const data = await dispatch(postCommentThunk(payload))
            if (data) {
                setSubmitted(false)
                setRating(null)
                setBody('')
            }
            await dispatch(getRecipesThunk())

        } catch (e) {
            setValidationErrors(e.errors)
        }
    }

    let reviewd = false
    for (let comment of recipe.comments) {
        if (comment.user.id === sessionUser.id) {
            reviewd = true
        }
    }

    return (
        <>
        <div className='CreateReviewDiv'>
                {submitted && validationErrors.length > 0 &&
                        <ul className='CreateReviewErrors'>
                            {validationErrors.map(error => (
                                <li className='error' key={error}>{error}</li>
                            ))}
                        </ul>
                }
            <form onSubmit={handleSubmit} className='CreateReviewForm'>
                    <div className='CreateReviewFormInput'>
                            <div className='CreateReviewFormStars'>
                                <div>
                                    Rate and Review
                                </div>
                        <StarRating rating={rating} setRating={setRating}/>
                    </div>
                    <div className='CreateReviewFormUser'>
                        <div className='CreateReviewFormUserInfo'>
                            <div>
                            {sessionUser.username}    
                            </div>   
                        </div>
                            {reviewd ?
                                <string
                                className='CreateReviewDisabled'
                                placeholder='Only one review'
                                value={body}
                                onChange={(e) => setBody(e.target.value)}
                                disabled
                                ></string>
                            :
                                <textarea
                                className='CreateReviewEntry'
                                placeholder='Write a review'
                                value={body}
                                onChange={(e) => setBody(e.target.value)}
                                ></textarea>
                        }
                    </div>
                </div>
                <div className='CreateReviewButton'>
                        {reviewd ?
                        <button className='CreateReviewButtonDisabled' disabled>One Review</button>
                        :
                        <button className='CreateReviewSubmit'>Submit</button>
                        }
                </div>
            </form>
        </div>
        </>
    )
}

export default CreateReview
