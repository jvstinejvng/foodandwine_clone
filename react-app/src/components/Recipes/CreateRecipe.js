import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom"

import { postRecipeThunk } from '../../store/recipe'
import { getRecipesThunk } from '../../store/recipe'

import '../CSS/CreateRecipe.css'

function CreateRecipe() {

    const dispatch = useDispatch()
    const history = useHistory()
    const sessionUser = useSelector(state => state.session.user)

    const [title, setTitle] = useState('')
    const [description, setDescription] = useState('')
    const [image_url, setImage_url] = useState('')
    const [total_time, setTotal_time] = useState('')
    const [servings, setServings] = useState('')
    const [ingredients, setIngredients] = useState('')
    const [directions, setDirections] = useState('')

    const [recipe_id, setRecipe_id] = useState('')

    const [validationErrors, setValidationErrors] = useState([])
    const [submitted, setSubmitted] = useState(false)
    const [hasCreated, setHasCreated] = useState(false)

    useEffect(() => {
        const fetchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        fetchRecipes().catch(console.error)
    }, [dispatch])

    const filetypes_regex = /\.(gif|jpe?g|png|webp)$/

    useEffect(() => {
        let errors = []

        if (!title.length || title.length < 5) errors.push('Uh oh, your title is too short! Make it over 5 characters.')
        if (title.length > 50) errors.push('Uh oh, your title is too long! Make it less than 50 characters.')
        
        if (!image_url) errors.push('Please enter an image file for your recipe.')
        if (!(filetypes_regex).test(image_url)) errors.push('Please enter a filename ending in .jpg, .jpeg, .png, .gif, or .webp.')

        if (!total_time.length || total_time.length < 5) errors.push('Uh oh, your title is too short! Make it over 5 characters.')
        if (total_time.length > 50) errors.push('Uh oh, your title is too long! Make it less than 50 characters.')
        
        if (!description || description.length < 5) errors.push('Uh oh, your description is too short! Make it over 5 characters.')
        if (description.length > 2000) errors.push('Uh oh, your description is too long! Make it less than 2000 characters.')

        if (!servings || servings.length < 3) errors.push('Total yield is too short! Make it over 3 characters.')
        if (servings.length > 50) errors.push('Total yield is too long! Make it less than 50 characters.')

        if (!ingredients || ingredients.length < 5) errors.push('Uh oh, your description is too short! Make it over 5 characters.')
        if (ingredients.length > 10000) errors.push('Uh oh, your description is too long! Make it less than 2000 characters.')

        if (!directions || directions.length < 5) errors.push('Uh oh, your description is too short! Make it over 5 characters.')
        if (directions.length > 10000) errors.push('Uh oh, your description is too long! Make it less than 2000 characters.')


        setValidationErrors(errors)
    }, [title, description, image_url, servings, ingredients, directions])


    const handleSubmit = async(e) => {
        e.preventDefault()

        setSubmitted(true)
        if (validationErrors.length) return
        
        const payload = {
            user_id: sessionUser.id,
            title,
            image_url,
            description,
            total_time,
            servings,
            ingredients,
            directions
        }

        try {
            const data = await dispatch(postRecipeThunk(payload))
            if (data) {
                setRecipe_id(data.id)
                setHasCreated(true)
                setTitle('')
                setDescription('')
                setImage_url('')
                setTotal_time('')
                setServings('')
                setIngredients('')
                setDirections('')
                setSubmitted(false)
                history.push(`/recipes/${data.id}`)
            }
        } catch (e) {
            setValidationErrors(e.errors)
        }
    }


    return (
        <div className='CreateReviewDiv'>
            <div className='CreateReviewHeaderDiv'>
                <h1 className='CreateReviewHeader'>Recipe</h1>
            </div>
                {submitted && validationErrors.length > 0 &&
                    <div className='CreateReviewErrors'>
                        <div className='CreateReviewErrorText'>Errors</div>
                            <ul className='CreateReviewErrorList'>
                                {validationErrors.map(error => (
                                    <li key={error}>{error}</li>
                                 ))}
                            </ul>
                    </div>
                }
        <form className='CreateReviewForm' onSubmit={handleSubmit}>
                <div className='CreateReviewFormInputDiv'>
                    <div className="CreateReviewFormInput">
                        <label>Title</label>
                        <input
                            name='title'
                            type='string'
                            placeholder="Title"
                            required
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                        />
                    </div>
                    <div className="CreateReviewFormInput">
                        <label>Description</label>
                        <textarea
                            name='description'
                            placeholder='"Share the story behind your recipe and what makes it special'
                            required
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                        />
                    </div>
                    <div className="CreateReviewFormInput">
                        <label>Image Link</label>
                        <input
                            name='image'
                            type='text'
                            placeholder='Use JPG, JPEG, PNG, TIFF'
                            value={image_url}
                            onChange={(e) => setImage_url(e.target.value)}
                        />
                    </div>
                    <div className="CreateReviewFormInput">
                        <label>Total Time</label>
                        <input
                            type='text'
                            name='servings'
                            placeholder="e.g. 4 servings"
                            required
                            value={total_time}
                            onChange={(e) => setTotal_time(e.target.value)}
                        />
                    </div>
                    <div className="CreateReviewFormInput">
                        <label>Servings</label>
                        <input
                            type='text'
                            name='servings'
                            placeholder="e.g. 4 servings"
                            required
                            value={servings}
                            onChange={(e) => setServings(e.target.value)}
                        />
                    </div>
                    <div className="CreateReviewFormInput">
                        <label>Ingredients</label>
                        <textarea
                            name='description'
                            placeholder='"Share the story behind your recipe and what makes it special'
                            required
                            value={ingredients}
                            onChange={(e) => setIngredients(e.target.value)}
                        />
                    </div>
                    <div className="CreateReviewFormInput">
                        <label>Directions</label>
                        <textarea
                            name='description'
                            placeholder='"Share the story behind your recipe and what makes it special'
                            required
                            value={directions}
                            onChange={(e) => setDirections(e.target.value)}
                        />
                    </div>

                </div>   
                <div className='CreateRecipeContainerButton'>
                    <button className='CreateRecipeButton'>sumbit</button>
                </div>
            </form>
        </div>
    )
}

export default CreateRecipe
