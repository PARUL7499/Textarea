import React, { useState } from 'react'

function Textarea() {

    const [text, setText] = useState("enter....")

    function upper() 
    {
        let newText = text.toUpperCase();
        setText(newText)
    }

    function lower() {
        let newText = text.toLowerCase();
        setText(newText)

    }

    function clear()
    {
        setText("")
    }


    return (
        <>
            <div className="container my-4">
                <div className="form-group">
                    <h1>Drop Your Text</h1>
                    <textarea 
                    className="form-control" 
                    id="exampleFormControlTextarea1"
                    rows="11"
                    value={text}
                     onChange={(e) => setText(e.target.value)}
                    >


                   </textarea>

                    <button onClick={upper} type="button" className="btn btn-primary mt-2 mr-4">Upper</button>

                    <button onClick={lower} type="button" className="btn btn-primary mt-2 ">Lower</button>

                    <button onClick={clear} type="button" className="btn btn-primary ml-4 mt-2 ">Clear</button>


                </div>

                <div className="container">

                    <h3>preview</h3>

                    <code>
                        <h4>{text}</h4>
                    </code>

                    <b>{ text.split(" ").length} words {text.length} characters</b>
                    <br />

                    <b><i>{text.split("").length* 0.25} s is Your Reading time </i></b>
                </div>
            </div>
        </>
    )
}

export default Textarea
