import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect , useHistory} from 'react-router-dom';
import { signUp } from '../../store/session';
import * as sessionActions from "../../store/session";


import '../CSS/SignUp.css'

const SignUpForm = () => {

  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();
  const history = useHistory();

  const onSignUp = async (e) => {

    e.preventDefault();
    setErrors([])
    if (password === repeatPassword) {
      const data = await dispatch(signUp(first_name, last_name, username, email, password));
      if (data) {
        setErrors(data)
      }
    } else {
      setErrors(['Passwords must match'])
    }
    
  };

  const updateFirstName = e => {
    setFirstName(e.target.value);
  };

  const updateLastName = e => {
    setLastName(e.target.value);
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  const handleDemoUser = async (e) => {
    e.preventDefault();
    const email1 = 'homechef@aa.io';
    const password1 = 'password';
    await dispatch(sessionActions.login(email1, password1));
    history.push('/')
  };


  return (
    <>
      <form className='signUpForm' onSubmit={onSignUp}>
        <div className='createAccount'>
          Create Account
        </div>
        <div className='signUpErrors'>
          {errors.map((error, ind) => (
            <li className="textError" key={ind}>{error}</li>
          ))}
        </div>
        <div>
        <div className='formText'>First Name</div>
          <label className='formFieldInput'>
            <input
              type='text'
              placeholder="Username"
              name='username'
              onChange={updateLastName}
              value={last_name}
            />
          </label>
          <div className='formText'>Last Name</div>
          <label className='formFieldInput'>
            <input
              type='text'
              placeholder="Username"
              name='username'
              onChange={updateFirstName}
              value={first_name}
            />
          </label>
        <div className='formText'>Username</div>
          <label className='formFieldInput'>
            <input
              type='text'
              placeholder="Username"
              name='username'
              onChange={updateUsername}
              value={username}
            />
          </label>
        </div>
        <div>
        <div className='formText' >Email</div>
          <label className='formFieldInput'>
            <input
              type='text'
              name='email'
              onChange={updateEmail}
              value={email}
            />
          </label>
        </div>
        <div className='passwordAlert'>
        <div className='formText'>Password</div>
          <label className='formFieldInput'>
            <input
              type='password'
              placeholder="At least 5 characters"
              name='password'
              onChange={updatePassword}
              value={password}
            />
          </label>
          <div className="alertDiv">
          <div className="alertIcon">
          </div>
          </div>
        </div>
        <div>
        <div className='formText'>Re-Password</div>
          <label className='formFieldInput'>
            <input
              type='password'
              name='repeat_password'
              onChange={updateRepeatPassword}
              value={repeatPassword}
            />
          </label>
        </div>
        <button className='splashSubmitButton' type='submit'>Create account</button>
        <button className='splashSubmitButton' onClick={handleDemoUser}>Log in with Demo User</button>
      </form>
    </>
  );
  }

export default SignUpForm;
