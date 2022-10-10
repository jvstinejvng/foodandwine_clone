import { NavLink } from "react-router-dom"

import "./CSS/RecipePage.css"
import breadcumbs from '../images/breadcrumb.png'


const NotFound = () => {
    return (
        <>
             <div className="Recipe404Page">
                    <div className='Recipe404Text'>This recipe was sent back to the kitchen!</div>
                        <div className='RecipePageImg'>
                            <img className="ReceipePage404img" alt="Bird picking on bread crumbs" src={breadcumbs}/>
                        </div>
                    <div className='RecipePage404SubText'>The page you're looking for is unavailable.</div>
                            {/* <div>You might find what you're looking for by using our search option</div> */}
                    <div className="BackHomeButtonDiv">
                                <NavLink to='/'><button className="BackHomeButton">Back to Home</button> </NavLink>
                    </div>
            </div>
          
        </>
    )
}

export default NotFound;
