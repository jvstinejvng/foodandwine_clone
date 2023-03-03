import { useState } from 'react'
import { useDispatch} from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import EditDirection from './EditDirection'

function Direction({ instruction, recipe_id, showEditDirection, directionStep }) {

    const dispatch = useDispatch()
    const [showEdit2, setShowEdit2] = useState()

    const handleDelete = async(e) => {
        e.preventDefault()

        try {
            const res = await fetch(`/api/recipes/instructions/${instruction.id}`, {
                method: 'DELETE'
            })
            if (res.ok) {
                const data = await res.json()
            }
            await dispatch(getRecipesThunk())
        } catch (e) {
            console.log('delete instruction failed! ' + e)
        }
    }

    return (
        ( showEditDirection && showEdit2 ?
            <> 
            <div className="direction-step-text-div" key={instruction.id}> 
                <span className="DirectionStepText">Step&nbsp;{directionStep + 1}</span>
                <i class="fa-solid fa-pen-to-square"></i>
            </div>
                <EditDirection
                instruction={instruction}
                showEdit2={showEdit2}
                setShowEdit2={setShowEdit2}
                recipe_id={recipe_id}
                />
            </>
            :
            (showEditDirection ?
                <div>
                    <span className="direction-step-text-div" key={instruction.id}> 
                        Step&nbsp;{directionStep + 1} 
                    </span>
                    <span className="DirectionStepEdit" onClick={handleDelete}>
                        <i class="fa-solid fa-trash-can"></i>
                        <span className="DirectionStepEditText">delete</span>
                    </span>
                    <div>
                    <span key={instruction.id} className='Direction'>
                    { instruction.list_order } { instruction.specification }
                    </span>
                    <span className="DirectionStepEdit" onClick={() => setShowEdit2(!showEdit2)}>
                        <i class="fa-solid fa-pen-to-square"></i>
                        <span className="DirectionStepEditText">edit</span>
                    </span>
                    </div>
                
                </div>
                :
                <div className='DirectionContainer'> 
                    <div className="direction-step-text-div" key={instruction.id}> Step&nbsp;{directionStep + 1} </div>
                    <div>{instruction.specification}</div>
                </div>
            )
        )
    )
}

export default Direction
