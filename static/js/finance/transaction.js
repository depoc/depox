const transaction = document.getElementById('transaction');
const transactionButton = document.getElementById('transactionButton');
const closeTransaction = document.getElementById('closeTransaction');

transactionButton.addEventListener('click', () => {
    transaction.classList.remove('hidden');
    transaction.classList.add('flex')
})

closeTransaction.addEventListener('click', () => {
  transaction.classList.add('hidden')
})

transaction.addEventListener('click', (event) => {
  if (event.target === transaction) {
    transaction.classList.add('hidden');
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') { 
    if (transaction.classList.contains('flex')) {
      transaction.classList.remove('flex');
      transaction.classList.add('hidden');
    }
  }
});