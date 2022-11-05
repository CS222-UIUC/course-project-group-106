import './App.css';
import React from 'react';
// import FileReader from './Components/FileReader';
// import Nav from './Components/Nav';
import './App.css';
import { useState } from 'react';
// import file from '../../data/transactions.csv';


function App() {

  const [currentPage, setCurrentPage] = useState('');

  function setPage(pageName) {
    setCurrentPage(pageName);
  }

  return (
    <div className='bg'>
      {/* <Nav setCurrentPage={setPage}/> */}
      
      <div className='nav'>
          <h1> Budget Tracker App </h1>
          <button class="navLi">Home</button>
          <button class="navLi">About</button>
          <button class="navLi">Projects</button>
      </div>
    </div>
  );
}

export default App;
