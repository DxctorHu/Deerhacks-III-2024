import React from 'react'
import Head from 'next/head';
import Link from 'next/link';
import './styles.modules.css';

<Head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta charSet="UTF-8" />
  <title> Gist - Get the gist of anything in seconds </title>

</Head>

export default function Page() {
  return (
    <div className="flex text-white bg-brown-1">
      {/* Text */}
      <div className="font-martel flex flex-col justify-center w-1/3 left-align m-[5%]">
        <h1 className="font-martel text-xl font-bold mb-6">Get the <span className='italic'>Gist</span> of anything in <span className='text-yellow-300'>seconds</span></h1>
        <p className="font-martel text-lg text-white opacity-75 mb-6">
          Upload a document and get a breakdown of all the important concepts you need to know
        </p>
        <Link href="/upload">
          <button className="py-4 px-15 text-lg bg-brown-3 text-white rounded-3 hover:opacity-70 cursor-pointer">
            Start Here
          </button>
        </Link>
        <p className="text-sm mt-6">Supported file types: PDF</p>
      </div>
      {/* Image */}
      <div className="flex w-2/3 items-center justify-center m-[5%]">
        <img
          className="object-cover h-full w-full" // This will cover the entire area of the div
          src="https://i.imgur.com/eLFXYK3.png"
          alt="darkAcademicTextbook"
        />
      </div>
    </div>
  )
}
  




