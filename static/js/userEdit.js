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

// Add event listener for the 'u' key
document.addEventListener('keydown', (event) => {
  if (event.key === 'u') {
    // Toggle the visibility of the userEdit modal
    if (userEdit.classList.contains('hidden')) {
      userEdit.classList.remove('hidden');
      userEdit.classList.add('flex');
    } else {
      userEdit.classList.add('hidden');
    }
  }
});