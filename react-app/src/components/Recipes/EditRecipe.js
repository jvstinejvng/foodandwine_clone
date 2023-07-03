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
    });

    const [title, setTitle] = useState(recipe.title)
    const [description, setDescription] = useState(recipe.description)
    const [image_url, setImage_url] = useState(recipe.image_url)
    const [total_time, setTotal_time] = useState(recipe.total_time)
  
    const [servings, setServings] = useState(recipe.servings)

    const [submitted, setSubmitted] = useState(false)

    const updateTitle = (e) => setTitle(e.target.value);
    const updateDescription = (e) => setDescription(e.target.value);
    const updateImageUrl = (e) => setImage_url(e.target.value);
    const updateTotalTime = (e) => setTotal_time(e.target.value);
    const updateServings = (e) => setServings(e.target.value);


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
        } else if (title.length > 200) {
            newErrors["title"] = "❗ Uh oh, you have exceeded the 200 character limit.";
        }
        if (description.length <= 10) {
            newErrors["description"] = "❗ How would you describe this recipe? Your description input must be more than 10 characters.";
        } else if (description.length > 2000) {
            newErrors["description"] = "❗ Uh oh, you have exceeded the 2000 character limit.";
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
        setValidationErrors(newErrors);
      }, [title, description, image_url, total_time, servings, validationErrors.length]);

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
                <div className='EditRecipeFormHeader'>Edit Your Recipe</div>            
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
                <div className='EditButtonDiv'>
                <button className='EditRecipeButton' 
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
        </>
    )
}

export default EditRecipe
