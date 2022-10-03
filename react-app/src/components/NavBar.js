import React from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { NavLink, Redirect } from 'react-router-dom';
import * as sessionaction from '../store/session';
import LogoutButton from './auth/LogoutButton';
import breadandbutter from '../images/breadandbutterlogo.svg'
import profileicon from '../images/profileicon.png'
import pencilicon from '../images/pencilicon.svg'
import forkandknife from '../images/forkandknife.png'
import logout from '../images/logout.svg'
import usericon from '../images/usericon.svg'

import './CSS/NavBar.css';

const NavBar = () => {

  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user);

  const demoLogin = async e => {
    e.preventDefault();
    await dispatch(sessionaction.login(
      'homechef@aa.io', 
      'password'));
    return <Redirect to='/' />
}

  return (
  <>
    <div className='NavBarMainDiv'>
        <div className='NavBarTopContainer'>
            <div className='NavBarLogo'>
                  <img alt="bread and butter logo" src={breadandbutter} />
            </div>
            <div className='NavBarLoginHome'>
            {!sessionUser &&
                <span className='NavBarLogIn'>
                      <img className='NavBarLogInImage' alt="Profile Icon" src={profileicon}/>
                      <NavLink className='LogInLink' to='/login' exact={true} activeClassName='active'>
                        Log In
                      </NavLink>
                      <img className='NavBarLogInImage' alt="Profile Icon" src={pencilicon}/>  
                      <NavLink className='LogInLink' to='/signup' exact={true} activeClassName='active'>
                        Sign Up 
                      </NavLink>
                      <img className='NavBarLogInImage' alt="Profile Icon" src={forkandknife}/>  
                      <button className='LogInLink' onClick={demoLogin}>
                        Demo User
                      </button>   
                </span>   
            }
            {sessionUser &&
                <span className='NavBarLogIn'>
                      <img className='NavBarLogInImage' alt="Profile Icon" src={usericon}/>
                      <NavLink className='LogInLink' to='/' exact={true} activeClassName='active'>
                       hello, {sessionUser.first_name}
                      </NavLink>
                      <img className='NavBarLogInImage' alt="Profile Icon" src={logout}/>  
                      < LogoutButton />
                </span>   
            }
            </div>
        </div>
        <div className='NavBarBottomContainer'>
            <div className='NavBarTags'>
                  <NavLink className='NavBarBottomLink' to='/' exact={true} activeClassName='active'>
                      HOME
                  </NavLink>
                  <NavLink className='NavBarBottomLink' to='/recipes' exact={true} activeClassName='active'>
                      RECIPES
                  </NavLink>
                  <NavLink className='NavBarBottomLink' to='/new-recipe' exact={true} activeClassName='active'>
                      ADD A RECIPE
                  </NavLink>
                  <NavLink className='NavBarBottomLink' to='/my-recipes' exact={true} activeClassName='active'>
                      MY RECIPE
                  </NavLink>
            </div>
        </div>
    </div>
  </>
  );
}

export default NavBar;
