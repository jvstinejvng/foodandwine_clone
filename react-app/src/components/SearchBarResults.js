import { useEffect, useState } from "react"
import { useDispatch, useSelector } from 'react-redux';
import { useParams } from 'react-router-dom'
import { getRecipesThunk } from '../store/recipe'
import RecipeCard from "./Recipes/RecipeCard";


function SearchBarResults() {

    const { term } = useParams()
    const searchTerm = term.slice(4)
    const dispatch = useDispatch()
    const recipes = useSelector(state => state.recipes)

    useEffect(() => {
        const fetchRecipes = async () => {
            await dispatch(getRecipesThunk())
        }
        fetchRecipes().catch(console.error)
    }, [dispatch])

    let searchResults
    if (recipes) {
        searchResults = Object.values(recipes).filter(recipe => {
            return recipe.title.toLowerCase().includes(searchTerm.toLowerCase())
        })
    }

    return (
        <>
            <h1>Results for '{searchTerm}'</h1>
            <div>
                <div>

                </div>
            </div>
            {searchResults.length > 0 ?
                    <div >
                        <div>
                            {searchResults.map(recipe => (
                                <RecipeCard key={recipe.id} recipe={recipe} />
                            ))}
                        </div>
                    </div>
            :
                <p>No recipes that match your search</p>
            }
        </>
    )
}

export default SearchBarResults;
