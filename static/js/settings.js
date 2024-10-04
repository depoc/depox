const settingsButton = document.getElementById('settingsButton');
const settings = document.getElementById('settings');
const closeSettings = document.getElementById('closeSettings');

settingsButton.addEventListener('click', () => {
  settings.classList.remove('hidden');
  settings.classList.add('flex');
});

closeSettings.addEventListener('click', () => {
  settings.classList.add('hidden');
});

settings.addEventListener('click', (event) => {
  if (event.target === settings) {
    settings.classList.add('hidden');
  }
});

// Add event listener for the 'u' key
document.addEventListener('keydown', (event) => {
  if (event.key === 'a') {
    // Toggle the visibility of the settings modal
    if (settings.classList.contains('hidden')) {
      settings.classList.remove('hidden');
      settings.classList.add('flex');
    } else {
      settings.classList.add('hidden');
    }
  }
});