const modalButton = document.getElementById('mobileMenuButton');
const modal = document.getElementById('mobileMenu');
const closeModal = document.getElementById('closeMobileMenu');

modalButton.addEventListener('click', () => {
modal.classList.remove('hidden');
modal.classList.add('flex');
});

closeModal.addEventListener('click', () => {
modal.classList.add('hidden');
});

modal.addEventListener('click', (event) => {
if (event.target === modal) {
  modal.classList.add('hidden');
}
});