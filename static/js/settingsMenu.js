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

// Event listeners for each button
userButton.addEventListener('click', () => {
  hideAllSections(); // Hide other sections
  userSection.classList.remove('hidden'); // Show the user settings section
});

empresaButton.addEventListener('click', () => {
  hideAllSections();
  empresaSection.classList.remove('hidden');
});

equipeButton.addEventListener('click', () => {
  hideAllSections();
  equipeSection.classList.remove('hidden');
});
