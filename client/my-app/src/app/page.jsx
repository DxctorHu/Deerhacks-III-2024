import React from 'react'
import './styles.modules.css'
import Image from 'next/image';
import Head from 'next/head';
import Link from 'next/link';
<Head>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta charSet="UTF-8" />
  <title> Gist - Get the gist of anything in seconds </title>

</Head>

export default function Page(){
  return (
    <div className="flex">
    {/* Text */}
    <div className="font-koh flex flex-col justify-center w-1/2 p-8 text-center" >
      <h1 className="font-koh text-xl font-bold mb-6">Get the gist of anything in seconds</h1>
      <p className="font-koh text-lg opacity-75 mb-6">Upload a document and get a breakdown of all the important concepts you need to know</p>
      <Link href="/upload"><button className="py-4 px-12 text-lg bg-black text-white rounded-full cursor-pointer">  Start Here </button> </Link>
      <p className="text-sm mt-6">Supported file types: PDF</p>
    </div>
    {/* Image */}
    <div className="w-1/2">
      <Image src="/darkAcademiaTextbook.png" width={850} height={703} alt="darkAcademiaTextbook" />
    </div>
  </div>
  


  );
}


