const userEditButton = document.getElementById('userEditButton');
const userEdit = document.getElementById('userEdit');
const closeUserEdit = document.getElementById('closeUserEdit');

userEditButton.addEventListener('click', () => {
  userEdit.classList.remove('hidden');
  userEdit.classList.add('flex');
});

closeUserEdit.addEventListener('click', () => {
  userEdit.classList.add('hidden');
});

userEdit.addEventListener('click', (event) => {
  if (event.target === userEdit) {
    userEdit.classList.add('hidden');
  }
});