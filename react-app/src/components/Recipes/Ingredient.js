import {  useState } from 'react'
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
            <>
                {ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}
                <span className='edit-ingredient-button-span'>
                    <span  className="edit-ingredient-button" onClick={() => setShowEdit1(!showEdit1)}>
                        <span className="edit-ingredient-edit">
                            <i class="fa-solid fa-pen-to-square"></i>
                            Edit
                        </span>
                    </span>
                    <span className="edit-ingredient-button" onClick={handleDelete}> 
                        <span className='edit-ingredient-delete'>
                            <i className="fa-solid fa-trash-can"></i>
                            Delete
                        </span>
                    </span>
                </span>
            </>
            :
            <>
                {ingredient.amount} {ingredient.measurement_unit.unit} {ingredient.food_stuff}
            </>
        )
    )
}

export default Ingredient
