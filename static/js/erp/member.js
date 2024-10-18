document.getElementById('toggle-membro-button').addEventListener('click', function() {
    // Toggle visibility of the member and CNPJ forms
    const memberForm = document.getElementById('membro-form');
    memberForm.classList.toggle('hidden');

    const equipeList = document.getElementById('equipe-list');
    equipeList.classList.toggle('hidden');
  
    const areaMemberButton = document.getElementById('div-membro-button');
    areaMemberButton.classList.toggle('mt-8');
    areaMemberButton.classList.toggle('border-black/30');
    areaMemberButton.classList.toggle('dark:border-white/60');

});