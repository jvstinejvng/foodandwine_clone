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

    let user_id
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
            <div id='LoggedOutSave'>
                <Link to='/log-in' className='' >
                    
                <i id='NotSaved'
                    className={`${hover ? 'fa-solid' : 'fa-regular'} fa-bookmark`}
                    onMouseEnter={() => setHover(true)}
                    onMouseLeave={() => setHover(false)}> 
                    Login to save this Recipe!
                </i>
                </Link>
            </div>
        )
    }

    if (owner) {
        return (
            <div id='LoggedOutSave'>
                <i id='NotSaved' class=" fa-solid fa-pen">You published this recipe</i>
            </div>
        )
    }

    return (
        <>
            { save ?
                <i id='liked'
                    className="fa-solid fa-bookmark"
                    title='Save this recipe!'
                    onClick={handleUnSave}>
                </i>
                :
                <i id='NotSaved'
                    className={`${hover ? 'fa-solid' : 'fa-regular'} fa-bookmark`}
                    title='Save this recipe!'
                    onMouseEnter={() => setHover(true)}
                    onMouseLeave={() => setHover(false)}
                    onClick={handleSave}> 
                </i>
            }
        </>
    )
}

export default SaveRecipe
