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
  userButton.classList.remove('bg-zinc-50');
  empresaButton.classList.remove('bg-zinc-50');
  equipeButton.classList.remove('bg-zinc-50');
}

// Event listeners for each button
userButton.addEventListener('click', () => {
  hideAllSections(); // Hide other sections
  resetButtonStyles();
  userSection.classList.remove('hidden'); // Show the user settings section
  userButton.classList.add('bg-zinc-50');
});

empresaButton.addEventListener('click', () => {
  hideAllSections();
  resetButtonStyles();
  empresaSection.classList.remove('hidden');
  userButton.classList.add('bg-zinc-50');
});

equipeButton.addEventListener('click', () => {
  hideAllSections();
  resetButtonStyles();
  equipeSection.classList.remove('hidden');
  userButton.classList.add('bg-zinc-50');
});
