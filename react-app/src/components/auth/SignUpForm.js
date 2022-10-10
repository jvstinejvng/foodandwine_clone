import React, {useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect , useHistory, Link} from 'react-router-dom';
import { signUp } from '../../store/session';
import * as sessionActions from "../../store/session";


import '../CSS/SignUp.css'

const SignUpForm = () => {

    const user = useSelector(state => state.session.user);
    const dispatch = useDispatch();

    const [errors, setErrors] = useState([]);
    // const [firstName, setFirstName] = useState("");
    const [username, setUsername] = useState('');
    // const [lastName, setLastName] = useState("");
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [repeatPassword, setRepeatPassword] = useState('');

    const onSignUp = async (e) => {
      e.preventDefault();
      if (password === repeatPassword) {
        const data = await dispatch(signUp( username.trim(),  email.trim(), password));
        if (data) {
          setErrors(data);
        }
      } else {
        setErrors(["Your password and confirmation password do not match."]);
      }
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
                    <div>
                      {errors.map((error, ind) => (
                      <div key={ind} className='SignUpFormError'>{error}</div>
                    ))}
                    </div>
    
            <div className='SignUpFormInput'>
                <label>Username</label>
                    <small className='SignUpFormSmall'>&nbsp;(required)</small>
                <input
                  className='InputSignUpField'
                  type='text'
                  name='username'
                  required
                  onChange={(e) => setUsername(e.target.value)}
                  value={username}
                  placeholder="Username"
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
                  onChange={(e) => setEmail(e.target.value)}
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
                    onChange={(e) => setPassword(e.target.value)}
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
                  onChange={(e) => setRepeatPassword(e.target.value)}
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
  