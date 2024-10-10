const passwordButtons = document.querySelectorAll('.passwordButton');
const password = document.getElementById('password');
const closePassword = document.getElementById('closePassword');

passwordButtons.forEach((button) => {
  button.addEventListener('click', () => {
    password.classList.remove('hidden');
    password.classList.add('flex');
  });
});

closePassword.addEventListener('click', () => {
  password.classList.add('hidden');
});

password.addEventListener('click', (event) => {
  if (event.target === password) {
    password.classList.add('hidden');
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') { 
    if (password.classList.contains('flex')) {
      password.classList.remove('flex');
      password.classList.add('hidden');
    }
  }
});
