import React, { Component } from 'react';
// if have time, create a logo
import logo from './logo.svg';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
       <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title"> Title goes here </h1>
        </header>
        <p className="App-intro">
          description goes here
        </p>
      </div>
    );
  }
}

export default App;
