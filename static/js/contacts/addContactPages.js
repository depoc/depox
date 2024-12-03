const dadosGeraisButton = document.getElementById('dados-gerais-button');
const enderecoBackButton = document.getElementById('endereco-back-button');
const enderecoNextButton = document.getElementById('endereco-next-button');
const dadosCompBackButton = document.getElementById('dados-comp-back-button')
const submitButtom = document.getElementById('submit-contact-form');

const sectionDadosGerais = document.getElementById('dados-gerais');
const sectionEndereco = document.getElementById('contact-endereco');
const sectionDadosComp = document.getElementById('dados-comp');

dadosGeraisButton.addEventListener('click', () => {
    submitButtom.classList.add('hidden');
    sectionDadosGerais.classList.add('hidden');
    sectionEndereco.classList.remove('hidden');
});

enderecoBackButton.addEventListener('click', () => {
    submitButtom.classList.add('hidden');
    sectionEndereco.classList.add('hidden');
    sectionDadosGerais.classList.remove('hidden');
});

enderecoNextButton.addEventListener('click', () => {
    sectionDadosGerais.classList.add('hidden');
    sectionEndereco.classList.add('hidden');
    sectionDadosComp.classList.remove('hidden');
    submitButtom.classList.remove('hidden');
});

dadosCompBackButton.addEventListener('click', () => {
    submitButtom.classList.add('hidden');
    sectionDadosGerais.classList.add('hidden');
    sectionDadosComp.classList.add('hidden');
    sectionEndereco.classList.remove('hidden');
});