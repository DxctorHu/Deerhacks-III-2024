'use client'
import {React, useEffect, useState }from 'react'


function page() {

  const [message,setMessage] = useState("Loading")
  // const [categories, setCategories] = useState([])

  
  // useEffect(() =>{
  //   fetch("http://127.0.0.1:8080/api/home")
  //   .then((response) => response.json())
  //   .then(data => {
  //     setMessage(data.message)
  //     setCategories(data.categories)
  //   })

  // }, [])
    
  useEffect(() =>{
    fetch("http://127.0.0.1:8080/upload")
    .then((response) => response.json())
    .then(data => {
      setMessage(data.message)
    })

  }, [])
  
  return (
    <div>
      <div>{message}</div>
     {/* <div>{categories.map((category,index) => (
        <div key={index}>{category}</div>
      ))}</div> 
      <div>{message}</div> */}
    </div>
  )
}

export default page
