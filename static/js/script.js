// Theme switch
function init() {
    preloadTheme();
  
    // Select all buttons with the class name 'dark-theme-button'
    const LightThemeButtons = document.querySelectorAll(".light-theme-button");

    // Add an event listener to each button
    LightThemeButtons.forEach(button => {
      button.addEventListener("click", () => {
        localStorage.setItem("theme", "light");
        toggleTheme(false);
      });
    });
  
    // Select all buttons with the class name 'dark-theme-button'
    const darkThemeButtons = document.querySelectorAll(".dark-theme-button");

    // Add an event listener to each button
    darkThemeButtons.forEach(button => {
      button.addEventListener("click", () => {
        localStorage.setItem("theme", "dark");
        toggleTheme(true);
      });
    });
  
    const systemThemeButton = document.getElementById(
      "system-theme-button",
    );
  
    systemThemeButton?.addEventListener("click", () => {
      localStorage.setItem("theme", "system");
      toggleTheme(
        window.matchMedia("(prefers-color-scheme: dark)").matches,
      );
    });
  
    window
      .matchMedia("(prefers-color-scheme: dark)")
      .addEventListener("change", (event) => {
        if (localStorage.theme === "system") {
          toggleTheme(event.matches);
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
      }
    `,
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
      toggleTheme(
        window.matchMedia("(prefers-color-scheme: dark)").matches,
      );
    }
  }
  
  document.addEventListener("DOMContentLoaded", () => init());
  document.addEventListener("astro:after-swap", () => init());
  preloadTheme();

// Mobile Menu
const modalButton = document.getElementById('mobileMenuButton');
const modal = document.getElementById('mobileMenu');
const closeModal = document.getElementById('closeMobileMenu');

modalButton.addEventListener('click', () => {
  modal.classList.remove('hidden');
  modal.classList.add('flex');
});

closeModal.addEventListener('click', () => {
  modal.classList.add('hidden');
});

modal.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.classList.add('hidden');
  }
});

// User Edit
const userEditButton = document.getElementById('userEditButton');
const userEdit = document.getElementById('userEdit');
const closeUserEdit = document.getElementById('closeUserEdit');

userEditButton.addEventListener('click', () => {
  userEdit.classList.remove('hidden');
  userEdit.classList.add('flex');
});

closeUserEdit.addEventListener('click', () => {
  userEdit.classList.add('hidden');
});

userEdit.addEventListener('click', (event) => {
  if (event.target === userEdit) {
    userEdit.classList.add('hidden');
  }
});

