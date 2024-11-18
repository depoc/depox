const transaction = document.getElementById('transaction');
const transactionButton = document.getElementById('transactionButton');
const saidaButton = document.getElementById('saidaButton');
const transferirButton = document.getElementById('transferirButton');
const closeTransaction = document.getElementById('closeTransaction');

const tipo = document.getElementById('tipo');

transactionButton.addEventListener('click', () => {
    transaction.classList.remove('hidden');
    transaction.classList.add('flex');
    tipo.value = 'receber'
})

saidaButton.addEventListener('click', () => {
  transaction.classList.remove('hidden');
  transaction.classList.add('flex');
  tipo.value = 'pagar'
})

transferirButton.addEventListener('click', () => {
  transaction.classList.remove('hidden');
  transaction.classList.add('flex');
  tipo.value = 'transferir'
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