import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from "react-redux"
import { useHistory } from "react-router-dom"

import { postRecipeThunk } from '../../store/recipe'
// import { getRecipesThunk } from '../../store/recipe'

// import exclamation from '../../images/exclamation.svg'
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
            newErrors["title"] = "❗ What's your recipe called? Your title input must be more than 5 characters.";
        } else if (title.length > 150) {
            newErrors["title"] = "❗ Uh oh, you have exceeded the 150 character limit.";
        }
        if (description.length <= 10) {
            newErrors["description"] = "❗ How would you describe this recipe? Your description input must be more than 10 characters.";
        } else if (description.length > 1000) {
            newErrors["description"] = "❗ Uh oh, you have exceeded the 1000 character limit.";
        }
        if (!isValidImageUrl(image_url)) {
            newErrors["image_url"] = '❗ Your recipe\'s image URL input must end in .jpg, .jpeg, .png, or .tiff';
        }
        if (total_time.length <= 5) {
            newErrors["total_time"] = "❗ How long does it take to make your recipe? Your total time input must be more than 5 characters.";
        } else if (total_time.length > 50) {
            newErrors["total_time"] = "❗ Uh oh, you have exceeded the 50 character limit.";
        }
        if (servings.length <= 5) {
            newErrors["servings"] = "❗ How many servings does your recipe yield? Your servings input must be more than 5 characters.";
        } else if (servings.length > 50) {
            newErrors["servings"] = "❗ Uh oh, you have exceeded the 50 character limit.";
        }
        if (ingredients.length <= 1) {
            newErrors["ingredients"] = "❗ What ingredients do you need for this recipe? Please separate each ingredient with a comma. e.g. 1 cup flour, 1/3 cup sugar";
        } else if (ingredients.length <= 3) {
            newErrors["ingredients"] = "❗ Your ingredeints input must be more than 3 characters.";
        } else if (ingredients.indexOf(',') <= 1) {
            newErrors["ingredients"] = "❗ Please include a comma after your ingredient.";
        } else if (ingredients.length > 10000) {
            newErrors["ingredients"] = "❗ Uh oh, you have exceeded the 10,000 character limit.";
        } else if (ingredients.endsWith(',') <= 0) {
            newErrors["ingredients"] = "❗ Finished with adding all your recipe's ingredients? Please add a comma to the end of your input.";
        }
        if (directions.length <= 1) {
            newErrors["directions"] = "❗ What are the steps for making this recipe? Please end every step with a period. e.g. Preheat oven to 350 degrees fahrenheit. Mix the flour and sugar together.";
        } else if (directions.length <= 10) {
            newErrors["directions"] = "❗ Your directions input must be more than 10 characters.";
        } else if (directions.indexOf('.') <= 1){
            newErrors["directions"] = "❗ Please include a period after your instructional step.";
        } else if (directions.length > 10000) {
            newErrors["directions"] = "❗ Uh oh, you have exceeded the 10,000 character limit.";
        }
        else if (directions.endsWith('.') <= 0){
            newErrors["directions"] = "❗ Finished with adding all your directions for your recipe? Please add a period to the end of your input.";
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
                    <p  className='AddARecipeHeaderSub'>Adding recipes to Bread & Butter guarantees you can always find them when you need them.</p>
                </div>
            <div className='RecipeFormContainer'>
            <form  className='RecipeFormContainerForm' onSubmit={handleSubmit}>
                <label>Recipe Title</label>
                    <input
                    className="CreateRecipeFormInputDiv"
                    type="string"
                    placeholder="Give your recipe a title"
                    required
                    value={title}
                    onChange={updateTitle}
                    />
                <div className="CreateRecipeError"> {validationErrors?.title}</div>
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
                <div className="CreateRecipeError" >{validationErrors?.description}</div>
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
                <div className="CreateRecipeError">{validationErrors?.image_url}</div>
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
                <div className="CreateRecipeError">{validationErrors?.total_time}</div>
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
                <div className="CreateRecipeError">{validationErrors?.servings}</div>
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
                <div className="CreateRecipeError">{validationErrors?.ingredients}</div>
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
                <div className="CreateRecipeError">{validationErrors?.directions}</div>
                <div className='CreateFormGap'></div>
                <div className='AddARecipeButtonDiv'>
                <button
                  className='AddARecipeButton' 
                  type='submit'
                  disabled={
                    Object.values(validationErrors).every((x) => x === "") ? false : true
                  }
                  >Submit Recipe
                </button>
                </div>  
            </form>
            </div>
        </div>
        </div>
    )
}

export default CreateRecipe
