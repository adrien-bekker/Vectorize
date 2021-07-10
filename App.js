import './App.css';
import axios from "axios";
import arrow from "./assets/arrow.png";

const App = (props) => {
    const [picture, setPicture] = useState(props.picture);
    const [endPicture, setEndPicture] = useState(props.endPicture);

    onDropHandler = (event) => {
        setPicture(URL.createObjectURL(event.target.files[0]))
    }

    return (
        <div className="App">
            <h1>Upload Image Here: </h1>
            <div className="ImageBoxes">
                <img src={picture} style={{height: "450px", width: "450px"}} />
                <img src={arrow} style={{height: "100px", width: "100px"}} />
                <img src={endPicture} style={{height: "450px", width: "450px"}} />
            </div>
        </div>
    );

}