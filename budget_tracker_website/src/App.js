import './App.css';
import React from 'react';
import './App.css';
import { useState } from 'react';
import { BrowserRouter as Router, Route, Switch} from 'react-router-dom';
import { useHistory } from 'react-router-dom';

import {Home} from './Components/Home';
import {About} from './Components/About';
import {Project} from './Components/Project';


function App() {

  // use useHistory
  // const history = useHistory();

  return (
    <Router>
      <div className='bg'>
          <div className='nav'>
              <h1> Budget Tracker App </h1>

              <a class="navLi" href="/home">Home</a>
              <a class="navLi" href="/about">About</a>
              <a class="navLi" href="/">Projects</a>
          
              {/* <button class="navLi">Home</button>
              <button class="navLi">About</button>
              <button class="navLi">Projects</button> */}
          </div>
          <div className='content'>
            <Switch>
              <Route path="/home">
                <Home />
              </Route>
              <Route path="/about">
                <About />
              </Route>
              <Route path="/project">
                <Project />
              </Route>
            </Switch>
          </div>
        </div>
    </Router>
  );
}

export default App;
