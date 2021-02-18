import React from 'react';
import {Link} from 'react-router-dom';
import './../../styles/header.css';

class Header extends React.Component {
    render() {
        return(
            <>
            <nav className="nav nav-tabs">
                <li className="nav-item">
                    <Link className="nav-link active" aria-current="page" to="/">Map</Link>
                </li>
                <li className="nav-item">
                    <Link className="nav-link" to="/ABCLocation">ABC</Link></li>
                <li className="nav-item">
                    <Link className="nav-link" to="/Popular">인기순</Link></li>
                <li className="nav-item">
                    <Link className="nav-link" to="/SafeLocation">밀집도순</Link></li>
                
            </nav>
            </>
        )
    }
}

export default Header;