import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Link, NavLink,Redirect } from 'react-router-dom';
import * as sessionaction from '../store/session';

import LogoutButton from './auth/LogoutButton';
// import SearchBar from '../Search/SearchBar';

import breadandbutter from '../images//breadandbutterlogo.svg'
import profileicon from '../images//profileicon.png'
import pencilicon from '../images/pencilicon.svg'
import forkandknife from '../images/forkandknife.png'
import logout from '../images/logout.svg'
import usericon from '../images/usericon.svg'

import './CSS/NavBar.css'

const NavBar = () => {

  const dispatch = useDispatch();
  const sessionUser = useSelector(state => state.session.user)

  const [searchBar, setSearchBar] = useState(false)

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
                  <Link to='/' class='NavBarLogo'>
                      <img alt="bread and butter logo" src={breadandbutter} />
                  </Link>
            <div className='NavBarLoginHome'>
              <div>
                {/* <div className='NavSearchBar'>
                  <img
                      src={pencilicon}
                      alt='MagnifyingGlassIcon'
                      className='MagnifyingGlassIcon'
                      onClick={() => setSearchBar(!searchBar)}
                      title='Search'/>
                    {searchBar && (
                      <SearchBar setShowSearch={setSearchBar}/>
                    )}       
                </div> */}
              </div>
              {!sessionUser &&
                    <span className='NavBarLogIn'>
                        <img className='NavBarLogInImage' alt="Profile Icon" src={profileicon}/>
                              <NavLink className='LogInLink' to='/log-in' exact={true} activeClassName='active'>
                                Log In
                              </NavLink>
                          <img className='NavBarLogInImage' alt="Profile Icon" src={pencilicon}/>  
                              <NavLink className='LogInLink' to='/sign-up' exact={true} activeClassName='active'>
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
                                hello, {sessionUser.username}
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
                  { sessionUser &&
                    <>
                        <NavLink className='NavBarBottomLink' to='/new-recipe' exact={true} activeClassName='active'>
                            ADD A RECIPE
                        </NavLink>
                        <NavLink className='NavBarBottomLink' to='/my-recipes' exact={true} activeClassName='active'>
                            MY RECIPE
                        </NavLink>
                    </>
                  }
            </div>
        </div>
    </div>
    </>
  );
}

export default NavBar;
