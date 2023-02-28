import { useEffect, useState } from 'react'
import { useDispatch } from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import '../CSS/CreateRecipeInfo.css'

function CreateDirection({ recipe_id, existing_order, edit }) {
    
    const dispatch = useDispatch()

    const [list_order, setList_order] = useState(!existing_order ? 1 : existing_order + 1)
    const [specification, setSpecification] = useState('')
    const [hasSubmitted, setHasSubmitted] = useState(false)
    const [validationErrors, setValidationErrors] = useState([])
    const [instructions, SetInstructions] = useState([])

    useEffect(() => {
        let errors = []

        if (!specification) errors.push('')
        if (specification.length < 4) errors.push('')
        if (specification.length > 1000) errors.push('')

        setValidationErrors(errors)
    }, [specification])

    const handleSubmit = async(e) => {

        e.preventDefault()
        setHasSubmitted(true)
        if (validationErrors.length) return

        const payload = {
            list_order,
            specification,
            recipe_id
        }

        setHasSubmitted(false)

        try {
            const res = await fetch('/api/recipes/instructions', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })

            if (res.ok) {
                const data = await res.json()
                await dispatch(getRecipesThunk())
                SetInstructions([...instructions, data])
                setList_order(list_order + 1)
                setSpecification('')
            }
        } catch (e) {
            setValidationErrors(e.errors)
        }
    }

    return (
        <>
        <h3>Add Directions!</h3>
        { hasSubmitted && validationErrors.length > 0 &&
            <ul className=''>
                { validationErrors.map(error => (
                <li className='' key={error}>{error}</li>
                ))}
            </ul>
        }
        { !edit && instructions.length > 0 ?
            <ol>
                {Object.values(instructions).map(instruction => (
                    <li key={instruction.id}>
                        <p>{instruction.specification}</p>
                    </li>
                ))}
            </ol>
            :
            null
        }
        <form onSubmit={handleSubmit} className="RecipeInfoForm" >
        <div className="DirectionFormInput">
            <div className="">
                <textarea
                    placeholder=""
                    required
                    value={specification}
                    onChange={(e)=> setSpecification(e.target.value)}
                >
                </textarea>
                <label></label>
            </div>
        </div>
        <div className='AddButton'>
            <div className=''>
                <h3 className=''></h3>
                <button className=''>
                    <i className="fa-solid fa-plus add"></i>
                </button>
            </div>
        </div>
        </form>
        </>
    )
}

export default CreateDirection
