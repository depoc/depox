const settingsUserButton = document.querySelector('#settingsUserButton');
const userInfo = document.querySelector('#userInfo');

settingsUserButton.addEventListener('click', () => {
  userInfo.classList.remove('hidden');
});

