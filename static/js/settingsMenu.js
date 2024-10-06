// Select all buttons and sections
const userButton = document.querySelector('#settingsUserButton');
const empresaButton = document.querySelector('#settingsEmpresaButton');
const equipeButton = document.querySelector('#settingsEquipeButton');

const userSection = document.querySelector('#userSettings');
const empresaSection = document.querySelector('#empresaSettings');
const equipeSection = document.querySelector('#equipeSettings');

// Function to hide all sections
function hideAllSections() {
  userSection.classList.add('hidden');
  empresaSection.classList.add('hidden');
  equipeSection.classList.add('hidden');
}

// Function to reset button styles
function resetButtonStyles() {
  userButton.classList.remove('bg-zinc-50', 'dark:bg-primary');
  empresaButton.classList.remove('bg-zinc-50', 'dark:bg-primary');
  equipeButton.classList.remove('bg-zinc-50', 'dark:bg-primary');
}

// Function to set the first button as selected
function selectDefaultButton() {
  resetButtonStyles(); // Reset styles
  hideAllSections(); // Hide all sections
  userSection.classList.remove('hidden'); // Show the user settings section
  userButton.classList.add('bg-zinc-50', 'dark:bg-primary'); // Apply active styles including dark mode
}

// Event listeners for each button
userButton.addEventListener('click', () => {
  hideAllSections(); // Hide other sections
  resetButtonStyles();
  userSection.classList.remove('hidden'); // Show the user settings section
  userButton.classList.add('bg-zinc-50', 'dark:bg-primary'); // Apply light and dark mode styles
});

empresaButton.addEventListener('click', () => {
  hideAllSections();
  resetButtonStyles();
  empresaSection.classList.remove('hidden'); // Show the empresa settings section
  empresaButton.classList.add('bg-zinc-50', 'dark:bg-primary'); // Apply light and dark mode styles
});

equipeButton.addEventListener('click', () => {
  hideAllSections();
  resetButtonStyles();
  equipeSection.classList.remove('hidden'); // Show the equipe settings section
  equipeButton.classList.add('bg-zinc-50', 'dark:bg-primary'); // Apply light and dark mode styles
});

// Call this function to select the first button on page load
selectDefaultButton();
