/** @type {import('tailwindcss').Config} */
const defaultTheme = require("tailwindcss/defaultTheme");
const colors = require("tailwindcss/colors");
module.exports = {
  content: [
    './users/templates/users/**/*.html',
    './users/templates/users/*.html',
    './users/forms.py',
    './erp/forms.py',

    './erp/templates/erp/**/*.html',
    './erp/templates/erp/*.html',

    './finance/templates/finance/**/*.html',
    './finance/templates/finance/*.html',   

    './templates/**/*.html',
    './templates/*.html',
    
    './static/js/erp/*.js',    
    './static/js/*.js',
  ],
  darkMode: 'selector', // Enable selector strategy for dark mode
  theme: {
    fontSize: {
      xs: [
        "0.75rem",
        {
          lineHeight: "1rem",
        },
      ],
      sm: [
        "0.875rem",
        {
          lineHeight: "1.5rem",
        },
      ],
      base: [
        "1rem",
        {
          lineHeight: "1.75rem",
        },
      ],
      lg: [
        "1.125rem",
        {
          lineHeight: "2rem",
        },
      ],
      xl: [
        "1.25rem",
        {
          lineHeight: "2rem",
        },
      ],
      "2xl": [
        "1.5rem",
        {
          lineHeight: "2rem",
        },
      ],
      "3xl": [
        "2rem",
        {
          lineHeight: "2.5rem",
        },
      ],
      "4xl": [
        "2.5rem",
        {
          lineHeight: "3.5rem",
        },
      ],
      "5xl": [
        "3rem",
        {
          lineHeight: "3.5rem",
        },
      ],
      "6xl": [
        "3.75rem",
        {
          lineHeight: "1",
        },
      ],
      "7xl": [
        "4.5rem",
        {
          lineHeight: "1.1",
        },
      ],
      "8xl": [
        "6rem",
        {
          lineHeight: "1",
        },
      ],
      "9xl": [
        "8rem",
        {
          lineHeight: "1",
        },
      ],
    },
    extend: {
      boxShadow: {
        thick: "0px 7px 32px rgb(0 0 0 / 35%);",
      },
      colors: {
        "primary": "#101010",
        "secondary": "#1a1a1a",
        "tertiary": "#262626",

        "off":"#ececec",
        "background":"#f7f7f5",
      },
      borderRadius: {
        "4xl": "2rem",
        "5xl": "3rem",
        "6xl": "5rem",
      },
      fontFamily: {
        sans: ["Inter", ...defaultTheme.fontFamily.sans],
      },
      transitionProperty: {
        'opacity': 'opacity',
      },
      transitionTimingFunction: {
        'custom': 'ease-in-out',
      },
      transitionDuration: {
        'fade': '300ms',
      },      
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    function ({ addUtilities }) {
      addUtilities({
        '.no-scrollbar': {
          '-ms-overflow-style': 'none', /* IE and Edge */
          'scrollbar-width': 'none', /* Firefox */
        },
        '.no-scrollbar::-webkit-scrollbar': {
          display: 'none', /* Chrome, Safari, and Edge */
        },
      });
    },
  ],
}