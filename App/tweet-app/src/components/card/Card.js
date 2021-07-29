import React from 'react'
import './Card.css'

function Card({title, note, theme, tweet, isinput, button, button1, button2}) {


    return (
        <div className="card">
            <div className="card-body text-center">
                <h4 className="card-title">{title}</h4>
                <h5 className="card-text">{note}</h5>
                {isinput}
                {button}

                {button1}
                {button2}
            </div>
        </div>
    ) 
}

export default Card
