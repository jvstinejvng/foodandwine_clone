import { useState } from "react"
import LoginForm from "./auth/LoginForm"
import SignUpForm from "./auth/SignUpForm"
import './CSS/UserAccount.css'

export default function UserAccountForms() {
    
    const [LogIn, setLogIn] = useState(false)

    const handleLogIn = () => {
        setLogIn(true)
    }

    return (
        <>
            <div className="AccountUserMain">
                <div className="AccountUserContainer">
                        <div className="AccountUserMainFormDiv">
                                <div  className="AccountUserMainForm">
                                    {!LogIn && <SignUpForm />}
                                    {!LogIn &&
                                        <div className="AccountUserFormLogin">
                                            <div className="AccountUserSwitch">
                                                Already a member?
                                                <button className="AccountUserSwitchButton" onClick={handleLogIn}> Sign in</button>
                                            </div>
                                        </div>}
                                    {LogIn && <LoginForm setLogIn={setLogIn} />}
                                </div>
                            </div>
                        </div>    
        </div> 
        </>
    )
}
