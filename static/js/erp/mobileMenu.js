const modalButton = document.getElementById('mobileMenuButton');
const modal = document.getElementById('mobileMenu');
const closeModal = document.getElementById('closeMobileMenu');

modalButton.addEventListener('click', () => {
  modal.classList.remove('hidden');
  modal.classList.add('flex');
});

closeModal.addEventListener('click', () => {
  modal.classList.add('hidden');
  modal.classList.remove('flex'); // Ensures 'flex' class is removed
});

modal.addEventListener('click', (event) => {
  if (event.target === modal) {
    modal.classList.add('hidden');
    modal.classList.remove('flex'); // Ensures 'flex' class is removed
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key.toLowerCase() === 'm') {
    if (modal.classList.contains('hidden')) {
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    }
  }
  if (event.key === 'Escape') { 
    if (modal.classList.contains('flex')) {
      modal.classList.remove('flex');
      modal.classList.add('hidden');
    }
  }
});
