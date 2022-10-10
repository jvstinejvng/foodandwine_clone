import { useEffect, useState } from 'react'
import { useDispatch, useSelector } from "react-redux"

import { editRecipeThunk } from '../../store/recipe'

import '../CSS/EditRecipe.css'

function EditRecipe( {recipe, setShowEditForm} ) {

    const dispatch = useDispatch()
    const sessionUser = useSelector(state => state.session.user)

    const [validationErrors, setValidationErrors] = useState({
        title: "",
        description: "",
        image_url: "",
        total_time: "",
        servings: "",
        ingredients: "",
        directions: ""
    });

    const [title, setTitle] = useState(recipe.title)
    const [description, setDescription] = useState(recipe.description)
    const [image_url, setImage_url] = useState(recipe.image_url)
    const [total_time, setTotal_time] = useState(recipe.total_time)
    const [ingredients, setIngredients] = useState(recipe.ingredients)
    const [directions, setDirections] = useState(recipe.directions)
    const [servings, setServings] = useState(recipe.servings)

    const [submitted, setSubmitted] = useState(false)

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
        if (!validationErrors) return

        const payload = {
            id: recipe.id,
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
            const data = await dispatch(editRecipeThunk(payload))
            if (data) setShowEditForm(false)
        } catch (e) {
            // setValidationErrors(e.errors)
        }
    }

    return (
        <>
        <div className='EditRecipeDiv'>
            <div className="EditRecipeForm">
                <div className='EditRecipeFormHeader'>Edit Your Recipe:</div>            
                <form className='EditRecipeFormDiv' onSubmit={handleSubmit}>
                    <label className="EditRecipeFormLabel">Recipe Title</label>
                        <input
                            className="EditRecipeString"
                            required
                            type="string"
                            placeholder="Give your recipe a title"
                            value={title}
                            onChange={updateTitle}
                        />
                                <div className='RecipeValidationError'>{validationErrors?.title}</div>
                    <label className="EditRecipeFormLabel">Description</label>
                        <textarea
                            className="EditRecipetextarea"
                            required
                            type="string"
                            placeholder="Share the story behind your recipe and what makes it special."
                            value={description}
                            onChange={updateDescription}
                        />
                                <div className='RecipeValidationError'>{validationErrors?.description}</div>
                    <label className="EditRecipeFormLabel">Recipe Image URL</label>
                        <input
                            className="EditRecipeString"
                            required
                            type="string"
                            placeholder="Supports image URLs ending with JPG, JPEG, PNG, TIFF"
                            value={image_url}
                            onChange={updateImageUrl}
                            />
                                <div className='RecipeValidationError'>{validationErrors?.image_url}</div>
                    <label className="EditRecipeFormLabel">Total Time</label>
                        <input
                            className="EditRecipeString"
                            required
                            type="string"
                            placeholder="e.g. 2 hours"
                            value={total_time}
                            onChange={updateTotalTime}
                        />
                                <div className='RecipeValidationError'>{validationErrors?.total_time}</div>
                <div className='EditRecipeSpace'></div>
                <label className="EditRecipeFormLabel">Yield</label>
                        <input
                            className="EditRecipeString"
                            required
                            placeholder="e.g. 4 servings"
                            value={servings}
                            onChange={updateServings}
                        />
                                <div className='RecipeValidationError'>{validationErrors?.servings}</div>
                <label className="EditRecipeFormLabel">Ingredients</label>
                        <textarea
                            className="EditRecipetextarea"
                            required
                            type="string"
                            placeholder="e.g. 2 tablespoon soften butter, 4 cups sifted flour,"
                            value={ingredients}
                            onChange={updateIngredients}
                        />
                         <div className='RecipeValidationError'>{validationErrors?.ingredients}</div>
                <label className="EditRecipeFormLabel" >Directions</label>
                        <textarea
                            className="EditRecipetextarea"
                            required
                            type="string"
                            placeholder="e.g. Combine all the dry ingredients in a large bowl. Mix the soften butter into the cake batter."
                            value={directions}
                            onChange={updateDirections}
                        />
                            <div className='RecipeValidationError'>{validationErrors?.directions}</div>
                <div className='EditButtonDiv'>
                <button className='EditRecipeButton' 
                        type='submit'
                        disabled={
                        Object.values(validationErrors).every((x) => x === "") ? false : true
                        }
                >Submit Recipe</button> 
                </div> 
                </form>
            </div>
        </div>
        </>
    )
}

export default EditRecipe
