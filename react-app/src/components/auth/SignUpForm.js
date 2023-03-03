import React, {useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect, Link} from 'react-router-dom';
import { signUp } from '../../store/session';

import '../CSS/SignUp.css'

const SignUpForm = () => {

    const user = useSelector(state => state.session.user);
    const dispatch = useDispatch();

    const [errors, setErrors] = useState([]);
    const [username, setUsername] = useState('');
    const [first_name, setFirstName] = useState('');
    const [last_name, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [repeatPassword, setRepeatPassword] = useState('');

    const onSignUp = async (e) => {
      e.preventDefault();
      if (password === repeatPassword) {
        const data = await dispatch(signUp( username, first_name, last_name, email, password));
        if (data) {
          setErrors(data);
        }
      } else {
        setErrors(["Your password and confirmation password do not match."]);
      }
    };


    const updateUsername = (e) => {
      setUsername(e.target.value);
    };

    const updateFirstName = (e) => {
      setFirstName(e.target.value);
    };

    const updateLastName = (e) => {
      setLastName(e.target.value);
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
  
    return (
      <div className='SignUpFormDiv'>
        <div className="SignUpFormContainer">
          <div className='SignUpFormTitle'>
              <h1 className='SignUpFormTitleText'>Join Now</h1>
              <p className='SignUpFormTitleSubText'>Create an account to start building and customizing your own recipes.</p>
          </div>
                <form className="SignUpForm" onSubmit={onSignUp}>
                    {/* <div>
                      {errors.map((error, ind) => (
                      <div key={ind} className='SignUpFormError'>{error}</div>
                    ))}
                    </div> */}
                     <div>
       {errors.length > 0 && (
          <ul className='errors'>
            {errors.map(error => (
                <li className='error' key={error}>{error}</li>
            ))}
          </ul>
        )}
      </div>
    
            <div className='SignUpFormInput'>
                <label>Username</label>
                    <small className='SignUpFormSmall'>&nbsp;(required)</small>
                <input
                  className='InputSignUpField'
                  type='text'
                  name='username'
                  required
                  onChange={updateUsername}
                  value={username}
                  placeholder="Username"
                ></input>
            </div>
            <div className='SignUpFormInput'>
                <label>First Name</label>
                    <small className='SignUpFormSmall'>&nbsp;(required)</small>
                <input
                  className='InputSignUpField'
                  type='text'
                  name='first_name'
                  required
                  onChange={updateFirstName}
                  value={first_name}
                  placeholder="First Name"
                ></input>
            </div>
            <div className='SignUpFormInput'>
                <label>Last Name</label>
                    <small className='SignUpFormSmall'>&nbsp;(required)</small>
                <input
                  className='InputSignUpField'
                  type='text'
                  name='last_name'
                  required
                  onChange={updateLastName}
                  value={last_name}
                  placeholder="Last Name"
                ></input>
            </div>
            <div className='SignUpFormInput'>
                <label>Email</label>
                  <small className='SignUpFormSmall'>&nbsp;(required)</small>
                <input
                  className='InputSignUpField'
                  type='text'
                  name='email'
                  required
                  onChange={updateEmail}
                  value={email}
                  placeholder="Email"
                ></input>
            </div>
            <div className='SignUpFormInput'>
                  <label>Password</label>
                    <small  className='SignUpFormSmall'>&nbsp;(required)</small>
                  <input
                    className='InputSignUpField'
                    type='password'
                    name='password'
                    required
                    onChange={updatePassword}
                    value={password}
                    placeholder="Password"
                  ></input>
            </div>
            <div className='SignUpFormInput'>
                <label>Confirm Password</label>
                  <small className='SignUpFormSmall'>&nbsp;(required)</small>
                <input
                  className='InputSignUpField'
                  type='password'
                  name='repeat_password'
                  onChange={updateRepeatPassword}
                  value={repeatPassword}
                  required={true}
                  placeholder="Confirm Password"
                ></input>
            </div>
            <div className="SignUpFormButtonDiv">
              <button type="submit" className="SignUpFormButton">Join Now</button>
            </div>
            <div className='SignUpBottomDiv'>
                  <div className='SignUpLogInOption'>
                    <span className='SignUpLogInOptionText'>Already have a Bread & Butter account? Continue Here!</span>
                    <div className="LogInLinkButton">
                      <Link style={{textDecoration: 'none'}} className='SignInLogLink' to="/log-in">Log In</Link>
                    </div>
                  </div>
              </div>
          </form>
        </div>
      </div>
    );
  };

  
  export default SignUpForm;
  