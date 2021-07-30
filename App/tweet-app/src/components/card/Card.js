import React from 'react'
import './Card.css'

function Card({title, note, theme, tweet, isinput, button, button1, button2}) {


    return (
        <div className="card">
            <div className="card-body text-center">
                <h4 className="card-title">{title}</h4>
                <h5 className="card-text">{note}</h5>
                <div className="card-bot">
                    {isinput}
                    {button}
                </div>
                <div className="card-buttons">
                    {button1}
                    {button2}
                </div>
            </div>
        </div>
    ) 
}

export default Card
