import { useEffect, useState } from 'react'
import { useDispatch } from "react-redux"
import { getRecipesThunk } from '../../store/recipe'
import '../CSS/EditDirection.css'

function EditDirection({ instruction, recipe_id, showEdit2, setShowEdit2 }) {

    const dispatch = useDispatch()

    const [list_order, setList_order] = useState(instruction.list_order)
    const [specification, setSpecification] = useState(instruction.specification)
    const [hasSubmitted, setHasSubmitted] = useState(false)
    const [validationErrors, setValidationErrors] = useState([])

    useEffect(() => {
        let errors = []

        if (!specification) errors.push('')
        if (specification.length < 4) errors.push('')
        if (specification.length > 999) errors.push('')

        setValidationErrors(errors)
    }, [specification])

    const handleSubmit = async(e) => {
        e.preventDefault()

        const payload = {
            list_order,
            specification,
            recipe_id
        }

        setHasSubmitted(true)
        if (validationErrors.length) return

        try {
            const res = await fetch(`/api/recipes/instructions/${instruction.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })

            if (res.ok) {
                const data = await res.json()
                setShowEdit2(!showEdit2)
                await dispatch(getRecipesThunk())
            }
        } catch (e) {
            setValidationErrors(e.errors)
        }
    }

    return (
    <div className='EditDirectionDiv'>
        <div>
            { validationErrors.length > 0 &&
                <ul className=''>
                    { validationErrors.map(error => (
                        <li key={error}>{error}</li>
                    ))}
                </ul>
            }
        </div>
        <form onSubmit={handleSubmit}>
            <textarea
                className='EditDirectionTextArea'
                placeholder=""
                required
                value={specification}
                onChange={(e)=> setSpecification(e.target.value)}
            >
            </textarea>
            <div className='EditDirectionButtonDiv'>
                <button className='EditDirectionButtonCancel' onClick={() => setShowEdit2(!showEdit2)}>Cancel</button>
                <button className='EditDirectionButton' type='submit' >Save</button>
            </div>
        </form>
    </div>
    )
}

export default EditDirection
