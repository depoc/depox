// Select all buttons and sections
const buttons = {
  user: document.querySelector('#settingsUserButton'),
  empresa: document.querySelector('#settingsEmpresaButton'),
  equipe: document.querySelector('#settingsEquipeButton')
};

const sections = {
  user: document.querySelector('#userSettings'),
  empresa: document.querySelector('#empresaSettings'),
  equipe: document.querySelector('#equipeSettings')
};

// Function to hide all sections
function hideAllSections() {
  Object.values(sections).forEach(section => section.classList.add('hidden'));
}

// Function to reset button styles
function resetButtonStyles() {
  Object.values(buttons).forEach(button => {
    button.classList.add('ring-black/15', 'text-zinc-500', 'dark:ring-white/20', 'dark:text-white/45');
    button.classList.remove('ring-black', 'text-black', 'dark:ring-zinc-300', 'dark:text-zinc-300');
  });
}

// Function to handle section display and button styles
function showSection(sectionKey) {
  hideAllSections();
  resetButtonStyles();
  sections[sectionKey].classList.remove('hidden');
  buttons[sectionKey].classList.remove('ring-black/15', 'text-zinc-500', 'dark:ring-white/20', 'dark:text-white/45');
  buttons[sectionKey].classList.add('ring-black', 'text-black', 'dark:ring-zinc-300', 'dark:text-zinc-300');
}

// Event listeners for each button
buttons.user.addEventListener('click', () => showSection('user'));
buttons.empresa.addEventListener('click', () => showSection('empresa'));
buttons.equipe.addEventListener('click', () => showSection('equipe'));

// Select the first button on page load
showSection('user');
