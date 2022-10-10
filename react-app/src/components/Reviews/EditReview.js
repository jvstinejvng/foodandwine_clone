import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from "react-redux"
import StarRating from './StarRating'

import { editCommentThunk } from '../../store/comment'
import { getRecipesThunk } from '../../store/recipe'

import '../CSS/EditReview.css'


function EditCommentForm({ comment, showEdit, setShowEdit }) {

    const dispatch = useDispatch()

    const [submitted, setSubmitted] = useState(false)

    const sessionUser = useSelector(state => state.session.user)
    const [validError, setValidError] = useState({
        rating: null,
        body: ""
    })


    const [rating, setRating] = useState(comment.rating)
    const [body, setBody] = useState(comment.body)

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

        const payload = {
            rating,
            body,
            user_id: sessionUser.id,
            recipe_id: comment.recipe_id,
            id: comment.id
        }

        // setShowEdit(!showEdit)

        try {
            const data = await dispatch(editCommentThunk(payload))
            if(data) (setShowEdit(!showEdit))
            await dispatch(getRecipesThunk(data))
        

        } catch (e) {
            // setValidationErrors(e.errors)
        }
    }

    return (
        <>
            {/* {hasSubmitted && validationErrors.length > 0 &&
                <ul className='errors'>
                    {validationErrors.map(error => (
                        <li className='error' key={error}>{error}</li>
                    ))}
                </ul>
            } */}
            <form onSubmit={handleSubmit} className='EditReviewDiv'>
                <div className='ReviewUserName'>
                    <div className="Reviewer">
                    {comment.user.username} 
                    </div>
                </div>
                <div className='ReviewDivText'>
                    <div className='ReviewInputDiv'>
                        <div className='ReviewInputStars'>
                                Your Rating
                            <StarRating rating={rating} setRating={setRating} />
                            <div >{validError?.rating}</div>
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
                            <div >{validError?.body}</div>
                        </div>
                    </div>
                    <div className='EditReviewButton'>
                        <button onClick={() => setShowEdit(!showEdit)} className='ReviewCancelButton'>Cancel</button>
                        <button 
                         disabled={
                            Object.values(validError).every((x) => x === "") ? false : true
                          }
                        >Submit</button>
                    </div>
                </div>
            </form>
        </>
    )
}

export default EditCommentForm
