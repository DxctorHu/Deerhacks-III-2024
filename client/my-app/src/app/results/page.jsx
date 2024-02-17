'use client'
import {React, useEffect, useState }from 'react'


function page() {

  const [message,setMessage] = useState("Loading")
  const [categories, setCategories] = useState([])
  const [output, setOutput] = useState("Loading..")
  var Latex = require('react-latex')

  useEffect(() =>{
    fetch("http://127.0.0.1:8080/api/home")
    .then((response) => response.json())
    .then(data => {
      setMessage(data.message)
      setCategories(data.categories)
      setOutput(data.output)
    })

  }, [])
    const out = <Latex>{output}</Latex>

  
  return (
    <div>
      <div>{message}</div>
     <div>{categories.map((category,index) => (
        <div key={index}>{category}</div>
      ))}</div> 
      <div>{out}</div>
      <div>{<Latex displayMode={true}>{'$\sqrt{\sin ^2\left(-1\right)}\le \:1-\sin \left(x\right)$'}</Latex>}</div>
    </div>
  )
}

export default page
