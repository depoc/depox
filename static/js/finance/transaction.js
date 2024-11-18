const transaction = document.getElementById('transaction');
const transactionButton = document.getElementById('transactionButton');
const saidaButton = document.getElementById('saidaButton');
const closeTransaction = document.getElementById('closeTransaction');

const tipo = document.getElementById('tipo');

transactionButton.addEventListener('click', () => {
    transaction.classList.remove('hidden');
    transaction.classList.add('flex');
    tipo.value = 'entrada'
})

saidaButton.addEventListener('click', () => {
  transaction.classList.remove('hidden');
  transaction.classList.add('flex');
  tipo.value = 'saida'
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