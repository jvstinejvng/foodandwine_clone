import { useEffect, useState } from 'react'
import { useDispatch} from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import EditIngredient from './EditIngredient'
import '../CSS/EditIngredient.css'

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
            <div>
                <span>{ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}</span>
                <div className='IngredientEditButton'>
                    <span  className="IngredientStepText" onClick={() => setShowEdit1(!showEdit1)}>
                        <i class="fa-solid fa-pen-to-square"></i>
                        <span className="IngredientStepEditText">edit</span>
                    </span>
                    <span className="IngredientStepText" onClick={handleDelete}>
                        <i class="fa-solid fa-trash-can"></i>
                        <span className="IngredientStepEditText">delete</span>
                    </span>
                </div>
            </div>
            :
            <div>
                <div>{ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}</div>
            </div>
        )
    )
}

export default Ingredient
