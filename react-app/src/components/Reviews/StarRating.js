import React, { useState } from 'react'
import { FaStar } from 'react-icons/fa'

import '../CSS/StarRating.css'

function StarRating({ rating, setRating }) {

    const [hover, setHover] = useState(null)

    return (
        <div className='StarContainer'>
            {[...Array(5)].map((_star, idx) => {
                const ratingValue = idx
                return (
                    <label key={idx} className='star-label'>
                        <input
                            type='radio'
                            name='rating'
                            value={ratingValue}
                            onClick={() => setRating(ratingValue + 1)}
                            />
                        <FaStar
                            color={ratingValue < (hover || rating) ? '#000000': '#DCDCDC'}
                            size={100}
                            className='star'
                            onMouseOver={() => setHover(ratingValue + 1)}
                            onMouseLeave={() => setHover(null)}
                            />
                    </label>
                )
            })}
        </div>
    )
}

export default StarRating;
