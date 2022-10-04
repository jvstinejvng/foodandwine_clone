// actions
const LOAD_REVIEWS = '/reviews/all_reviews'
const ADD_REVIEW = '/reviews/add_review'
const EDIT_REVIEW = '/reviews/edit_review'
const DELETE_REVIEW = '/reviews/delete_reviews'

const loadReviews = (reviews) => {
    return {
        type: LOAD_REVIEWS,
        reviews
    }
}

const addReview = (review) => {
    return {
        type: ADD_REVIEW,
        review
    }
}

const editReview = (review) => {
    return {
        type: EDIT_REVIEW,
        review
    }
}

const deleteReview = (review) => {
    return {
        type: DELETE_REVIEW,
        review
    }
}

// thunks
// load review 
export const loadReviewThunk = () => async (dispatch) => {
    const response = await fetch('/api/reviews/');
    if (response.ok) {
        const data = await response.json()
        dispatch(loadReviews(data.reviews));
    }
    else {
        const error = await response.json();
        throw error;
    }
}

// add review 
export const addReviewThunk = (review) => async (dispatch) => {
    const response = await fetch('/api/reviews/', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(review)
    })

    if (response.ok) {
        const data = await response.json()
        if (data.errors) {
            return
        }
        dispatch(addReview(data))
        return data
    }
}

// edit review 
export const editReviewThunk = (review) => async (dispatch) => {
    const response = await fetch(`/api/comments/${review.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify(review)
    })
    if (response.ok) {
        const data = await response.json()
        dispatch(editReview(data))
        return data
    } else {
        const error = await response.json()
        throw error
    }
}

export const deleteReviewThunk = (review) => async (dispatch) => {
    const response = await fetch(`/api/comments/${review.id}`, {
        method: 'DELETE'
    })
    if (response.ok) {
        const data = await response.json()
        if (data.message === "Review Deleted!") {
            dispatch(deleteReview(review))
        }
        return review
    } else {
        const error = await response.json()
        throw error
    }
}

// reducer
const initialState = {}
export default function review_reducer(state = initialState, action) {
    let newState = {...state}
    switch (action.type) {
      case LOAD_REVIEWS:
          newState = { ...state }
          action.reviews.forEach(review => newState[review.id] = review)
          return newState
      case ADD_REVIEW:
          newState = { ...state }
          newState[action.review.id] = action.review
          return newState
      case EDIT_REVIEW:
          newState = { ...state, [action.review.id]: action.review }
          return newState
      case DELETE_REVIEW:
          newState = { ...state }
          delete newState[action.review.id]
          return newState
      default:
        return state;
    }
  }
  
