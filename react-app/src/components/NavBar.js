import React from 'react';
import { NavLink } from 'react-router-dom';
import LogoutButton from './auth/LogoutButton';
import breadandbutter from '../images/breadandbutterlogo.svg'
import profileicon from '../images/profileicon.png'

import './CSS/NavBar.css';

const NavBar = () => {

  // const sessionUser = useSelector(state => state.session.user)

  // const [ showDropdown, setShowDropdown ] = useState(false)

  // const handleDropdown = () => {
  //   if (showDropdown) return
  //   setShowDropdown(true)
  // }

  return (
  <>
    <div className='NavBarMainDiv'>
        <div className='NavBarTopContainer'>
            <div className='NavBarLogo'>
                  <img alt="bread and butter logo" src={breadandbutter} />
            </div>
            <div className='NavBarLoginHome'>
                <span className='NavBarLogIn'>
                    <img className='NavBarLogInImage' alt="Profile Icon" src={profileicon}/>
                      <NavLink className='LogInLink' to='/login' exact={true} activeClassName='active'>
                        Log In
                      </NavLink>  
                </span>   
                <span className='NavBarHome'>
                      <NavLink className='LogInLink' to='/' exact={true} activeClassName='active'>
                        Home 
                      </NavLink>  
                </span>
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
