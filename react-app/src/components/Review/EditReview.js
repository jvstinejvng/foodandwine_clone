import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useHistory } from "react-router-dom";
import { editReviewThunk, getAllReviewsThunk } from "../../store/reviews";

const EditReview = ({ recipeId, userId, userReview, userStars, displayLanding, reviewOfCurrentUser }) => {
  const dispatch = useDispatch();
  const history = useHistory();
  const currentUser = useSelector(state => state?.session?.user);
  const currentReviewId = reviewOfCurrentUser[0].id

  const [errors, setErrors] = useState([]);
  const [review, setReview] = useState(`${userReview}`);
  const [stars, setStars] = useState(`${userStars}`);

  const updateReview = (e) => setReview(e.target.value);
  const updateStars = (e) => setStars(e.target.value);

  useEffect(() => {
    dispatch(getAllReviewsThunk())
  }, [dispatch])

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
      id: currentReviewId,
      review,
      stars,
      recipe_id: recipeId,
      user_id: userId
    }

    const editedRecipe = await dispatch(editReviewThunk(reviewData));

    if (editedRecipe) {
      setErrors([]);
      displayLanding();
      history.push(`/recipes/${recipeId}`);
    }
  }
  return (
    <>
    
      <form
        className="EditRecipeForm"
        onSubmit={handleSubmit}>
        <div className='EditRecipeFormText'>
          <label className='EditRecipeFormTextStars'>Stars</label>
          <input
            type="integer"
            placeholder="Stars"
            required
            value={stars}
            onChange={updateStars}
            className='EditRecipeFormInput'
          />
          <div className='EditRecipeFormTextError'>{errors.stars}</div>
          <label className='EditRecipeFormText'></label>
          <textarea
            type="string"
            placeholder="Enter Your Review"
            required
            value={review}
            onChange={updateReview}
            className='EditRecipeFormTextInput'
          />
          <div className='EditRecipeFormError' >{errors.review}</div>
          <div className='EditRecipeFormError' >{errors.reviewLength}</div>
        </div>

        {Object.values(errors).length ?
          <div className="EditRecipeFormButton">
             <button
              type="submit"
              disabled={true}
              className="EditRecipeFormButtonDisabled">Submit</button>
            <button onClick={displayLanding} className='EditRecipeFormButtonCancel'>Cancel</button>
          </div>
          :
          <div className="EditRecipeFormButtonDiv">
            <button
              type="submit"
              className="EditRecipeFormButtonSubmit">Submit</button>
            <button onClick={displayLanding} className='EditRecipeFormButton'>Cancel</button>
          </div>
        }
      </form>
  
    </>

  )
}


export default EditReview;
