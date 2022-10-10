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
    const [validError, setValidError] = useState({
        rating: null,
        body: ""
    })

    const [rating, setRating] = useState(null)
    const [body, setBody] = useState('')

    // const updateRating = (e) => setRating(e.target.value);
    // const updateBody = (e) => setBody(e.target.value);

    useEffect(() => {
        const newErrors = {};
        if (!rating) {
            newErrors["rating"] = "❗ Please rate the recipe.";
        } 
        if (body.length  > 1000) {
            newErrors["body"] = "❗You\'ve exceeded the 1000 character limit.";
        } 
        setValidError(newErrors);
    }, [rating, body, validError.length]);

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
                    <div className='ReviewTitle'>
                            <div className="ReviewTitleText">{recipe.title}</div>
                     </div>
                    <div className='CreateReviewStars'>     
                        <div>
                            {reviewed ?
                                <div className="CreateReviewStarDivReviewed"> You've already added a review for this recipe. </div>
                                : 
                                <div>
                                <span className="CreateReviewStarDivText">Your Rating</span>
                                <small className="ReviewRequired">&nbsp;(required)</small>
                                        <StarRating rating={rating} setRating={setRating}/>
                                <div className="CreateReviewError">{validError?.rating}</div>
                                </div>
                            }
                        </div>
                    </div>
                        <div className='ReviewInputTextBox'>
                            <div className='ReviewCommentDiv'>
                                {reviewed ?
                                    <div className='ReviewCommentPost'>
                                        See your your review post below to edit or delete your review. 
                                    </div>  
                                    : 
                                    <div>
                                        <span className='ReviewCommentText'>Your Review</span> 
                                        <small  className="ReviewOptional">&nbsp;(optional)</small>
                                         <textarea
                                            className='CreateReviewText'
                                            placeholder='What did you think about this recipe? Did you make any changes or notes?'
                                            value={body}
                                            onChange={(e) => setBody(e.target.value)}
                                        ></textarea>  
                                    <div className="CreateRecipeError">{validError?.body}</div>
                                    </div>   
                                }
                            </div>
                        </div>
                </div>
                <div className='CreateReviewSubmit'>
                        {reviewed ?
                            <span className='CreateReviewSubmitDisabled' disabled></span>
                            :
                            <button className="ReviewSubmitButton" 
                            disabled={
                                Object.values(validError).every((x) => x === "") ? false : true
                            }
                            >Submit</button>
                        }
                </div>
                </form>
        </>
        </div>
    )
}

export default CreateReview
