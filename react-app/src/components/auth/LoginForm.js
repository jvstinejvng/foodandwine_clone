import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
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
      <div className='LoginHeader'>
        <h1>Log In</h1>
      </div>
      <div className='LoginFormDiv'>
        <form onSubmit={onLogin}>
          <ul>
            {errors.map((error, ind) => (
              <li key={ind}>{error}</li>
            ))}
          </ul>
          <img className='LoginIcon' alt="Mail Icon" src={mailicon}/>
          <div className='LoginInput'>
            <input
              name='email'
              type='text'
              placeholder='yours@email.com'
              value={email}
              onChange={updateEmail}
            />
          </div>
          <img className='LoginIcon' alt="Lock Icon" src={lockicon}/>
          <div className='LoginInput'>
            <input
              name='password'
              type='password'
              placeholder='your password'
              value={password}
              onChange={updatePassword}
            />
          </div>
          <button className='LoginButton' type='submit'>LOG IN</button>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;