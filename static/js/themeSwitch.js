function init() {
  preloadTheme();

  // Select all buttons with the class name 'light-theme-button'
  const lightThemeButtons = document.querySelectorAll(".light-theme-button");

  // Add an event listener to each light theme button
  lightThemeButtons.forEach(button => {
    button.addEventListener("click", () => {
      localStorage.setItem("theme", "light");
      toggleTheme(false);
      toggleButtons(); // Call toggleButtons after changing the theme
    });
  });

  // Select all buttons with the class name 'dark-theme-button'
  const darkThemeButtons = document.querySelectorAll(".dark-theme-button");

  // Add an event listener to each dark theme button
  darkThemeButtons.forEach(button => {
    button.addEventListener("click", () => {
      localStorage.setItem("theme", "dark");
      toggleTheme(true);
      toggleButtons(); // Call toggleButtons after changing the theme
    });
  });

  const systemThemeButton = document.getElementById("system-theme-button");

  systemThemeButton?.addEventListener("click", () => {
    localStorage.setItem("theme", "system");
    toggleTheme(window.matchMedia("(prefers-color-scheme: dark)").matches);
    toggleButtons(); // Call toggleButtons after changing the theme
  });

  window.matchMedia("(prefers-color-scheme: dark)").addEventListener("change", (event) => {
    if (localStorage.theme === "system") {
      toggleTheme(event.matches);
      toggleButtons(); // Call toggleButtons after changing the theme
    }
  });
}

function toggleTheme(dark) {
  const css = document.createElement("style");

  css.appendChild(
    document.createTextNode(
      `* {
       -webkit-transition: none !important;
       -moz-transition: none !important;
       -o-transition: none !important;
       -ms-transition: none !important;
       transition: none !important;
    }`,
    ),
  );

  document.head.appendChild(css);

  if (dark) {
    document.documentElement.classList.add("dark");
  } else {
    document.documentElement.classList.remove("dark");
  }

  window.getComputedStyle(css).opacity;
  document.head.removeChild(css);
}

function preloadTheme() {
  const userTheme = localStorage.theme;

  if (userTheme === "light" || userTheme === "dark") {
    toggleTheme(userTheme === "dark");
  } else {
    toggleTheme(window.matchMedia("(prefers-color-scheme: dark)").matches);
  }
  toggleButtons(); // Call toggleButtons to adjust visibility based on the initial theme
}

function toggleButtons() {
  const lightThemeButtons = document.querySelectorAll(".light-theme-button");
  const darkThemeButtons = document.querySelectorAll(".dark-theme-button");

  // Check if the current theme is dark or light
  const isDarkTheme = document.documentElement.classList.contains("dark");

  // Show light buttons when the theme is dark
  lightThemeButtons.forEach(button => {
    button.classList.toggle('hidden', !isDarkTheme);
    button.classList.toggle('flex', isDarkTheme);
  });

  // Show dark buttons when the theme is light
  darkThemeButtons.forEach(button => {
    button.classList.toggle('hidden', isDarkTheme);
    button.classList.toggle('flex', !isDarkTheme);
  });
}

document.addEventListener("DOMContentLoaded", () => init());
