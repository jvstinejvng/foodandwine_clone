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
    const [validationErrors, setValidationErrors] = useState({
        title: "",
        description: "",
        image_url: "",
        total_time: "",
        servings: "",
    });


    const [title, setTitle] = useState('') 
    const [description, setDescription] = useState('')
    const [image_url, setImage_url] = useState('')
    const [total_time, setTotal_time] = useState('')
    const [servings, setServings] = useState('')

    const [measurementUnits, setMeasurementUnits] = useState('')
    const [recipe_id, setRecipe_id] = useState('')
    const [submitted, setSubmitted] = useState(false)
    const [hasCreated, setHasCreated] = useState(false)

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
        async function fetchUnits() {
            const res = await fetch('/api/recipes/units')
            const data = await res.json()
            setMeasurementUnits(data.units)
        }
        fetchUnits()
    }, [])

    useEffect(() => {
        const fetchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        fetchRecipes().catch(console.error)
    }, [dispatch])

   
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
        if (validationErrors.length) return
        
        const payload = {
            user_id: sessionUser.id,
            title,
            image_url,
            description,
            total_time,
            servings,
  
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
