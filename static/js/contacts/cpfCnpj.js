document.addEventListener('DOMContentLoaded', () => {
    const pfRadio = document.getElementById('pf');
    const pfForm = document.getElementById('pf-form');
    const pjRadio = document.getElementById('pj');
    const nomeLabel = document.getElementById('nome-label');
    const apelidoLabel = document.getElementById('apelido-label');
    const cpfCnpjLabel = document.getElementById('cpf-cnpj-label');
    const checkbox = document.getElementById('contribuinte-checkbox');

    const toggleForms = () => {
      if (pfRadio.checked) {
        nomeLabel.textContent = 'nome';
        apelidoLabel.textContent = 'apelido';
        cpfCnpjLabel.textContent = 'cpf';
        checkbox.classList.add('hidden');
        pfForm.classList.add('mb-24');
      } else if (pjRadio.checked) {
        nomeLabel.textContent = 'razão social';
        apelidoLabel.textContent = 'fantasia';
        cpfCnpjLabel.textContent = 'cnpj';
        checkbox.classList.remove('hidden');
        pfForm.classList.remove('mb-24');
      }
    };

    // Initial toggle
    toggleForms();

    // Listen for changes
    pfRadio.addEventListener('change', toggleForms);
    pjRadio.addEventListener('change', toggleForms);
});