import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom"

import { postRecipeThunk } from '../../store/recipe'
// import { getRecipesThunk } from '../../store/recipe'

import '../CSS/CreateRecipe.css'

function CreateRecipe() {

    const dispatch = useDispatch()
    const history = useHistory()
    const sessionUser = useSelector(state => state.session.user)
    const [validationErrors, setValidationErrors] = useState({
        title: "",
        description: "",
        image_url: "",
        total_time: "",
        servings: "",
        ingredients: "",
        directions: "",
    });


    const [title, setTitle] = useState('') 
    const [description, setDescription] = useState('')
    const [image_url, setImage_url] = useState('')
    const [total_time, setTotal_time] = useState('')
    const [servings, setServings] = useState('')
    const [ingredients, setIngredients] = useState('')
    const [directions, setDirections] = useState('')

    const [recipe_id, setRecipe_id] = useState('')

    const [submitted, setSubmitted] = useState(false)
    const [hasCreated, setHasCreated] = useState(false)

    const updateTitle = (e) => setTitle(e.target.value);
    const updateDescription = (e) => setDescription(e.target.value);
    const updateImageUrl = (e) => setImage_url(e.target.value);
    const updateTotalTime = (e) => setTotal_time(e.target.value);
    const updateServings = (e) => setServings(e.target.value);
    const updateIngredients = (e) => setIngredients(e.target.value);
    const updateDirections = (e) => setDirections(e.target.value);

    const isValidImageUrl = (string) => {
        const ValidImage = [".jpg", ".jpeg", ".png", ".tiff"];
            for (let i = 0; i < ValidImage.length; i++) {
                let suffix = ValidImage[i];
                if (string.endsWith(suffix)) {
                return true;
            }
        }
        return false;
    };

   
    useEffect(() => {
        const newErrors = {};
        if (title.length <= 5) {
            newErrors["title"] = "What's your recipe called? Title must be more than 6 characters";
        } else if (title.length >= 100) {
            newErrors["title"] = "Your recipe title must be 50 characters or less";
        }
        if (description.length <= 0) {
            newErrors["description"] = "How would you describe this recipe?";
        } else if (description.length <= 10) {
            newErrors["description"] = "Your recipe description must be more than 10 characters";
        }
        if (!isValidImageUrl(image_url)) {
            newErrors["image_url"] = 'Your recipe\'s image URL must end in .jpg, .jpeg, .png, or .tiff';
        }
        if (total_time.length <= 0) {
            newErrors["total_time"] = "How long does it take to make your recipe?";
        } else if (total_time.length >= 50) {
            newErrors["total_time"] = "Your CreateRecipeFormInputDiv must be 50 characters or less";
        }
        if (servings.length <= 0) {
            newErrors["servings"] = "How many servings does your recipe yield?";
        } else if (servings.length >= 50) {
            newErrors["servings"] = "Your CreateRecipeFormInputDiv must be 50 characters or less";
        }
        if (ingredients.indexOf(',') <= 1) {
            newErrors["ingredients"] = "You need to add a comma after an ingredient";
        } if (ingredients.endsWith(',') <= 0){
            newErrors["ingredients"] = "end with a comma";
        }
        else if (ingredients.length <= 5 ) {
            newErrors["ingredients"] = "Your recipe ingredients must be more than 5 character";
        }
        if (directions.indexOf('.') <= 1) {
            newErrors["directions"] = "Must include a period to your directions";
        } if (directions.endsWith('.') <= 0){
            newErrors["directions"] = "end with a period";
        } else if (directions.length <= 5) {
            newErrors["directions"] = "Your reciple directions must be more than 5 characters";
        }
        setValidationErrors(newErrors);
      }, [title, description, image_url, total_time, servings, ingredients, directions, validationErrors.length]);


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
            <div className='AddARecipeContainer'>
                <div className='AddARecipeHeaderDiv'>
                    <h1 className='AddARecipeHeader'>Add a Recipe</h1>
                    <p  className='AddARecipeHeaderSub' >Uploading personal recipes is easy! Add yours to your favorites, share with friends, family, or the Allrecipes community.</p>
                </div>
            <div className='RecipeFormContainer'>
            <form  className='RecipeFormContainerForm' onSubmit={handleSubmit}>
                <label>Recipe Title</label>
                    <textarea
                    className="CreateRecipeFormInputDiv"
                    type="string"
                    placeholder="Give your recipe a title"
                    required
                    value={title}
                    onChange={updateTitle}
                    />
                <div>{validationErrors?.title}</div>
                <div className='CreateFormGap'></div>
                <label>Description</label>
                    <textarea
                    className="CreateRecipeFormInputDiv"
                    type="string"
                    placeholder="Share the story behind your recipe and what makes it special"
                    required
                    value={description}
                    onChange={updateDescription}
                    />
                <div>{validationErrors?.description}</div>
                <div className='CreateFormGap'></div>
                <label>Recipe Image URL</label>
                    <input
                    className="CreateRecipeFormInputDiv"
                    type="string"
                    placeholder="Use JPG, JPEG, PNG, TIFF"
                    required
                    value={image_url}
                    onChange={updateImageUrl}
                    />
                <div>{validationErrors?.image_url}</div>
                <div className='CreateFormGap'></div>
                <label>Total Time</label>
                    <input
                    className="CreateRecipeFormInputDiv"
                    type="string"
                    placeholder="e.g. 2 hours"
                    required
                    value={total_time}
                    onChange={updateTotalTime}
                    />
                <div>{validationErrors?.total_time}</div>
                <div className='CreateFormGap'></div>
                <label>Yield</label>
                    <input
                    className="CreateRecipeFormInputDiv"
                    type="string"
                    placeholder="e.g. 4 servings"
                    required
                    value={servings}
                    onChange={updateServings}
                    />
                <div>{validationErrors?.servings}</div>
                <div className='CreateFormGap'></div>
                <label>Ingredients</label>
                    <textarea
                    className="CreateRecipeFormInputDiv"
                    type="string"
                    placeholder="e.g. 2 tablespoon soften butter, 4 cups sifted flour"
                    required
                    value={ingredients}
                    onChange={updateIngredients}
                    />
                <div>{validationErrors?.ingredients}</div>
                <div className='CreateFormGap'></div>
                <label>Directions</label>
                    <textarea
                    className="CreateRecipeFormInputDiv"
                    type="string"
                    placeholder="e.g. Combine all dry ingredients in a large bowl. Mix soften butter into the large bowl."
                    required
                    value={directions}
                    onChange={updateDirections}
                    />
                <div>{validationErrors?.directions}</div>
                <div className='CreateFormGap'></div>
                <button
                  className='AddARecipeButton' 
                  type='submit'
                  disabled={
                    Object.values(validationErrors).every((x) => x === "") ? false : true
                  }
                  >Submit Recipe
                </button>
                
            </form>
            </div>
        </div>
        </div>
    )
}

export default CreateRecipe
