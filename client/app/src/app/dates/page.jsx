import React from 'react';
import Link from 'next/link';

const NavBar = () => {
  const dates =localStorage.getItem('dates')
  return (
    <div className="flex w-full h-screen p-0 m-0">
      <div className="w-1/3 bg-black bg-opacity-8 flex flex-col justify-center items-center">
        <nav className="flex flex-col justify-center items-center flex-grow text-lg">
          <ul className="list-none">
            <li className="mb-4">
              <p className="text-white hover:text-yellow-300">
                <Link href="/dates">Dates</Link>
              </p>
            </li>
            <li className="mb-4">
              <p className="text-white hover:text-yellow-300">
                <Link href="/definitions">Definitions</Link>
              </p>
            </li>
            <li className="mb-4">
              <p className="text-white hover:text-yellow-300">
                <Link href="/examples">Examples</Link>
              </p>
            </li>
            <li>
              <p className="text-white hover:text-yellow-300">
                <Link href="/summary">Summary</Link>
              </p>
            </li>
          </ul>
        </nav>
      </div>

      <div className="w-2/3 flex justify-center items-center bg-brown-1 h-screen">
          {dates.map((date, index) => (
            <div key={index}>
              {date}
            </div>
          ))}
      </div>
    </div>
  );
};

export default NavBar;
