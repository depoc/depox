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
  userButton.classList.add(
    'ring-zinc-400', 'text-zinc-400',
    'dark:ring-zinc-500', 'dark:text-zinc-500'
  );
  empresaButton.classList.add(
    'ring-zinc-400', 'text-zinc-400',
    'dark:ring-zinc-500', 'dark:text-zinc-500'
  );
  equipeButton.classList.add(
    'ring-zinc-400', 'text-zinc-400',
    'dark:ring-zinc-500', 'dark:text-zinc-500'
  );
}

// Function to set the first button as selected
function selectDefaultButton() {
  resetButtonStyles(); // Reset styles
  hideAllSections(); // Hide all sections
  userSection.classList.remove('hidden'); // Show the user settings section
  userButton.classList.remove(
    'ring-zinc-400', 'text-zinc-400',
    'dark:ring-zinc-500', 'dark:text-zinc-500'
  );
  userButton.classList.add(
    'ring-black', 'text-black',
    'dark:ring-zinc-300', 'dark:text-zinc-300'
  );
}

// Event listeners for each button
userButton.addEventListener('click', () => {
  hideAllSections(); // Hide other sections
  resetButtonStyles();
  userSection.classList.remove('hidden'); // Show the user settings section
  userButton.classList.remove(
    'ring-zinc-400', 'text-zinc-400',
    'dark:ring-zinc-500', 'dark:text-zinc-500'
  );
  userButton.classList.add(
    'ring-black', 'text-black',
    'dark:ring-zinc-300', 'dark:text-zinc-300'
  );
});

empresaButton.addEventListener('click', () => {
  hideAllSections();
  resetButtonStyles();
  empresaSection.classList.remove('hidden'); // Show the empresa settings section
  empresaButton.classList.remove(
    'ring-zinc-400', 'text-zinc-400',
    'dark:ring-zinc-500', 'dark:text-zinc-500'
  );
  empresaButton.classList.add(
    'ring-black', 'text-black',
    'dark:ring-zinc-300', 'dark:text-zinc-300'
  );
});

equipeButton.addEventListener('click', () => {
  hideAllSections();
  resetButtonStyles();
  equipeSection.classList.remove('hidden'); // Show the equipe settings section
  equipeButton.classList.remove(
    'ring-zinc-400', 'text-zinc-400',
    'dark:ring-zinc-500', 'dark:text-zinc-500'
  );
  equipeButton.classList.add(
    'ring-black', 'text-black',
    'dark:ring-zinc-300', 'dark:text-zinc-300'
  );
});

// Call this function to select the first button on page load
selectDefaultButton();
