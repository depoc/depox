const settingsButtons = document.querySelectorAll('#settingsButton');
const settings = document.getElementById('settings');
const closeSettings = document.getElementById('closeSettings');

settingsButtons.forEach((button) => {
  button.addEventListener('click', () => {
    settings.classList.remove('hidden');
    settings.classList.add('flex');
  });
});

closeSettings.addEventListener('click', () => {
  settings.classList.add('hidden');
});

settings.addEventListener('click', (event) => {
  if (event.target === settings) {
    settings.classList.add('hidden');
  }
});

document.addEventListener('keydown', (event) => {
  if (event.target.tagName === 'INPUT' || 
    event.target.tagName === 'TEXTAREA' || 
    event.target.isContentEditable) {
    return;
  }

  if (event.key.toLowerCase() === 'a' ) {
    if (settings.classList.contains('hidden')) {
      settings.classList.remove('hidden');
      settings.classList.add('flex');
    }
  }
  if (event.key === 'Escape') { 
    if (settings.classList.contains('flex')) {
      settings.classList.remove('flex');
      settings.classList.add('hidden');
    }
  }
});