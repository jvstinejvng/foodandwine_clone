import { useEffect, useState } from 'react'
import { useDispatch} from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import EditIngredient from './EditIngredient'

function Ingredient({ recipe, ingredient, showEditIngredient, measurementUnits }) {

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
        ( showEditIngredient && showEdit1 ?
        <EditIngredient
            ingredient={ingredient}
            measurementUnits={measurementUnits}
            recipe_id={recipe.id}
            showEdit1={showEdit1}
            setShowEdit1={setShowEdit1}
            />
        :
        showEditIngredient ?
            <div className=''>
                <div>{ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}</div>
                <div>
                    <div onClick={() => setShowEdit1(!showEdit1)}>
                        <div>edit</div>
                    </div>
                    <div onClick={handleDelete}>
                        <div>delete</div>
                    </div>
                </div>
            </div>
            :
            <div className=''>
                <div>{ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}</div>
            </div>
        )
    )
}

export default Ingredient
