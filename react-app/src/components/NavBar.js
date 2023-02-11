import { useSelector, useDispatch } from 'react-redux'
import { Link, NavLink,Redirect } from 'react-router-dom';
import * as sessionaction from '../store/session';
import { useState } from 'react'

import LogoutButton from './auth/LogoutButton';
import SearchBar from './SearchBar';

import breadandbutter from '../images//breadandbutterlogo.svg'

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

  const searchbutton = () => { setSearchBar(!searchBar) }

  return (
    <div className='NavBarMainDiv'>
      <div className='NavBarTopContainer'>
          <Link to='/' className='NavBarLogo'><img alt="bread and butter logo" src={breadandbutter} /></Link>
        <div className='NavBarTopRight'>
          <span className='NavBarUserBarSearch'> 
            {searchBar && sessionUser && ( <SearchBar setShowSearch={setSearchBar}/> )}  
            {searchBar && !sessionUser && ( <SearchBar setShowSearch={setSearchBar}/> )} 
              {searchBar ?
                <i 
                  class="fa-solid fa-mark"
                  alt='Search'
                  onClick={searchbutton}
                ></i>
                :
                <i class="fa-solid fa-magnifying-glass" onClick={searchbutton}
                title='search'></i>
              }
          </span>
          {!sessionUser && !searchBar &&
            <span className='NavBarUserBar'>
              <NavLink className='NavBarUserLogLinks' to='/log-in' exact={true} activeClassName='active'>
                <i class="fa-solid fa-circle-user"></i>
                Log In
              </NavLink>
              <NavLink className='NavBarUserLogLinks' to='/sign-up' exact={true} activeClassName='active'>
                <i class="fas fa-plus-circle"></i>
                Sign Up 
              </NavLink>
              <button className='NavBarUserDemo' onClick={demoLogin}>
                <i class="fas fa-adjust"></i>
                Demo User
              </button>  
            </span>
          }
          {sessionUser && !searchBar &&
            <span className='NavBarUserBar'>
              <NavLink className='NavBarBottomLink' to='/saved-recipes' exact={true} activeClassName='active'>
                <i class="fa-solid fa-bookmark"></i>
              </NavLink>
              <i class="fa-solid fa-circle-user">
              <span className='NavBarHelloUser'>hello, {sessionUser.first_name}</span>
              </i>
              <i class="fas fa-chevron-circle-right"><LogoutButton /></i>
            </span>
          }
        </div>
      </div>
        <div className='NavBarBottomContainer'>
          <div className='NavBarTags'>
            <NavLink className='NavBarBottomLink' to='/' exact={true} activeClassName='active'>HOME</NavLink>
            <NavLink className='NavBarBottomLink' to='/recipes' exact={true} activeClassName='active'>ALL RECIPES</NavLink>
          {sessionUser &&
            <>
              <NavLink className='NavBarBottomLink' to='/new-recipe' exact={true} activeClassName='active'>ADD A RECIPE</NavLink>
              <NavLink className='NavBarBottomLink' to='/my-recipes' exact={true} activeClassName='active'>MY RECIPES</NavLink>
            </>
          }
          </div>
        </div>
    </div>
  );
}

export default NavBar;
