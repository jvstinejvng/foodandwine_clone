import React, { useEffect, useState } from 'react';
import { useHistory } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { addRecipeThunk } from '../../store/recipes';
import '../CSS/AddRecipe.css'


 function AddRecipe() {

    const sessionUser = useSelector(state => state.session.user);
    const dispatch = useDispatch();
    const history = useHistory();
    const [errors, setErrors] = useState({
        title: "",
        description: "",
        imageUrl: "",
        time: "",
        servings: "",
        ingredients: "",
        directions: "",
    });
    const [submitted, setSubmitted] = useState(false);
    
    const [title, setTitle] = useState('');
    const [description, setDescription] = useState('');
    const [imageUrl, setImageUrl] = useState('');
    const [totalTime, setTotalTime] = useState('');
    const [servings, setServings] = useState('');
    const [ingredients, setIngredients] = useState('');
    const [directions, setDirections] = useState('');

    const updateTitle = (e) => setTitle(e.target.value);
    const updateDescription = (e) => setDescription(e.target.value);
    const updateImageUrl = (e) => setImageUrl(e.target.value);
    const updateTotalTime = (e) => setTotalTime(e.target.value);
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
        if (title.length <= 0) {
            newErrors["title"] = "What's your recipe called?";
        } else if (title.length >= 255) {
            newErrors["title"] = "Your recipe title must be 255 characters or less";
        }
        if (description.length <= 0) {
            newErrors["description"] = "How would you describe this recipe?";
        } else if (description.length <= 5) {
            newErrors["title"] = "Your recipe description must be 10 characters or more";
        }
        if (!isValidImageUrl(imageUrl)) {
            newErrors["imageUrl"] = 'Your recipe\'s image URL must end in .jpg, .jpeg, .png, or .tiff';
        }
        if (totalTime.length <= 0) {
            newErrors["totalTime"] = "How long does it take to make your recipe?";
        } else if (totalTime.length >= 50) {
            newErrors["totalTime"] = "Your input must be 50 characters or less";
        }
        if (servings.length <= 0) {
            newErrors["servings"] = "How many servings does your recipe yield?";
        } else if (servings.length >= 50) {
            newErrors["servings"] = "Your input must be 50 characters or less";
        }
        if (ingredients.length <= 0) {
            newErrors["ingredients"] = "What ingredients do you need for this recipe? Please separate every ingredient with a comma. example: 1 cup flour, 1/3 cup sugar";
        } else if (ingredients.length <= 2) {
            newErrors["ingredients"] = "Your recipe ingredients must be 2 characters or more";
        }
        if (directions.length <= 0) {
            newErrors["directions"] = "What are the steps for making this recipe? Please use end sentences with a period. example: Mix the flour and sugar together.";
        } else if (directions.length <= 2) {
            newErrors["directions"] = "Your reciple directions must be 2 characters or more";
        }
        setErrors(newErrors);
      }, [title, description, imageUrl, totalTime, servings, ingredients, directions, errors.length]);

      const handleSubmit = async (e) => {
        e.preventDefault();
        setSubmitted(true)

        const data = {
          user_id: sessionUser.id,
          title,
          description,
          img_url: imageUrl,
          total_time: totalTime,
          servings,
          ingredients,
          directions
        };
    
       await dispatch(addRecipeThunk(data));
        history.push('/recipes/')
      };
    

    return (
    <>
        <div className='AddARecipeContainer'>
            <h1>Add a Recipe</h1>
            {submitted &&
                <div className='errors'>
                    <ul>
                        {errors.length > 0 && errors.map((error, i) => (
                            <li style={{color: 'red'}} key={i}>{error}</li>
                        ))}
                    </ul>
                </div>
            }
            <div className='RecipeFormContainer'>
            <form onSubmit={handleSubmit}>
                <label>Recipe Title</label>
                    <input
                    className="input"
                    type="string"
                    placeholder="Give your recipe a title"
                    required
                    value={title}
                    onChange={updateTitle}
                    />
                <div>{errors?.title}</div>
                <label>Description</label>
                    <input
                    className="input"
                    type="string"
                    placeholder="Share the story behind your recipe and what makes it special"
                    required
                    value={description}
                    onChange={updateDescription}
                    />
                <div>{errors?.description}</div>
                <label>Recipe Image URL</label>
                    <input
                    className="input"
                    type="string"
                    placeholder="Use JPG, JPEG, PNG, TIFF"
                    required
                    value={imageUrl}
                    onChange={updateImageUrl}
                    />
                <div>{errors?.imageUrl}</div>
                <label>Total Time</label>
                    <input
                    className="input"
                    type="string"
                    placeholder="e.g. 2 hours"
                    required
                    value={totalTime}
                    onChange={updateTotalTime}
                    />
                <div>{errors?.totalTime}</div>
                <label>Yield</label>
                    <input
                    className="input"
                    type="string"
                    placeholder="e.g. 4 servings"
                    required
                    value={servings}
                    onChange={updateServings}
                    />
                <div>{errors?.servings}</div>
                <label>Ingredients</label>
                    <input
                    className="input"
                    type="string"
                    placeholder="e.g. 2 tablespoon soften butter, 4 cups sifted flour"
                    required
                    value={ingredients}
                    onChange={updateIngredients}
                    />
                <div>{errors?.ingredients}</div>
                <label>Directions</label>
                    <input
                    className="input"
                    type="string"
                    placeholder="e.g. Combine all dry ingredients in a large bowl. Mix soften butter into the large bowl."
                    required
                    value={directions}
                    onChange={updateDirections}
                    />
                <div>{errors?.directions}</div>                
                <button className='AddARecipeButton' type='submit'>Submit Recipe</button>
            </form>
            </div>
        </div>
    </>
    );
}

export default AddRecipe
