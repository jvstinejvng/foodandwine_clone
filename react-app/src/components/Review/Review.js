import React, { useEffect, useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { NavLink, useHistory, useParams } from 'react-router-dom'
import { getAllReviewsThunk, deleteReviewThunk } from '../../store/reviews'
import CreateReview from './AddReview'
import EditReview from './EditReview';


const Reviews = ({ display, setDisplay, displayLanding, dropToggle, setDropToggle }) => {

    const { id } = useParams()
    const dispatch = useDispatch();
    // const recipesDict = useSelector((state) => (state?.recipes))
    const reviewsArray = useSelector((state) => Object.values(state?.reviews))
    const reviewsByRecipeId = reviewsArray.filter(review => review.recipe_id == id)
    const currentUser = useSelector((state) => (state?.session?.user))

    function displayCreate() {
        setDisplay((display) => display = 'create')
        setDropToggle((dropToggle) => dropToggle = false)
    }

    function displayLanding() {
        setDisplay((display) => display = 'landing')
        setDropToggle((dropToggle) => dropToggle = false)
    }

    useEffect(() => {
        dispatch(getAllReviewsThunk())
    }, [dispatch])

    if (currentUser == null) {
        return null
    }

    const currentUserUsername = currentUser.username
    const currentUserId = currentUser.id
    const reviewOfCurrentUser = reviewsByRecipeId.filter(review => review.user_id == currentUserId)

    function updatedDate(date) {
        let dateArray = date.split(' ')
        dateArray.splice(-2, 2)
        let newArray = dateArray.join(' ')
        return newArray
    }


    function noReviews() {
        if (reviewsByRecipeId.length == 0) {
            return (
                <div>This Recipe hasn't been reviewed yet</div>
            )
        }
    }


    function currentUserReviewCheck() {
        if (reviewOfCurrentUser.length > 0) {
            const review = reviewOfCurrentUser[0].review
            const updated_at = reviewOfCurrentUser[0].updated_at
            const stars = reviewOfCurrentUser[0].stars
            const reviewId = reviewOfCurrentUser[0].id
            const reviewsUserIdArray = reviewsByRecipeId.map((review) => review.user_id)
            const currentUserReviewIndex = reviewsUserIdArray.indexOf(currentUserId)
            reviewsByRecipeId.splice(currentUserReviewIndex, 1)


            function deleteReview() {
                dispatch(deleteReviewThunk(reviewId))
                    .then(() => dispatch(getAllReviewsThunk()))
                setDropToggle((dropToggle) => dropToggle = false)
            }

            function editReview() {
                setDisplay((display) => display = 'edit')
                setDropToggle((dropToggle) => dropToggle = false)
            }


            return (
                <div className='ReviewDiv' >
                    {display === 'landing' ?
                        <div className='ReviewDiv' >
                            <div className='ReviewDiv'>
                                <div className='ReviewDiv'>Would you like to edit your review, {" "}</div>
                                <div className='ReviewDiv'></div>
                                <div className='ReviewDiv'>{currentUserUsername}?</div>
                            </div>
                            <div className='ReviewDiv'></div>
                            <div className='ReviewDiv'>
                                <div className='ReviewDiv'>
                                    <div className='ReviewDiv'>You rated</div>
                                    <div className='ReviewDiv'></div>
                                    <div className='ReviewDiv'></div>
                                    <div className='ReviewDiv'> {stars} </div>
                                    <div className='ReviewDiv'></div>
                                    {stars > 1 ?
                                        <div>
                                            <div className='ReviewDiv'> stars</div>
                                        </div>
                                        :
                                        <div>
                                            <div className='ReviewDiv'> star</div>
                                        </div>
                                    }
                                </div>
                                <div>
                                    <div className='ReviewDiv'>{updatedDate(updated_at)}</div>
                                </div>
                            </div>                
                            <div className='ReviewDiv' >"{review}"</div>
                            <div className='ReviewDiv'></div>
                            <button
                                onClick={editReview}
                                className='ReviewDiv'
                            >Edit Review</button>
                            <button
                                onClick={deleteReview}
                                className='ReviewDiv'
                            >Delete Review</button>
                            <div className='ReviewDiv' ></div>
                            <div className='ReviewDiv'></div>
                        </div>
                        : null}
                    <div className='ReviewDiv' ></div>

                    {display === 'edit' ?
                        <div>
                            <EditReview userId={currentUserId} RecipeId={id} displayLanding={displayLanding} userReview={review} userStars={stars} reviewOfCurrentUser={reviewOfCurrentUser} />
                        </div>
                        : null}
                    <div ></div>
                    {reviewsByRecipeId.map((review) =>
                        <div key={review.id} className='ReviewDiv'>
                            {display === 'landing' ?
                                <div className='ReviewDiv'>
                                    <div className='ReviewDiv'>
                                        <div className='ReviewDiv'>
                                            <div className='ReviewDiv'>{review.user.username}</div>
                                            <div className='ReviewDiv'></div>
                                            <div className='ReviewDiv'>rated it {review.stars}</div>
                                            <div className='ReviewDiv'></div>
                                            {review.stars > 1 ?
                                                <div>
                                                    <div className='ReviewDiv'> stars</div>
                                                </div>
                                                :
                                                <div>
                                                    <div className='ReviewDiv'> star</div>
                                                </div>
                                            }
                                        </div>
                                        <div>
                                        </div>
                                    </div>
                                    <div className='ReviewDiv'></div>
                                    <div>
                                        <div className='ReviewDiv'>"{review.review}"</div>
                                        <div className='ReviewDiv'></div>
                                    </div>
                                </div>
                                : null}
                        </div>

                    )}
                </div>
            )
        }


        else {
            return (
                <div className='ReviewDiv'>
                    {display === 'landing' ?
                        <div className='ReviewDiv'>
                            <div className='ReviewDiv alex_pad_bottom_5'>
                                <div className='ReviewDiv' >{currentUserUsername},</div>
                                <div className='ReviewDiv'></div>
                                <div className='ReviewDiv alex_font_14'>start your review of</div>
                                <div className='ReviewDiv'></div>
                            </div>
                            <div className='ReviewDiv'>
                                <button
                                    onClick={displayCreate}
                                    className='ReviewDiv'
                                >Write A Review
                                </button>
                            </div>
                        </div>

                        : null}

                    <div className='ReviewDiv'></div>


                    {display === 'create' ?
                        <div>
                            <CreateReview userId={currentUserId} RecipeId={id} displayLanding={displayLanding} />

                        </div>
                        : null}


                    {display === 'landing' ?
                        <div className='ReviewDiv'>
                            {reviewsByRecipeId.map((review) =>
                                <div key={review.id} className='ReviewDiv '>
                                    <div className='ReviewDiv'>
                                        <div className='ReviewDiv'>
                                            <div className='ReviewDiv'>{review.user.username}</div>
                                            <div className='ReviewDiv'></div>
                                            <div className='ReviewDiv'>rated it {review.stars}</div>
                                            <div className='ReviewDiv'></div>
                                            {review.stars > 1 ?
                                                <div>
                                                    <div className='ReviewDiv'> stars</div>
                                                </div>
                                                :
                                                <div>
                                                    <div className='ReviewDiv'> star</div>
                                                </div>
                                            }
                                        </div>
                                        <div>
                                            <div className='ReviewDiv'>{updatedDate(review.updated_at)}</div>
                                        </div>
                                    </div>
                                    <div className='ReviewDiv'></div>
                                    <div className='ReviewDiv'>"{review.review}"</div>
                                </div>
                            )}
                        </div>
                        : null}
                    {display === 'landing' ? <div>{noReviews()}</div> : null}
                </div>
            )
        }
    }

    return (
        <>
            <div>{currentUserReviewCheck()}</div>
        </>
    );
}


export default Reviews;
