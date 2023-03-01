import { useEffect, useState } from 'react'
import { useDispatch} from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import '../CSS/EditIngredient.css'

function EditIngredient({ ingredient, measurementUnits, recipe_id, showEdit1, setShowEdit1}) {

    const dispatch = useDispatch()

    const [amount, setAmount] = useState(ingredient.amount)
    const [unit, setUnit] = useState(ingredient.measurement_unit.id)
    const [food_stuff, setFood_stuff] = useState(ingredient.food_stuff)
    const [hasSubmitted, setHasSubmitted] = useState(false)
    const [validationErrors, setValidationErrors] = useState([])

    useEffect(() => {
        let errors = []

        if (amount > 10000) errors.push('')

        if (food_stuff.length < 2) errors.push('')
        if (food_stuff.length > 50) errors.push('Please enter less than 50 characters into ingeredient name.')

        setValidationErrors(errors)
    }, [amount, unit, food_stuff])


    const handleSubmit = async (e) => {
        e.preventDefault()

        const payload = {
            amount,
            food_stuff,
            measurement_unit_id: unit,
            recipe_id
        }

        setHasSubmitted(true)
        if (validationErrors.length) return

        try {
            const res = await fetch(`/api/recipes/ingredients/${ingredient.id}`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(payload)
            })
            if (res.ok) {
                const data = await res.json()
                setShowEdit1(!showEdit1)            }

            await dispatch(getRecipesThunk())
        } catch (e) {
            setValidationErrors(e.errors)
        }
    }

    return (
    <div>
        { validationErrors.length > 0 &&
            <ul className=''>
                { validationErrors.map(error => (
                    <li className='' key={error}>{error}</li>
                ))}
            </ul>
        }
    <form className="" onSubmit={handleSubmit}>
        <div className='EditIngredientDiv'>
        <div className="">
            <input
                type="text"
                pattern="[0-9/]*"
                placeholder=" "
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                />
            <label>Quantity</label>
        </div>
        <div className=""> 
            <select
                type="number"
                placeholder={ingredient.measurement_unit}
                required
                value={unit}
                onChange={(e) => setUnit(e.target.value)}
            >
            {measurementUnits && (
                Object.values(measurementUnits).map(unit => (
                    <option key={unit.id} value={unit.id}>{unit.unit}</option>
                )))}
            </select>
            <label>Unit</label>
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
        <div className=''>
            <span onClick={() => setShowEdit1(!showEdit1)} className=''>Cancel</span>
                <button type='submit' className=''>Submit</button>
        </div>
        </div>
        </form>
    </div>
    )
}

export default EditIngredient
