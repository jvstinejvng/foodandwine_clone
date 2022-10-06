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

    useEffect(() => {
        let errors = []

        if (!rating) errors.push('Rating is require')
        if (body.length > 750) errors.push('You have exceed the ')
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
            recipe_id: recipe.id
        }
        try {
            const newReview = await dispatch(postCommentThunk(data))
            if (newReview) {
                setSubmitted(false)
                setRating(null)
                setBody('')
            }
            await dispatch(getRecipesThunk())

        } catch (e) {
            setValidationErrors(e.errors)
        }
    }

    let reviewed = false
    for (let comment of recipe.comments) {
        if (comment.user.id === sessionUser.id) {
            reviewed = true
        }
    }

    return (
        <>
        <div className='CreateReviewDiv'>
                     <div className='CreateReviewFormUserInfo'>
                            <div>
                            {sessionUser.first_name}    
                            </div>   
                        </div>
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
                            {reviewed ?
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
                        {reviewed ?
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
