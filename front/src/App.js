import React, {useState, useEffect} from 'react';
import "./styles/style.css"

function App() {

  const [data, setData] = useState(0)
  
  useEffect (() => {
    fetch("/words").then(
        res => res.json()
      ).then(
        data => {

          setData(data)
        }
      )
    }, [])

  return (
    <div className='container'>

      <div className='content'>

        <h1>{data.term}</h1>

        <p>{data.defintion}</p>

        <iframe src={data.gif} alt="a gif based on the randomly picked word"></iframe><p><a href={data.gif}></a></p>

      
        <button onClick = {() => {
          fetch("/words").then(
              res => res.json()
            ).then(
              data => {

                setData(data)
                // console.log(data)
              })
              }}>NEW WORD</button>
      

      </div>
    </div>
  
  ) 
}


export default App