const history = document.getElementById('history');
const closeHistory = document.getElementById('closeHistory');

function historyButton() {
  history.classList.remove('hidden');
  history.classList.add('flex')
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