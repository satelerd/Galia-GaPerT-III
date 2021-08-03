import React, { useEffect, useState } from "react";
import './App.css';
import Card from "./components/card/Card"
import OpenAI from 'openai-api';

// agruega 1 al contador de visitas
var xhr = new XMLHttpRequest();
xhr.open("GET", "https://api.countapi.xyz/hit/satelerd.github.ioGalia-GaPerT-III/visitas");
console.log("visitas", xhr)
xhr.responseType = "json";
xhr.send();


function App() {
  const [theme, setTheme] = useState("");
  const [galiaResponse, setGaliaResponse] = useState()
  const [gptResponse, setGptResponse] = useState("")

  async function ApiCall() {
    const  userHandler = process.env.REACT_APP_USER_HANDLER
    const openai = new OpenAI(userHandler);
    const preset = "Galia es una filosofa reconocida a nivel mundial que busca la creatividad, la libre expresión y la buena música. Galia es bastante sarcástica, por lo que a veces responde de mala gana.\nEste modelo generara un Tweet de Galia según un tema a elección.\n\nTema: El ocio. \nTweet: Siento que a veces hago mucho por la gente y la humanidad. ¿Por qué no puedo estar un rato sin hacer nada?\n###\nTema: La música.\nTweet: La música crea mas simpatía que el sexo.\n###\nTema: Paises sub desarrollados.\nTweet: Los paises subdesarrollados deberian ser mas estrictos con la migracion.\n###\nTema: Los carros.\nTweet: Me gusta mucho andar en bicicleta, pero estoy en contra de querer cambiar el mundo por ese termino.\n###\nTema: Pornografia.\nTweet: Me gusta mucho mirar porno, pero siempre tengo que tener cuidado con la hora, para no dar una \"sorpresa\" a mi madre.\n###\nTema: La gente.\nTweet: La gente es una raza aislada, que se siente superior y que no tiene en cuenta el mundo que la rodea.\n###\nTema:"
    const final = ".\nTweet:"
    var fullPromp = ""

    if(theme === "") {
      fullPromp = preset
    } else {
      fullPromp = preset + theme + final
    }

    setGaliaResponse("CALMA")
    setGptResponse (
      await openai.complete({
        engine: 'davinci',
        prompt: fullPromp,
        maxTokens: 64,
        temperature: 0.5,
        topP: 1,
        presencePenalty: 0,
        frequencyPenalty: 0,
        bestOf: 1,
        n: 1,
        stream: false,
        stop: ["###", "testing"]
      })
    )
    // agruega 1 al contador de generaciones
    var xhr = new XMLHttpRequest();
    xhr.open("GET", "https://api.countapi.xyz/hit/satelerd.github.ioGalia-GaPerT-III/generaciones");
    console.log("generaciones", xhr)
    xhr.responseType = "json";
    xhr.send();
    
  } 

  useEffect(() => {
    if(gptResponse === "" || gptResponse.data === undefined) {
      setGaliaResponse("")
    } else{
      // Limpieza de texto
      var cont = 0
      var txt = gptResponse.data.choices[0].text
      for(let i=0; i<txt.length; i++) {
        if (txt[i] === ":") {
          break
        }
        cont++
      }
      if (theme === "") {
        setTheme("Tema: " + txt.slice(0, cont-6))
        console.log(txt)
        txt = txt.slice(cont+2,txt.length-1)
        console.log(txt)
      } else {
        txt = txt.slice(1,txt.length)
      }
      
      setGaliaResponse(txt)
      
    }
    console.log();
  }, [gptResponse])


  var title = "Elige el tema para el tweet"
  var note = "(Dejalo vacio para que Galia genere su propio tema)"
  var posibleInput = [{html: <input placeholder="Ej: La humanidad" onChange={ event => setTheme("Tema: " + event.target.value) }></input>}, {html: <div></div>}]
  var buttons = {button: <button className="bold" onClick={() => {ApiCall()}}>Generar Tweet</button>, button1: <button className="bold">Twittear</button>, button2: <button className="bold">Generar de nuevo</button>}



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
          {/* <ApiCall></ApiCall> */}
          <Card title={"Tweet generado"} theme={theme} tweet={"Tweet:"} isinput={posibleInput[1].html} galia={galiaResponse} button1={buttons.button1} button2={buttons.button2}/>
        </div>
      </div>
    </div>
  );
}

export default App;
