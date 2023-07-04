import { useEffect, useState } from 'react'
import { useDispatch} from "react-redux"
import { getRecipesThunk } from '../../store/recipe'
import '../CSS/CreateIngredient.css'

function CreateIngredient({ recipe_id, measurementUnits }) {

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
        <h3 className='create-ingredient-title'>Enter Ingredients Below</h3>
        { hasSubmitted && validationErrors.length > 0 &&
                <ul className='create-ingredient-errors'>
                    {validationErrors.map(error => (
                        <li className='' key={error}>{error}</li>
                    ))}
                </ul>
        }
        <form className="create-ingredient-form" onSubmit={handleSubmit}>
            <span className="ingredient-form-span">
                <input
                    className="ingredient-form-input"
                    type="text"
                    pattern="^[0-9 /]*$" 
                    placeholder=""
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                    max="1000"

                />
                <label className="ingredient-form-label">Quality</label>
            </span>
            <span className="ingredient-form-span">
                <select
                    className="ingredient-form-input"
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
                <label className="ingredient-form-label">Unit</label>
            </span>
            <span className="ingredient-form-span">
                <input
                    className="ingredient-form-input"
                    type="text"
                    placeholder=""
                    required
                    value={food_stuff}
                    onChange={(e) => setFood_stuff(e.target.value)}
                />
                <label className="ingredient-form-label">Ingredient</label>
            </span>
            <div>
                <button className='create-ingredient-add-button'>
                    <i className="fa-solid fa-plus add"></i>
                    <span className='add-ingredient-text'>add ingredient</span>
                </button>
            </div>
            </form>
            
        </>
    )
}

export default CreateIngredient
