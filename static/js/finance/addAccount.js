const addAccount = document.getElementById('addAccount');
const addAccountButton = document.getElementById('addAccountButton');
const closeAddAccount = document.getElementById('closeAddAccount');

addAccountButton.addEventListener('click', () => {
  addAccount.classList.remove('hidden');
  addAccount.classList.add('flex');
})

closeAddAccount.addEventListener('click', () => {
  addAccount.classList.add('hidden')
})

addAccount.addEventListener('click', (event) => {
  if (event.target === addAccount) {
    addAccount.classList.add('hidden');
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') { 
    if (addAccount.classList.contains('flex')) {
      addAccount.classList.remove('flex');
      addAccount.classList.add('hidden');
    }
  }
});