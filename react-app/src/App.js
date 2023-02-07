import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';

import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
// import UsersList from './components/UsersList.js';
// import User from './components/User.js';

import NavBar from './components/NavBar.js';
import Homepage from './components/Homepage.js';
import AllRecipes from './components/Recipes/AllRecipes';
import RecipePage from './components/Recipes/RecipePage';
import CreateRecipe from './components/Recipes/CreateRecipe';
import UserRecipes from './components/Recipes/UserRecipes';
import SavedRecipes from './components/Recipes/SavedRecipesPage';

import ProtectedRoute from './components/auth/ProtectedRoute';
import { authenticate } from './store/session';

import { getRecipesThunk } from './store/recipe';
import SearchBarResults from './components/SearchBarResults';
import NotFound from './components/NotFound.js';
import Footer from './components/Footer.js';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
    const searchRecipes = async () => {
      await dispatch(getRecipesThunk())
    }
    searchRecipes().catch(console.error)
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
      <NavBar />
          <Switch>
            <Route path='/log-in' exact={true}>
              <LoginForm />
            </Route>
            <Route path='/sign-up' exact={true}>
              <SignUpForm />
            </Route>
            {/* <ProtectedRoute path='/users' exact={true} >
              <UsersList/>
            </ProtectedRoute> */}
            {/* <ProtectedRoute path='/users/:userId' exact={true} >
              <User />
            </ProtectedRoute> */}
            <Route path='/' exact={true} >
              <Homepage />
            </Route>
            <Route path='/recipes' exact={true}>
              <AllRecipes />
            </Route>
            {/* <Route path='/recipes/search/:term' exact={true}>
              <SearchBarResults />
            </Route> */}
            <ProtectedRoute path='/new-recipe' exact={true} >
              <CreateRecipe />
            </ProtectedRoute>
            <ProtectedRoute path='/my-recipes' exact={true} >
              <UserRecipes />
            </ProtectedRoute>
            <ProtectedRoute path='/saved-recipes' exact={true} >
              <SavedRecipes />
            </ProtectedRoute>
            <Route path='/recipes/:id'>
              <RecipePage/>
            </Route>
            <Route>
              <NotFound/>
            </Route>
          </Switch>
          <Footer />
    </BrowserRouter>
  );
}

export default App;
