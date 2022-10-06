import { useEffect, useState, useContext } from 'react'
import { useDispatch, useSelector } from "react-redux"

import { editRecipeThunk } from '../../store/recipe'

import '../CSS/EditRecipe.css'

function EditRecipe( {recipe, setShowEditForm} ) {

    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)
  
    const [title, setTitle] = useState(recipe.title)
    const [description, setDescription] = useState(recipe.description)
    const [image_url, setImage_url] = useState(recipe.image_url)
    const [total_time, setTotal_time] = useState('')
    const [servings, setServings] = useState('')
    const [ingredients, setIngredients] = useState('')
    const [directions, setDirections] = useState('')


    const [validationErrors, setValidationErrors] = useState([])
    const [submitted, setSubmitted] = useState(false)

    const filetypes_regex = /\.(gif|jpe?g|png|webp)$/

    //validations
    useEffect(() => {
        let errors = []

        if (!title.length || title.length < 5) errors.push('Uh oh, your title is too short! Make it over 5 characters.')
        if (title.length > 50) errors.push('Uh oh, your title is too long! Make it less than 50 characters.')

        if (!description || description.length < 5) errors.push('Uh oh, your description is too short! Make it over 5 characters.')
        if (description.length > 2000) errors.push('Uh oh, your description is too long! Make it less than 2000 characters.')

        if (!image_url) errors.push('Please enter an image file for your recipe.')
        if (!(filetypes_regex).test(image_url)) errors.push('Please enter a filename ending in .jpg, .jpeg, .png, .gif, or .webp.')

        if (!total_time.length || total_time.length < 5) errors.push('Uh oh, your title is too short! Make it over 5 characters.')
        if (total_time.length > 50) errors.push('Uh oh, your title is too long! Make it less than 50 characters.')
        
        if (!servings || servings.length < 3) errors.push('Total yield is too short! Make it over 3 characters.')
        if (servings.length > 50) errors.push('Total yield is too long! Make it less than 50 characters.')

        if (!ingredients || ingredients.length < 5) errors.push('Uh oh, your description is too short! Make it over 5 characters.')
        if (ingredients.length > 10000) errors.push('Uh oh, your description is too long! Make it less than 2000 characters.')

        if (!directions || directions.length < 5) errors.push('Uh oh, your description is too short! Make it over 5 characters.')
        if (directions.length > 10000) errors.push('Uh oh, your description is too long! Make it less than 2000 characters.')


        setValidationErrors(errors)
    }, [title, description, image_url, total_time, servings, ingredients, directions])


    const handleSubmit = async(e) => {
        e.preventDefault()

        setSubmitted(true)
        if (validationErrors.length) return


        const payload = {
            id: recipe.id,
            user_id: sessionUser.id,
            title,
            image_url,
            description,
            servings,
            ingredients,
            directions
        }
        try {
            const data = await dispatch(editRecipeThunk(payload))
            if (data) setShowEditForm(false)
        } catch (e) {
        }
    }

    return (
        <>
        <div className='EditRecipeDiv'>
                <div className='EditRecipeHeader' >Edit Recipe</div>
                        {validationErrors.length > 0 &&
                            <ul className='EditRecipeErrors'>
                            {validationErrors.map(error => (
                                <li className='EditRecipeErrors' key={error}>{error}</li>
                                ))}
                            </ul>
                        }
            <form className='EditRecipeFormDiv' onSubmit={handleSubmit}>
                <div className='EditRecipeFormInputDiv'>
                    <div className="EditRecipeFormInputSection">
                        <label>Title:</label>
                        <input
                            type='string'
                            placeholder='Title'
                            required
                            value={title}
                            onChange={(e) => setTitle(e.target.value)}
                            />
                    </div>
                    <div className="EditRecipeFormInputSection">
                        <label>Description:</label>
                        <input
                            type='string'
                            placeholder='Description'
                            required
                            value={description}
                            onChange={(e) => setDescription(e.target.value)}
                            />
                    </div>
                    <div className="EditRecipeFormInputSection">
                         <label>Image Link:</label>
                        <input
                            type='text'
                            placeholder='image'
                            value={image_url}
                            onChange={(e) => setImage_url(e.target.value)}
                            />
                    </div>
                    <div className="EditRecipeFormInputSection">
                        <label>Total Time</label>
                        <input
                            type='text'
                            placeholder="serving"
                            required
                            value={servings}
                            onChange={(e) => setTotal_time(e.target.value)}
                            />
                    </div>
                    <div className="EditRecipeFormInputSection">
                        <label>serving</label>
                        <input
                            type='text'
                            placeholder="serving"
                            required
                            value={servings}
                            onChange={(e) => setServings(e.target.value)}
                            />
                    </div>
                    <div className="EditRecipeFormInputSection">
                        <label>Ingredients:</label>
                        <input
                            type='string'
                            placeholder='ingredients'
                            required
                            value={ingredients}
                            onChange={(e) => setIngredients(e.target.value)}
                            />
                    </div>
                    <div className="EditRecipeFormInputSection">
                        <label>Directions:</label>
                        <input
                            type='string'
                            placeholder='directions'
                            required
                            value={directions}
                            onChange={(e) => setDirections(e.target.value)}
                            />
                    </div>
                </div>
                        <div className='EditRecipeFormButtonDiv'>
                            <button type='submit' className='EditRecipeFormButton' >Submit</button>
                        </div>
            </form>
            </div>
        </>
    )
}

export default EditRecipe
