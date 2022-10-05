import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { createReviewThunk } from "../../store/reviews";
import '../CSS/Review.css'

const CreateReview = ({ RecipeId, userId, displayLanding }) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const currentUser = useSelector(state => state?.session?.user);
  const [errors, setErrors] = useState([]);
  const [review, setReview] = useState('');
  const [stars, setStars] = useState('');

  const updateReview = (e) => setReview(e.target.value);
  const updateStars = (e) => setStars(e.target.value);


  useEffect(() => {
    const newErrors = {};

    if (!currentUser) newErrors.login = 'Please log in or sign up to continue.';
    if (stars <= 0 || stars > 5) newErrors.stars = 'Star rating must be between 1 and 5.';
    if (review.length <= 0) newErrors.review = 'Review is required.';
    if (review.length > 1000) newErrors.reviewLength = 'Review must be 1000 characters or less.';

    setErrors(newErrors);
  }, [currentUser, review, stars])

  const handleSubmit = async (e) => {
    e.preventDefault();

    const reviewData = {
      review,
      stars,
      recipe_id: RecipeId,
      user_id: userId
    }

    const createdReview = await dispatch(createReviewThunk(reviewData));

    if (createdReview) {
      setErrors([]);
      displayLanding()
      history.push(`/recipes/${RecipeId}`);
    }
  }
  return (
    <>
      <form className="AddRecipeForm"
        onSubmit={handleSubmit}>
        <div className='AddRecipeFormDiv'>
          <label className='AddRecipeFormRatingTitle' >Your rating:</label>
          <input
            type="number"
            placeholder="Stars"
            required
            value={stars}
            onChange={updateStars}
            className='AddReviewFormStars'
          />
          <div className='AddReviewFormErrors'>{errors.stars}</div>
          <label className='AddReviewFormQuestion'>What did you think?</label>
          <textarea
            type="string"
            placeholder="Enter Your Review"
            required
            value={review}
            onChange={updateReview}
            className='AddReviewFormResponseInput'
          />
          <div className='AddReviewFormReviewError' >{errors.review}</div>
          <div className='AddReviewFormReviewLength'>{errors.reviewLength}</div>
        </div>

        {Object.values(errors).length ?
          <div className="AddReviewFormButtonDiv">
            <button onClick={displayLanding} className='AddReviewFormReviewButtonCancel'>Cancel</button>
             <button
              type="submit"
              disabled={true}
              className="AddReviewFormReviewButtonSubmit">Submit</button>
          </div>
          :
          <div className="AddReviewFormButtonDiv">
            <button onClick={displayLanding} className='AddReviewFormReviewButtonCancel'>Cancel</button>
            <button
              type="submit"
              className="AddReviewFormReviewButtonSubmit">Submit</button>
          </div>
        }
      </form>
    </>
  )
}

export default CreateReview;
