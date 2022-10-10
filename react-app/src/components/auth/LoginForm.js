import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect, Link } from 'react-router-dom';
import { login } from '../../store/session';
import mailicon from '../../images/mailicon.svg'

import lockicon from '../../images/lockicon.svg'

import '../CSS/LogIn.css';

const LoginForm = () => {
  const [errors, setErrors] = useState([]);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onLogin = async (e) => {
    e.preventDefault();
    const data = await dispatch(login(email, password));
    if (data) {
      setErrors(data);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <div className='LoginMainContainer'>
      <div className='LoginDiv'>
          <div className='LoginHeaderDiv'>
            <h1 className='LoginHeaderText'>Log In</h1>
           </div>
      <div className='LoginFormDiv'>
        <form className='LoginForm' onSubmit={onLogin}>
          <div className="LoginError">
            {errors.map((error, ind) => (
              <li key={ind}>{error}</li>
            ))}
          </div>
          <div className='LoginInput'>
          <span className='LoginIconDiv'>
            <img className='LoginIcon' alt="Mail Icon" src={mailicon}/>
            </span>
            <input
              name='email'
              className="LoginInputField"
              required
              type='text'
              placeholder='yours@email.com'
              value={email}
              onChange={updateEmail}
            />
          </div>
          <div className='LoginInput'>
              <span className='LoginIconDiv'>
              <img className='LoginIcon' alt="Lock Icon" src={lockicon}/>
              </span>
                  <input
                    name='password'
                    type='password'
                    placeholder='your password'
                    className="LoginInputField"
                    required
                    value={password}
                    onChange={updatePassword}
                  />
                </div>
                <div className='LoginButtonDiv'>
                  <button className='LoginButton' type='submit'>LOG IN</button>
                </div>
                <div className='SignUpBottomDiv'>
                  <div className='SignUpLogInOption'>
                    <span className='SignUpLogInOptionText'>Not a member yet?</span>
                    <span className='SignUpLogInOptionText'>Create your account here!</span>
                    <div className="LogInLinkButton">
                      <Link style={{textDecoration: 'none'}} className='SignInLogLink' to="/log-in">Join Now</Link>
                    </div>
                  </div>
              </div>
        </form>
      </div>
      </div>
    </div>
  );
};

export default LoginForm;