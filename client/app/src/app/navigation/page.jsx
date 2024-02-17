import React from 'react'
import Link from 'next/link';
import Image from 'next/image';
import styles from 'styles.modules.css';

const NavBar = () => {
  return (
    <body className = "m-0 p-0 bg-[#513520] font-koh text-[2.2vw] flex"> 
    <nav className="bg-black bg-opacity-70 p-4 text-white">
      <ul className="list-none m-0 p-0 bg-black bg-opacity-70">
      <li className= "className=text-white p-0 m-0">
          <Link href="/overview" className="text-white no-underline items-center flex p-0 px-1">
              <img src="/star.svg" alt="Overview" />
          </Link>
        </li>
        <li className="className=text-white p-0 m-0">
          <Link href="/definitions" className="text-white no-underline items-center flex p-0 px-1">
            <Image src='/next.svg' width={50} height={50} />
          </Link>
        </li>
        <li className="className=text-white p-0 m-0">
          <Link href="/formulas" className="text-white no-underline items-center flex p-0 px-1">
              <img src="/star.svg" alt="Formulas" />
          </Link>
        </li>
        <li className="className=text-white p-0 m-0">
          <Link href="/examples" className="text-white no-underline items-center flex p-0 px-1">
              <img src="/star.svg" alt="Examples" />
          </Link>
        </li>
        <li className="className=text-white p-0 m-0">
          <Link href="/summary" >
              <img src="/star.svg" alt="Summary" />
          </Link>
        </li>
      </ul>
    </nav>
    </body> 
  );
};

export default NavBar;
