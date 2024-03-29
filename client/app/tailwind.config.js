/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
      fontFamily: {
        martel: ["Martel Sans"]

      },
      fontSize:{
        'lg': '35px',
        'xl': '70px',
      },
      colors: {
        'brown-1': '#513520',
        'brown-2': '#956542',
        'brown-3': '#C19A6b'
      }

    },
  },
  plugins: [],
};