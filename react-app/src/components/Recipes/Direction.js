import { useState } from 'react'
import { useDispatch} from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import EditDirection from './EditDirection'

function Instruction({ instruction, recipe_id, showEditInstruction, currentLength }) {

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
        (showEditInstruction && showEdit2 ?
            <EditDirection
                instruction={instruction}
                showEdit2={showEdit2}
                setShowEdit2={setShowEdit2}
                recipe_id={recipe_id}
                />
        :
        showEditInstruction ?
            <div className='instruction-container'>
                <p key={instruction.id} className='instruction'>
                    {instruction.list_order}. {instruction.specification}
                </p>
                <div>
                    <div onClick={() => setShowEdit2(!showEdit2)}><span>edit</span></div>
                    {instruction.list_order === currentLength && <div onClick={handleDelete}><span>delete</span></div>}
                </div>
            </div>
            :
            <div className='header-button-container'>
                <p key={instruction.id}>{instruction.list_order}. {instruction.specification}</p>
            </div>
        )
    )
}

export default Instruction
