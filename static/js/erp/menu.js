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
  const bottomOffset = 50; // Adjust this value if needed

  // Calculate if near bottom
  const nearBottom = (window.innerHeight + window.scrollY) >= (document.body.offsetHeight - bottomOffset);

  if (currentScrollPosition > lastScrollPosition && currentScrollPosition > 0) {
    // Scrolling down, hide button
    modalButton.classList.add('hidden');
  } else if (currentScrollPosition < lastScrollPosition && !nearBottom) {
    // Scrolling up and not near the bottom, show button
    modalButton.classList.remove('hidden');
  }

  // Update last scroll position
  lastScrollPosition = currentScrollPosition;
});