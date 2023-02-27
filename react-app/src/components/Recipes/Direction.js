import { useState } from 'react'
import { useDispatch} from "react-redux"

import { getRecipesThunk } from '../../store/recipe'
import EditDirection from './EditDirection'

function Instruction({ instruction, recipe_id, showEditDirection, currentLength }) {

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
            <EditDirection
                instruction={instruction}
                showEdit2={showEdit2}
                setShowEdit2={setShowEdit2}
                recipe_id={recipe_id}
                />
        :
        showEditDirection ?
            <div className=''>
                <div key={instruction.id} className=''>
                    {instruction.list_order}. {instruction.specification}
                </div>
                <div>
                    <div onClick={() => setShowEdit2(!showEdit2)}><div>edit</div></div>
                    {instruction.list_order === currentLength && <div onClick={handleDelete}><div>delete</div></div>}
                </div>
            </div>
            :
            <div className=''>
                <div key={instruction.id}>{instruction.list_order}. {instruction.specification}</div>
            </div>
        )
    )
}

export default Instruction
