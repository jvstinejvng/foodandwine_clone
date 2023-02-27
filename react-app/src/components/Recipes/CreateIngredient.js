import { useEffect, useState } from 'react'
import { useDispatch} from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import '../CSS/CreateRecipeInfo.css'

function CreateIngredient({ recipe_id, measurementUnits, edit }) {

    const dispatch = useDispatch()
    const [amount, setAmount] = useState('')
    const [unit, setUnit] = useState(1)
    const [food_stuff, setFood_stuff] = useState('')
    const [hasSubmitted, setHasSubmitted] = useState(false)
    const [validationErrors, setValidationErrors] = useState([])
    const [ingredients, SetIngredients] = useState([])

    useEffect(() => {
        let errors = []
        if (food_stuff.length < 2) errors.push('')
        if (food_stuff.length > 50) errors.push('')

        setValidationErrors(errors)
    }, [ amount, unit, food_stuff])

    const handleSubmit = async(e) => {
        e.preventDefault()

        setHasSubmitted(true)
        if (validationErrors.length) return

        const payload = {
            amount,
            food_stuff,
            measurement_unit_id: unit,
            recipe_id
        }

        setHasSubmitted(false)

        try {
            const res = await fetch('/api/recipes/ingredients', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(payload)
            })

            if (res.ok) {
                const data = await res.json()
                if (data) {
                    SetIngredients([...ingredients, data])
                    setAmount('')
                    setFood_stuff('')
                    setUnit(1)
                    await dispatch(getRecipesThunk())
                }
            }
        } catch (e) {
            setValidationErrors(e.errors)
        }
    }

    return (
        <>
        <h3>Add Ingredients!</h3>
        { hasSubmitted && validationErrors.length > 0 &&
                <ul className=''>
                    {validationErrors.map(error => (
                        <li className='' key={error}>{error}</li>
                    ))}
                </ul>
        }
        { !edit && ingredients.length > 0 ?
            <ul>
                { Object.values(ingredients).map(ingredient => (
                    <li key={ingredient.id}>
                        <p> {ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}</p>
                    </li>
                ))}
            </ul>
            :
            null
        }
        <form className="RecipeInfoForm" onSubmit={handleSubmit}>
            <div className='add-IngredientInputDiv'>
            <div className="">
                <input
                    type="number"
                    placeholder=""
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                    min={undefined}
                    max="1000"

                />
                <label>quality</label>
            </div>
            <div className="">
                <select
                    type="number"
                    placeholder="0"
                    required
                    value={unit}
                    onChange={(e) => setUnit(e.target.value)}
                >
                    { measurementUnits && (
                        Object.values(measurementUnits).map(unit => (
                        <option key={unit.id} value={unit.id}>{unit.unit}</option>
                        ))
                    )}
                </select>
                <label>Unit:</label>
            </div>
            <div className="">
                <input
                    type="text"
                    placeholder=""
                    required
                    value={food_stuff}
                    onChange={(e) => setFood_stuff(e.target.value)}
                />
                <label>Ingredient</label>
            </div>
            </div>
            <div className='AddButton'>
                <div className='next-button-container add-button'>
                    <h3 className=''>Add</h3>
                    <button className=''>
                        <i className="fa-solid fa-plus add"></i>
                    </button>
                </div>
             </div>
            </form>
        </>
    )
}

export default CreateIngredient
