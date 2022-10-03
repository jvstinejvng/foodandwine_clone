import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import { Redirect } from 'react-router-dom';
import { login } from '../../store/session';
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
          <div>
            <input
              name='email'
              type='text'
              placeholder='yours@email.com'
              value={email}
              onChange={updateEmail}
            />
          </div>
          <div>
            <input
              name='password'
              type='password'
              placeholder='your password'
              value={password}
              onChange={updatePassword}
            />
            <button className='LoginButton' type='submit'>Login</button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default LoginForm;
