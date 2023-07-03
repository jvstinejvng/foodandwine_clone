import { useState } from 'react'
import { useDispatch} from "react-redux"
import { getRecipesThunk } from '../../store/recipe'
import EditDirection from './EditDirection'
import '../CSS/EditDirection.css'

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
            <div className="direction-numbered-steps-div" key={instruction.id}> 
                Step&nbsp;{directionStep + 1}
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
                <>
                    <span className="direction-numbered-steps-div" key={instruction.id}> 
                        Step&nbsp;{directionStep + 1} 
                    </span>
                    <span className='edit-direction-button-span'>
                        <span className="edit-direction-steps" onClick={handleDelete}>
                            <span className="edit-direction-steps-trash">
                                <i class="fa-solid fa-trash-can"></i>
                                delete
                            </span>
                        </span>
                    </span>
                    <div>
                        <span key={instruction.id}>
                            { instruction.list_order } { instruction.specification }
                        </span>
                        <span className='edit-direction-button-span'>
                            <span className="edit-direction-steps" onClick={() => setShowEdit2(!showEdit2)}>
                                <span className="edit-direction-steps-edit">
                                    <i class="fa-solid fa-pen-to-square"></i>
                                    edit
                                </span>
                            </span>
                        </span>
                    </div>
                </>
                :
                <> 
                    <div className="direction-numbered-steps-div" key={instruction.id}> 
                        Step&nbsp;{directionStep + 1} 
                    </div>
                    {instruction.specification}
                </>
            )
        )
    )
}

export default Direction
