import { useEffect, useState } from 'react'
import { useDispatch} from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import EditIngredient from './EditIngredient'

function Ingredient({ recipe, ingredient, showEditIngredientredient, measurementUnits }) {

    const dispatch = useDispatch()
    const [showEdit1, setShowEdit1] = useState()

    const handleDelete = async(e) => {
        e.preventDefault()

        try {
            const res = await fetch(`/api/recipes/ingredients/${ingredient.id}`, {
                method: 'DELETE'
            })

            await dispatch(getRecipesThunk())
        } catch (e) {
            console.log('delete ingredient failed! ' + e)
        }
    }

    return (
        (showEditIngredientredient && showEdit1 ?
        <EditIngredient
            ingredient={ingredient}
            measurementUnits={measurementUnits}
            recipe_id={recipe.id}
            showEdit1={showEdit1}
            setShowEdit1={setShowEdit1}
            />
        :
        showEditIngredientredient ?
            <div className='ingredient-container'>
                <p>{ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}</p>
                <div>
                    <div onClick={() => setShowEdit1(!showEdit1)}><span>edit</span></div>
                    <div onClick={handleDelete}><span>delete</span></div>
                </div>
            </div>
            :
            <div className='header-button-container-ing'>
                <p>{ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}</p>
            </div>)
    )
}

export default Ingredient
