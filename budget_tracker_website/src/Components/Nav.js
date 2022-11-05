import React from 'react';
import useState from 'react';

function Nav(setPage) {

    return (
        <div>
            <p> hello </p>
            <div class="logo">NavBar</div>
                <button class="navLi" onClick={setPage('Home')}>Home</button>
                <button class="navLi">About</button>
                <button class="navLi">Projects</button>
                <button class="navLi">Contact Us</button>

                <div class="navBtn ">
                <div class="line1"></div>
                <div class="line2"></div>
                <div class="line3"></div>
            </div>
        </div>
    )
}

export default Nav;