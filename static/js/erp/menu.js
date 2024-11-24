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
  if (event.target.tagName === 'INPUT' || 
    event.target.tagName === 'TEXTAREA' || 
    event.target.tagName === 'SELECT' || 
    event.target.isContentEditable) {
    return;
  }

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

let lastScrollPosition = 0;

window.addEventListener('scroll', () => {
  const currentScrollPosition = window.scrollY;
  const bottomOffset = 50;

  const nearBottom = (window.innerHeight + window.scrollY) >= (document.body.offsetHeight - bottomOffset);

  if (currentScrollPosition > lastScrollPosition && currentScrollPosition > 0) {
    modalButton.classList.add('opacity-0', 'pointer-events-none'); // Hide button smoothly
  } else if (currentScrollPosition < lastScrollPosition && !nearBottom) {
    modalButton.classList.remove('opacity-0', 'pointer-events-none'); // Show button smoothly
  }

  lastScrollPosition = currentScrollPosition;
});