import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from "react-redux"
import StarRating from './StarRating'

import { postCommentThunk } from '../../store/comment'
import { getRecipesThunk } from '../../store/recipe'

import '../CSS/CreateReview.css'

function CreateReview( {recipe} ) {

    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)

    const [submitted, setSubmitted] = useState(false)
    const [validError, setValidError] = useState([])

    const [rating, setRating] = useState(null)
    const [body, setBody] = useState('')

    useEffect(() => {
        let error = []
        if (!rating) error.push('A rating is required before submitting.')
        if (body.length > 1000) error.push('You\'ve exceeded the 1000 character limit.')
        setValidError(error)
    }, [rating, body])


    const handleSubmit = async(e) => {
        e.preventDefault()

        setSubmitted(true)
        if (validError.length) return

        const data = {
            rating,
            body,
            user_id: sessionUser.id,
            recipe_id: recipe.id
        }

        try {
            const newData = await dispatch(postCommentThunk(data))
            if (newData) {
                setSubmitted(false)
                setRating(null)
                setBody('')
            }
            await dispatch(getRecipesThunk())

        } catch (e) {
            setValidError(e.errors)
        }
    }

    let reviewed = false
    for (let comment of recipe.comments) {
        if (comment.user.id === sessionUser.id) {
            reviewed = true
        }
    }

    return (
        <div className='CreateFormDiv'>
        <>
            <form onSubmit={handleSubmit} className='CreateReviewForm'>
                <div className='ReviewInputDiv'>
                    <div className='ReviewUserName'>
                            <div>
                              {recipe.title} 
                            </div>
                     
                        </div>
                        {submitted && validError.length > 0 &&
                            <div className='CreateReviewError'>
                                    {validError.map(error => (
                                <div className='CreateReviewError' key={error}>{error}</div>
                            ))}
                            </div>
                         }

                    <div className='CreateReviewStars'>
                        <div>
                            Your Rating
                        </div>
                        <div>
                        <StarRating rating={rating} setRating={setRating}/>
                        </div>
                    </div>
                    <div className='ReviewInputTextBox'>
                        <div>
                        Your Review
                        </div>
                        <div>
                        {reviewed ?
                            <textarea
                            className='CreateReviewDisabled'
                            placeholder='You have already made a review for this recipe!'
                            value={body}
                            onChange={(e) => setBody(e.target.value)}
                            disabled
                            ></textarea>
                        :
                            <textarea
                                className='CreateReviewText'
                                placeholder='What did you think about this recipe? Did you make any changes or notes?'
                                value={body}
                                onChange={(e) => setBody(e.target.value)}
                                ></textarea>
                        }
                        </div>
             
                    </div>
                </div>
                <div className='CreateReviewSubmit'>
                    {reviewed ?
                        <span id='CreateReviewSubmitDisabled' disabled></span>
                    :
                        <button>Submit</button>
                    }
                </div>
            </form>
        </>
        </div>
    )
}

export default CreateReview
