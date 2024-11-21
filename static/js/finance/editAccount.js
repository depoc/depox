const editBankAccount = document.getElementById('editBankAccount');
const editBankAccountButton = document.getElementById('editBankAccountButton');
const closeBankAccount = document.getElementById('closeBankAccount');

editBankAccountButton.addEventListener('click', () => {
  editBankAccount.classList.remove('hidden');
  editBankAccount.classList.add('flex');
})

closeBankAccount.addEventListener('click', () => {
  editBankAccount.classList.add('hidden')
})

editBankAccount.addEventListener('click', (event) => {
  if (event.target === editBankAccount) {
    editBankAccount.classList.add('hidden');
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') { 
    if (editBankAccount.classList.contains('flex')) {
      editBankAccount.classList.remove('flex');
      editBankAccount.classList.add('hidden');
    }
  }
});