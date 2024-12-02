const dadosGeraisButton = document.getElementById('dados-gerais-button');
const enderecoBackButton = document.getElementById('endereco-back-button')

const sectionDadosGerais = document.getElementById('dados-gerais');
const sectionEndereco = document.getElementById('contact-endereco');

dadosGeraisButton.addEventListener('click', () => {
    sectionDadosGerais.classList.add('hidden');
    sectionEndereco.classList.remove('hidden');
});

enderecoBackButton.addEventListener('click', () => {
    sectionEndereco.classList.add('hidden');
    sectionDadosGerais.classList.remove('hidden');
});