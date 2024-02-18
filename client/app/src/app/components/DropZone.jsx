'use client'
import {React, useCallback} from 'react';
import { useDropzone } from 'react-dropzone'
import { useRouter } from 'next/navigation';

export default function DropZone(){
  const router = useRouter()

  const onDrop = useCallback(acceptedFiles => {
    const file = acceptedFiles[0]
    const formData = new FormData();

    formData.append('file',file)
    fetch('http://127.0.0.1:8080/upload', { 
      mode: 'no-cors',
      method: 'POST',
      body: formData
  })
  .then(response => response.json())
  .then(data => {
    console.log("uploaded:", data)
    localStorage.setItem('dates',data.dates)
    localStorage.setItem('examples',data.examples)
    localStorage.setItem('definitions',data.defintions)
    localStorage.setItem('summary',data.summary)

    router.push('/navigation')

  })
  .catch(error => {
    console.log("error",error)
    router.push('/navigation')

  })
  }, []);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });
    return (
      <div className="min-h-screen flex flex-col justify-center items-center bg-brown-1">
        <h1 className="text-3xl text-white font-bold mb-8">Upload Your PDF</h1>
        <div {...getRootProps()} className="max-w-md w-full cursor-pointer">
          <input {...getInputProps()} />
          <div className={` border rounded-lg shadow-md p-8 ${isDragActive ? 'border-green-400' : 'border-gray-300'}`}>
            <div className="flex justify-center min-h-64 items-center border-dashed border-2 border-gray-300 rounded-lg">
              <svg
                className={`w-8 h-8 ${isDragActive ? 'text-green-400' : 'text-gray-400'} mr-2`}
                fill="none"
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path d="M8 17l4 4 4-4m-4-5v9"></path>
                <path d="M20 21H4a2 2 0 01-2-2V5a2 2 0 012-2h5l2 3h6l2-3h5a2 2 0 012 2v14a2 2 0 01-2 2z"></path>
              </svg>
              <span className={isDragActive ? 'text-green-400 m-3' : 'text-gray-400'}>{isDragActive ? 'Drop your PDF here' : 'Drop your PDF here'}</span>
            </div>
            <p className="text-sm text-gray-400 mt-4">Or click to select a file</p>
          </div>
        </div>
      </div>
  );
};


