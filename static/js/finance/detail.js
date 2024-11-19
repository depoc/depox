const history = document.getElementById('history');
const closeHistory = document.getElementById('closeHistory');

function historyButton(row) {
  history.classList.remove('hidden');
  history.classList.add('flex')

  // Access data attributes
  const conta = row.getAttribute('data-conta');
  const tipo = row.getAttribute('data-tipo');
  const valor = row.getAttribute('data-valor');
  const contato = row.getAttribute('data-contato');
  const descricao = row.getAttribute('data-descricao');
  const categoria = row.getAttribute('data-categoria');
  const created = row.getAttribute('data-created');

  // Populate modal fields
  document.getElementById('modal-conta').textContent = conta;
  document.getElementById('modal-tipo').textContent = tipo;
  document.getElementById('modal-valor').textContent = valor;
  document.getElementById('modal-contato').textContent = contato;
  document.getElementById('modal-descricao').textContent = descricao;
  document.getElementById('modal-categoria').textContent = categoria;  
  document.getElementById('modal-created').textContent = created;  
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