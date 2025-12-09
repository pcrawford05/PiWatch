import { useState, useEffect } from 'react'
import './App.css'

import {LogEntry} from "./LogEntry.jsx"

import "bootstrap/dist/css/bootstrap.min.css";

function App() {

  const [logImgs, setLogImgs] = useState([]);
  const [showLogImg, setShowLogImg] = useState("");

  let logEntryKey = 1;

  async function pollingFunc(){
    const logResponse = await fetch("http://127.0.0.1:5000/log_img");
    const logResults = await logResponse.json();
    console.log(logResults);
    setLogImgs(logResults.log);
  }

  useEffect( () => {
    pollingFunc();

    function startPolling () {
      setInterval( () => {
        pollingFunc();
      }, 1000);
    }

    startPolling();
  },
  []);

  function handleEntryClick(url) {
    setShowLogImg(url);
  }

  return (
    <>
      <div id="header">
        <h1>PiWatch</h1>
      </div>
      <div className="container">
        <div className="row">
          <div id="curr-img" className="col-8">            
            <h2>Selected Log Image</h2>
            <img src={showLogImg} alt={showLogImg || "Select an image from log"} style={{ maxWidth: '100%' }} />
          </div>
          <div id="log" className="col-4">
            <h2>Log</h2>

            {logImgs.map( (entry) => {
              logEntryKey ++;
              return (<LogEntry url={entry} parentHandleClick={handleEntryClick} key={logEntryKey} />);
            } ) }

          </div>
        </div>
      </div>
    </>
  )
}

export default App
