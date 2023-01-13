import { useSelector, useDispatch } from 'react-redux'
import { Link, NavLink,Redirect } from 'react-router-dom';
import * as sessionaction from '../store/session';
import { useState } from 'react'

import LogoutButton from './auth/LogoutButton';
import SearchBar from './SearchBar';

import breadandbutter from '../images//breadandbutterlogo.svg'
import profileicon from '../images//profileicon.png'
import pencilicon from '../images/pencilicon.svg'
import forkandknife from '../images/forkandknife.png'
import logout from '../images/logout.svg'
import usericon from '../images/usericon.svg'
import MagnifyingGlassIcon from '../images/search.png'

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


  const searchbutton = () => {
    setSearchBar(!searchBar)
  }


  return (
      <div className='NavBarMainDiv'>
          <div className='NavBarTopContainer'>
                  <Link to='/' className='NavBarLogo'>
                      <img alt="bread and butter logo" src={breadandbutter} />
                  </Link>
            <div className='NavBarTopRight'>
                  <span className='NavBarUserBarSearch'>
                  <img
                      src={MagnifyingGlassIcon}
                      alt='Search'
                      id='MagnifyingGlassIcon'
                      onClick={searchbutton}
                      title='search'/>
                      <p id="help"></p>
                    {searchBar && sessionUser && (
                      <SearchBar setShowSearch={setSearchBar}/>
                      
                    )}  
                     {searchBar && !sessionUser && (
                      <SearchBar setShowSearch={setSearchBar}/>
                    )}    
                  </span>
              {!sessionUser && !searchBar &&
                    <span className='NavBarUserBar'>
                        <img className='NavBarUserBarImage' alt="Profile Icon" src={profileicon}/>
                              <NavLink className='NavBarUserLogLinks' to='/log-in' exact={true} activeClassName='active'>
                                Log In
                              </NavLink>
                          <img className='NavBarUserBarImage' alt="Profile Icon" src={pencilicon}/>  
                              <NavLink className='NavBarUserLogLinks' to='/sign-up' exact={true} activeClassName='active'>
                              Sign Up 
                            </NavLink>
                          <img className='NavBarUserBarImage' alt="Profile Icon" src={forkandknife}/>  
                        <button className='NavBarUserDemo' onClick={demoLogin}>
                            Demo User
                        </button>  
                      </span>   
                      
              }
              {sessionUser && !searchBar &&
                    <span className='NavBarUserBar'>
                        <img className='NavBarUserBarImage' alt="Profile Icon" src={usericon}/>
                            <div className='NavBarHelloUser'>
                                hello, {sessionUser.username}
                            </div>
                        <img className='NavBarUserBarImage' alt="Profile Icon" src={logout}/>  
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
  
  );
}

export default NavBar;
