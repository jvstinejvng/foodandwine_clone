import React, { useState, useEffect } from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import { useDispatch } from 'react-redux';
import UserAccount from './components/UserAccount';
import NavBar from './components/NavBar';
import ProtectedRoute from './components/auth/ProtectedRoute';
import UsersList from './components/UsersList';
import Homepage from './components/Homepage';
import User from './components/User';
import AllRecipes from './components/Recipe/AllRecipes';
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
        <Route path='/user-account' exact={true}>
          <UserAccount />
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
      </Switch>
    </BrowserRouter>
  );
}

export default App;
