import React, { useState } from "react";
import './App.css';
import Card from "./components/card/Card"

var Twitter = require('twitter');

const cliente = new Twitter({
    consume_key:"ulIyy3tdHD2ICYAQuLfmaPFY3",
    consumer_secret:"pF63JdlSd8mYIsWLP4KVnoZG8DIRRP9HsEv2nfMZ1FVHKQZVdJ",
    access_token: "1419713857514311681-pIrCxJOHrWk2mOXtYTjL4zzuRSnxbS",
    access_token_secret: "y3gueu71x60uIvnHOxZc6okYWpBmijoiTHFOwUgBUPjx9"
})

cliente.post("statuses/update", {status: "pruebaa"})
    .then((tweet) => {
        console.log(tweet);
    })
    .catch((err) => {
        console.log(err);
    })

function App() {
  const [theme, setTheme] = useState();

  var title = "Elige el tema para el tweet"
  var note = "(Dejalo vacio para que Galia genere su propio tema)"
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
