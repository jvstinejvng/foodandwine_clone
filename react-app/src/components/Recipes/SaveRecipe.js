import { useEffect, useState } from "react"
import { useDispatch, useSelector } from "react-redux"
import { Link } from 'react-router-dom';
import { getRecipesThunk } from "../../store/recipe"
import '../CSS/SavedRecipe.css'

function SaveRecipe( {recipe} ) {

    const sessionUser = useSelector(state => state.session.user)
    const dispatch = useDispatch()

    const [owner, setOwner] = useState(false)
    const [hover, setHover] = useState(false)
    const [save, setSave] = useState(false)

    let user_id;
    if (sessionUser) { user_id = sessionUser.id }

    useEffect(() => {
        if (!owner) {
            for (let save of recipe.saves) {
                if (save.id === user_id) { setSave(true) }
            }
        }
        if (user_id === recipe.user.id) { setOwner(true) }
    },[user_id, recipe.saves])

    const handleSave = async (e) => {

        e.preventDefault()
        setSave(true)

        const payload = { user_id }

        try {
            const res = await fetch(`/api/recipes/${recipe.id}/save`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json'},
                body: JSON.stringify(payload)
            })
            if (res.ok) {
                await dispatch(getRecipesThunk())
            }
        } catch (e) {
            alert('Failed to Save Recipe, Please Try Again')
        }
    }

    const handleUnSave = async (e) => {

        e.preventDefault()
        setSave(false)

        const payload = { user_id }

        try {
            const res = await fetch(`/api/recipes/${recipe.id}/unsave`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
            if (res.ok) {
                await dispatch(getRecipesThunk())
            }
        } catch (e) {
            alert('Failed to Unsave Recipe, Please Try Again')
        }
    }

    if (!sessionUser) {
        return (
            <div>
                <Link to='/log-in'>          
                <div
                    id='NotUserSave'
                    className={`${hover ? 'fa-solid' : 'fa-regular'} fa-bookmark`}
                    onMouseEnter={() => setHover(true)}
                    onMouseLeave={() => setHover(false)}> 
                    <span className='NotUserSaveText'>Log In to save this Recipe!</span>
                </div>
                </Link>
            </div>
        )
    }

    if (owner) {
        return (
                <div id="RecipeOwner" class="fa-solid fa-pen">
                    <span className="RecipeOwnerText" >You published this recipe</span>
                </div>
        )
    }
  
    return (
        <>
        { save ?
            <div
                id="BookmarkIcon"
                className="fa-solid fa-bookmark"
                onClick={handleUnSave}>
            </div>
            :
            <div
                id="BookmarkIcon"
                className={`${hover ? 'fa-solid' : 'fa-regular'} fa-bookmark`}
                onMouseEnter={() => setHover(true)}
                onMouseLeave={() => setHover(false)}
                onClick={handleSave}> 
            </div>
        }
        </>
    )
}

export default SaveRecipe
