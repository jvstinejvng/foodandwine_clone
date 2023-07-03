import { Link } from 'react-router-dom';
import React from "react";
import './CSS/Footer.css'
import breadandbutter from '../images/bread-butter-footer.png'


function Footer() {

    return (
        <div className='footer-div'>
            <span className='footer-container-left'>
                <Link to='/'><img className='footer-logo' alt="bread and butter logo" src={breadandbutter} /></Link>
                <div className='footer-connect'>Connect with me</div>  
                <div className='footer-icons'>
                    <a className="footer-link" href="mailto:justinejang415@gmail.com"><i class="fa-solid fa-envelope"></i></a>
                    <a href="https://github.com/jvstinejvng" className="footer-link" target="_blank">
                        <i class="fa-brands fa-github"></i>
                    </a>
                    <a href="https://www.linkedin.com/in/jvstinejvng/" className="footer-link" target="_blank">
                        <i class="fa-brands fa-linkedin"></i>
                    </a>
                    <a href="https://github.com/jvstinejvng/foodandwine_clone" className="footer-link" target="_blank">
                        <i class="fa-solid fa-file-code"></i>
                    </a>
                </div>
            </span>
            {/* <span  className='footer-container-middle'>
                <Link to='/'>Recipes</Link>
            </span> */}
            <span className='footer-container-right'>
                <div  className='footer-copyright'>©Justine Jang 2023</div>
                <div  className='footer-text'>Inspired by <a className='foodandwinetext' href='https://www.foodandwine.com/'>Food & Wine</a></div>
                <div  className='footer-text'>This website is not intended for commercial use and is solely for demonstration purposes.</div>
            </span>
        </div>
    )
}

export default Footer
