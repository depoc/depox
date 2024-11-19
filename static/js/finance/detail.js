const history = document.getElementById('history');
const closeHistory = document.getElementById('closeHistory');

function historyButton(row) {
  history.classList.remove('hidden');
  history.classList.add('flex')

  // Access data attributes
  const id = row.getAttribute('data-id');
  const conta = row.getAttribute('data-conta');
  let tipo = row.getAttribute('data-tipo');
  const valor = row.getAttribute('data-valor');
  const contato = row.getAttribute('data-contato');
  const descricao = row.getAttribute('data-descricao');
  const categoria = row.getAttribute('data-categoria');
  const created = row.getAttribute('data-created');

  if (tipo === "receber") {
    tipo = "recebimento";
  } else if (tipo === "pagar") {
    tipo = "pagamento"
  } else {
    tipo = "transferência"
  }

  // Populate modal fields
  document.getElementById('modal-id').textContent = id;
  document.getElementById('modal-conta').textContent = conta;
  document.getElementById('modal-tipo').textContent = tipo;
  document.getElementById('modal-valor').textContent = valor;
  document.getElementById('modal-contato').textContent = contato;
  document.getElementById('modal-descricao').textContent = descricao;
  document.getElementById('modal-categoria').textContent = categoria;  
  document.getElementById('modal-created').textContent = created;  

  // Update form action dynamically
  const form = document.getElementById('delete-transaction-form');
  const actionUrl = "lancamento/0/excluir/".replace('0', id);
  form.setAttribute('action', actionUrl);
  }

closeHistory.addEventListener('click', () => {
  history.classList.add('hidden')
})

history.addEventListener('click', (event) => {
  if (event.target === history) {
    history.classList.add('hidden');
  }
});

document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape') { 
    if (history.classList.contains('flex')) {
      history.classList.remove('flex');
      history.classList.add('hidden');
    }
  }
});