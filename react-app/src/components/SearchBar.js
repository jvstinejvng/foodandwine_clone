import { useEffect, useState } from "react"
import { useDispatch, useSelector } from 'react-redux';
import { Link, useHistory } from 'react-router-dom'
import { getRecipesThunk } from '../store/recipe'

import './CSS/SearchBar.css'

function SearchBar( {setShowSearch} ) {

    const dispatch = useDispatch()
    const history = useHistory()
    const [searchTerm, setSearchTerm] = useState('')
    const [filteredResults, setFilteredResults] = useState([])

    const recipes = useSelector(state => state.recipes)

    useEffect(() => {
        const searchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        searchRecipes().catch(console.error)
    }, [dispatch])

    const handleFilter = (e) => {
        const searchWord = e.target.value
        setSearchTerm(searchWord)
        const newFilter = Object.values(recipes).filter(recipe => {
            return recipe.title.match(/\b\w/g).join('').toLowerCase().includes(searchWord.toLowerCase())
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

    const handleSubmit = async(e) => {
        history.push(`/recipes/search/title=${searchTerm}`)
        setFilteredResults([])
        setSearchTerm('')
        setShowSearch(false)
    }

    return (
        <div className='SearchBarDiv'>
            <form className='SearchBarResult' onSubmit={handleSubmit} >
                <div className='SearchText'>Search</div>
                <input
                    className='SearchBarInput'
                    type='text'
                    value={searchTerm}
                    onChange={handleFilter}
                    placeholder='Search recipes'/>
                <div >  
                    <i className="fa-solid fa-xmark clear-search"
                        onClick={searchTerm.length ? clearInput : () => setShowSearch(false)}
                        title={searchTerm.length ? 'Clear Search' : 'Close Search'}></i>
                </div>
            </form>
            {filteredResults.length > 0 && (
                <div className="SearchBarResultDiv">
                    {filteredResults && (
                        filteredResults.slice(0, 5).map((result, idx) => (
                            <Link
                                to={`/recipes/${result.id}`}>
                                <div
                                    key={idx}
                                    className='SearchBarResultDisplay'
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
