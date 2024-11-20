const transfer = document.getElementById('transfer');
const transferirButton = document.getElementById('transferirButton');
const closeTransfer = document.getElementById('closeTransfer');

transferirButton.addEventListener('click', () => {
  transfer.classList.remove('hidden');
  transfer.classList.add('flex');
})

closeTransfer.addEventListener('click', () => {
  transfer.classList.add('hidden')
})

transfer.addEventListener('click', (event) => {
  if (event.target === transfer) {
    transfer.classList.add('hidden');
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') { 
    if (transfer.classList.contains('flex')) {
      transfer.classList.remove('flex');
      transfer.classList.add('hidden');
    }
  }
});