import React, {useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { useHistory, useParams } from 'react-router-dom';
import { addReviewThunk, loadReviewThunk } from '../../store/reviews';
import '../CSS/Review.css'

const AddReviewForm = () => {

    const {id} = useParams()
    const history = useHistory();
    const dispatch = useDispatch();
    const [hasSubmitted, setHasSubmitted] = useState(false)

    const sessionUser = useSelector(state => state.session.user)

    const [stars, setStars] = useState(0);
    const [review, setReview] = useState("");
    const [errors, setErrors] = useState([]);

    const [dropdown, setDropdown] = useState(true)

    useEffect(() => {
        let validate = []
        if (!stars) validate.push('Your star rating is required before submitting.')
        if (review.length > 1000) validate.push('You have exceeded the maximum limit of characters allowed(1000 characters)')
        setErrors(validate)
    }, [stars, review])


    const handleSubmit = async (e) => {
        e.preventDefault()

        setHasSubmitted(true)
        if (errors.length) return

        const data = {
            stars: parseInt(stars),
            review,
            recipeId: id,
            userId: sessionUser.id
        }
            try {
                const review = await dispatch(addReviewThunk(review))
                if (review) {
                    setStars(0)
                    setReview("")
                    setDropdown(true)
                    setHasSubmitted(false)
                }
                await dispatch(loadReviewThunk())
    
            } catch (e) {
                setErrors(e.errors)
            }
        
    }


    return (
        <div className='new-review-form-container'>
            <form onSubmit={handleSubmit}>
            <h1 className='single-h2'>Reviews:</h1> 
                {dropdown === false ? <label className="new-review-label" htmlFor="rating"> Your Rating
                    {errors.length > 0 &&
                        <ul className='errors'>
                            {errors.map(error => (
                            <li className='error' key={error}>{error}</li>
                        ))}
                    </ul>
                    }
                <div className="rating" id="rating" onChange={e => setStars(e.target.value)}> 
                        <input
                            className="star star-1"
                            type="radio"
                            name="stars"
                            id="star-1"
                            value="5"
                        />
                        <label className="star star-1 star-label" htmlFor="star-1"></label>
                        <input
                            className="star star-2"
                            type="radio"
                            name="stars"
                            id="star-2"
                            value="4"
                        />
                        <label className="star star-2 star-label" htmlFor="star-2"></label>
                        <input
                            className="star star-3"
                            type="radio"
                            name="stars"
                            id="star-3"
                            value="3"
                        />
                        <label className="star star-3 star-label" htmlFor="star-3"></label>
                        <input
                            className="star star-4"
                            type="radio"
                            name="stars"
                            id="star-4"
                            value="2"
                        />
                        <label className="star star-4 star-label" htmlFor="star-4"></label>
                        <input
                            className="star star-5"
                            type="radio"
                            name="stars"
                            id="star-5"
                            value="1"
                        />
                        <label className="star star-5 star-label" htmlFor="star-5"></label>
                </div>
                </label>:<></>}
                <div>
                    {dropdown === true ? <button className="new-review-label review-toggle" onClick={() => setDropdown(!dropdown)}>Leave a review</button>:<label className="new-review-label">Your Review
                        <textarea
                            className='new-review-input'
                            id="review-text"
                            value={review}
                            onChange={e => setReview(e.target.value)}
                            required
                            autoComplete='off'
                            placeholder="What did you think about this recipe? Did you make any changes or notes?"
                        />
                    </label>}
                </div>
                <div className='buttons-container'>
                    {dropdown === false ? <button className='add-review-button' type='submit'>Submit</button>:<></>}
                    {dropdown === false ? <button className='add-review-button cancel-review' onClick={() => setDropdown(!dropdown)} type='button'>Cancel</button>:<></>}
                </div>
            </form>
        </div>
    )
}

export default AddReviewForm
