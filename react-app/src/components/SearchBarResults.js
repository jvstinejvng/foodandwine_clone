import { useEffect, useState } from "react"
import { useDispatch, useSelector } from 'react-redux';
import { Link, useParams, useHistory } from 'react-router-dom'
import { getRecipesThunk } from '../store/recipe'
import RecipeCard from "./Recipes/RecipeCard";

import './CSS/SearchBar.css'

function SearchResults( {setSearchBar} ) {

    const { term } = useParams()
    const history = useHistory()
    const dispatch = useDispatch()

    const recipes = useSelector(state => state.recipes)
    const AllRecipeSearch = Object.values(useSelector(state => state.recipes))
    const randomRecipe = Math.floor(Math.random() * AllRecipeSearch.length)

    const [searchTerm, setSearchTerm] = useState(term.slice(6))
    const updateSearchTerm = (e) => setSearchTerm(e.target.value)
   
    useEffect(() => {
        const searchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        searchRecipes().catch(console.error)
    }, [dispatch])

    let searchResults
    if (recipes) {
        searchResults = Object.values(recipes).filter(recipe => {
            return recipe.title.toLowerCase().includes(searchTerm.toLowerCase())
        })
    } 

    const handleSubmit = async(e) => {
        history.push(`/recipes/search/title=${searchTerm}`)
        setSearchTerm('')
        setSearchBar(false)
        e.preventDefault()
    }

    const clearInput = () => {
        setSearchTerm('')
    }

    return (
        <>
        <div>
            <div className='SearchPageResultHeaderDiv'>
            <div className='SearchPageResultHeader'>
                <h3 className='SearchPageResulth3'>Search Results For</h3>
                    <form className='SearchPageResultText'  onSubmit={handleSubmit}>
                        <i id='SPMagnifyingGlass' class="fa-solid fa-magnifying-glass"></i>
                            <input className='SearchPageResultInput'
                            type='text'
                            value={searchTerm}
                            onChange={updateSearchTerm}
                            placeholder='Search'/>
                    </form>
                    { searchTerm ? 
                        <i id='SPXMark' 
                            className="fa-solid fa-xmark" 
                            onClick={searchTerm.length ? clearInput : () => setSearchBar(false)}>
                            <p id='ClearSearch'>clear search</p>
                        </i>
                        :
                        <div></div>
                    }
            </div>
            </div>
            <div className='SearchBarResultContainer'> 
                { searchTerm.length > 0 &&
                    <div className='SearchBarPageResult'>
                        { searchResults.map(recipe => (
                            <RecipeCard key={recipe.id} recipe={recipe} />
                        ))}
                    </div>
                }

                {!searchTerm &&  
                    <div className="SearchResultPageBlank">
                        <h2 className="SearchAllRecipeh2">Search All Recipes</h2>
                        <div className="RandomRecipeGenerator">Don't know what to cook? 
                            <Link to={AllRecipeSearch.length > 0 && `/recipes/${AllRecipeSearch[randomRecipe].id}`}>
                            <button>Find Me A Recipe</button>
                            </Link>
                        </div>
                    </div> 
                }   

                {!searchResults.length && 
                    <div className="SearchResultText" >
                        Uh oh. We didn't find the search term "{searchTerm}" that you were looking for.
                        <p className="SearchResultSub" >Please try another search term</p>
                    </div>
                }

                {/* {searchResults.length > 0 ?
                    <div>
                        {searchResults.map(recipe => (
                        <RecipeCard key={recipe.id} recipe={recipe} />
                        ))}
                    </div>
                    :
                    <div>0 results found for your search.
                        <p>Please try another search term</p>
                    </div>
            } */}   
            </div>    
        </div>
        </>
    )
}

export default SearchResults;
