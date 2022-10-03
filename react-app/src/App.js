import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import LoginForm from './components/auth/LoginForm';
import SignUpForm from './components/auth/SignUpForm';
import UsersList from './components/UsersList';
import Homepage from './components/Homepage';
import User from './components/User';
import AllRecipes from './components/Recipe/AllRecipes';
import RecipeForm from './components/Recipe/RecipeForm';
import SingleRecipe from './components/Recipe/SingleRecipe';
import { authenticate } from './store/session';

function App() {
  const [loaded, setLoaded] = useState(false);
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticate());
      setLoaded(true);
    })();
  }, [dispatch]);

  if (!loaded) {
    return null;
  }

  return (
    <BrowserRouter>
        <NavBar />
      <Switch>
        <Route path='/' exact={true} >
          <Homepage />
        </Route>
        <Route path='/log-in' exact={true}>
          <LoginForm />
        </Route>
        <Route path='/sign-up' exact={true}>
          <SignUpForm />
        </Route>
        <ProtectedRoute path='/users' exact={true} >
          <UsersList/>
        </ProtectedRoute>
        <ProtectedRoute path='/users/:userId' exact={true} >
          <User />
        </ProtectedRoute>
        <Route path='/recipes' exact={true} >
          <AllRecipes/>
        </Route>
        <Route path='/recipes/:id' exact={true}>
          <SingleRecipe />
        </Route>
        <Route path='/new-recipe' exact={true}>
          <RecipeForm />
        </Route>

      </Switch>
    </BrowserRouter>
  );
}

export default App;
