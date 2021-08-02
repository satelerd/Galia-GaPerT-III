import React from 'react'
import './Card.css'


function Card({title, note, theme, tweet, isinput, galia, button, button1, button2}) {

    return (
        <div className="card">
            <div className="card-body text-center">
                <h4 className="card-title">{title}</h4>
                <h5 className="card-text">{note}</h5>
                

                <div className="card-res">
                    <h5>{theme}</h5>
                    <h5>{galia}</h5>
                </div>

                <div className="card-bot">
                    {isinput}
                    {button}
                    {button1}
                    {button2}
                </div>

                {/* <div className="card-buttons">
                    {button1}
                    {button2}
                </div> */}
            </div>
        </div>
    ) 
}

export default Card
