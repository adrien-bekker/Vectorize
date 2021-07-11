import './App.css';
import axios from "axios";
import arrow from "./assets/arrow.png";
import React, { useState } from 'react';
import endImg from "./assets/vectorized.png";
import loading from "./assets/loading.gif";

const App = (props) => {
    const [picture, setPicture] = useState(props.picture);
    const [pictureData, setPictureData] = useState(props.pictureData);
    const [endPicture, setEndPicture] = useState(props.endPicture);
    const [colors, setColors] = useState([{id: 0, color: "#ffffff"}, {id: 1, color: "#000000"}]);
    const [download, setDownload] = useState(null);

    const pyServer = axios.create({baseURL: "https://f52704964933.ngrok.io"});

    

    let tempColors = colors;

    const onDropHandler = (event) => {
      setPicture(URL.createObjectURL(event.target.files[0]));
      setPictureData(event.target.files[0]);
      console.log(event.target);
    }

    const onColorChange = (event, id) => {
      tempColors = colors.map(color => {
        if (color.id == id) {
          return {...color, color: event.target.value}
        }
        return color;
      })
      setColors([...tempColors]);

    }

    const newColor = {color: "#ffffff", id: tempColors.length};
    const addColor = () => {
      setColors([...tempColors, newColor]);
    }

    const subtractColor = () => {
      tempColors.pop();
      setColors([...tempColors]);
    }

    const vectorize = () => {
      let hexColors = "";
      colors.forEach(color => hexColors += color.color);
      hexColors = hexColors.replaceAll("#", "%23");
      console.log(hexColors);
      setDownload(<img src = {loading} style = {{height: "40px", width: "40px"}}/>);
      pyServer.get("/vectorize/" + hexColors).then((res) => {
        setEndPicture("")
        setEndPicture(endImg);
        setDownload(<a href='data:image/png;base64,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' download>Click to download</a>);
      });
      }
      
    return (
        <div className="App">
            <h1>Vectorize!</h1>
            <div className="ImageBoxes">
                <img src={picture} className="fadeInImage" style={{height: "300px", width: "300px"}} />
                <img src={arrow} style={{height: "50px", width: "100px", marginBottom: "7%", cursor: "pointer"}} onClick={vectorize} />
                <img src={endPicture} className="fadeInImage" style={{height: "300px", width: "300px"}} />
            </div>
            <input type="file" id="file" onChange={onDropHandler} style={{width: "0.1px", height: "0.1px"}} />
            <label for="file">Select an image!</label>
            <div>
              <h2>Add/Remove Color</h2>
              <label onClick={addColor}>+</label>
              <label onClick={subtractColor}>-</label>
            </div>
            <div style={{marginTop: "25px"}}>
              {colors.map((color, i) => {
                return <input type = "color" value={color.color} onChange={(event) => onColorChange(event, i)} id={i} />
              })}
            </div>
            <div className="downloadButton" style={{marginTop: "20px"}}>
              {download}
            </div>
        </div>
    );
}

export default App;
