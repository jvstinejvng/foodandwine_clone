import { useState, useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { NavLink , useHistory} from 'react-router-dom';
import { getAllRecipesThunk } from '../../store/recipes'


function MyRecipes() {
    const dispatch = useDispatch();
    const history = useHistory();
    const sessionUser = useSelector(state => state.session.user);
    const [isLoaded, setIsLoaded] = useState(false);


    const filterResponse = (recipes) => {
        return sessionUser
          ? recipes
              .filter((recipe) => recipe.user_id === sessionUser["id"])
              .sort((a, b) => b.id - a.id)
          : history.push("/");
      };

      const allRecipes = useSelector((state) => Object.values(state?.recipes));
      const filteredRecipes = filterResponse(allRecipes);

      useEffect(() => {
        dispatch(getAllRecipesThunk()).then(() => setIsLoaded(true));
      }, [dispatch]);
    


    return (
    <>
    <div>
    <div className='AllRecipeCardContainer'>
    <div>
            {isLoaded &&
              sessionUser &&
              filteredRecipes?.length > 0 &&
              filteredRecipes?.map((userRecipes, index) => (
                <div  key={index}>
                  <NavLink to={`/recipes/${userRecipes.id}`}>
                    <img
                      src={userRecipes.img_url}
                      alt="bookcover"
                    />
                  </NavLink>
                  <div>
                  </div>
                </div>
              ))}
            </div>
    </div>
    </div>
    </>
    )
}

export default MyRecipes
