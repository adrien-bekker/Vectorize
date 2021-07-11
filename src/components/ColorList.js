import { useState } from "react";

const colorValueHandler = (event) => {
    console.log(event.target.value)
}

const colorList = () => {
    return (
        <input type = "color" onChange={colorValueHandler}/>
    );
}

export default colorList;