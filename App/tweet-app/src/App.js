import React, { useState } from "react";
import './App.css';
import Card from "./components/card/Card"

function App() {
  const [theme, setTheme] = useState();

  var title = "Elegir tema"
  var note = "(Dejar vacio para Galia genere su propio tema)"
  var posibleInput = [{html: <input onChange={ event =>setTheme(event.target.value)}></input>}, {html: <div></div>}]
  var buttons = {button: <button>Generar Tweet</button>, button1: <button>Twittear</button>, button2: <button>Generar de nuevo</button>}

  return (
    <div className="App">
      <header>
        <h1>Galia Tweet's</h1>
      </header>

      <div className="Body">
        <div className="pasos">
          <div className="paso1">
            <Card title={title} note={note} isinput={posibleInput[0].html} button={buttons.button}/>
          </div>
        </div>

        <div className="tweetgen">
          <Card title={"Tweet generado"} theme={theme} tweet={"Tweet:"} isinput={posibleInput[1].html} button1={buttons.button1} button2={buttons.button2}/>
        </div>
      </div>
    </div>
  );
}

export default App;
