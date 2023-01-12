import { useEffect, useState } from "react"
import { useDispatch, useSelector } from 'react-redux';
import { Link, useHistory } from 'react-router-dom'
import { getRecipesThunk } from '../store/recipe'

import './CSS/SearchBar.css'

function SearchBar({ setShowSearch }) {
    const dispatch = useDispatch()
    const history = useHistory()
    const [searchTerm, setSearchTerm] = useState('')
    const [filteredResults, setFilteredResults] = useState([])

    const recipes = useSelector(state => state.recipes)

    useEffect(() => {
        const fetchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        fetchRecipes().catch(console.error)
    }, [dispatch])

    const handleFilter = (e) => {
        const searchWord = e.target.value
        setSearchTerm(searchWord)
        const newFilter = Object.values(recipes).filter(recipe => {
            return recipe.title.toLowerCase().includes(searchWord.toLowerCase())
        })

        if (searchWord === '') {
            setFilteredResults([])
        } else {
            setFilteredResults(newFilter)
        }
    }

    const clearInput = () => {
        setFilteredResults([])
        setSearchTerm('')
    }

    const handleSubmit = () => {
        history.push(`/recipes/search/title=${searchTerm}`)
        setFilteredResults([])
        setSearchTerm('')
        setShowSearch(false)
    }


    return (
        <div>
            <form onSubmit={handleSubmit}>
                <input
                    type='text'
                    value={searchTerm}
                    onChange={handleFilter}
                    placeholder='Search recipes'/>
                <div >
                    <div
                        onClick={searchTerm.length ? clearInput : () => setShowSearch(false)}
                        title={searchTerm.length ? 'Clear Search' : 'Close Search'}></div>
                </div>
            </form>
            {filteredResults.length > 0 && (
                <div >
                    {filteredResults && (
                        filteredResults.slice(0, 4).map((result, idx) => (
                            <Link
                                to={`/recipes/${result.id}`}>
                                <div
                                    key={idx}
                                    className='search-result'
                                    onClick={() => setShowSearch(false)}>
                                    {result.title}
                                </div>
                            </Link>
                        ))
                    )}
                </div>
            )}
        </div>
    )
}

export default SearchBar
