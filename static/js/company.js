document.getElementById('toggle-address-button').addEventListener('click', function() {
    // Toggle visibility of the address and CNPJ forms
    const addressForm = document.getElementById('address-form');
    addressForm.classList.toggle('hidden');

    const areaEmpresaButton = document.getElementById('div-empresa-button');
    areaEmpresaButton.classList.toggle('hidden');
    const areaContatoButton = document.getElementById('div-contato-button');
    areaContatoButton.classList.toggle('hidden');    

    const areaAdressButton = document.getElementById('div-address-button');
    areaAdressButton.classList.toggle('mt-8');
    areaAdressButton.classList.toggle('border-black/30');
    areaAdressButton.classList.toggle('dark:border-white/60');

    // Toggle visibility of the SVGs
    const toggleSvg = document.getElementById('toggle-svg');
    const hiddenSvg = document.getElementById('hidden-svg');
    
    toggleSvg.classList.toggle('hidden');
    hiddenSvg.classList.toggle('hidden');
});

document.getElementById('toggle-empresa-button').addEventListener('click', function() {
    // Toggle visibility of the address and CNPJ forms
    const addressForm = document.getElementById('empresa-form');
    addressForm.classList.toggle('hidden');

    const areaAdressButton = document.getElementById('div-address-button');
    areaAdressButton.classList.toggle('hidden');
    const areaContatoButton = document.getElementById('div-contato-button');
    areaContatoButton.classList.toggle('hidden');        

    const areaEmpresaButton = document.getElementById('div-empresa-button');
    areaEmpresaButton.classList.toggle('border-black/30');
    areaEmpresaButton.classList.toggle('dark:border-white/60');

    // Toggle visibility of the SVGs
    const toggleSvg = document.getElementById('empresa-toggle-svg');
    const hiddenSvg = document.getElementById('empresa-hidden-svg');
    
    toggleSvg.classList.toggle('hidden');
    hiddenSvg.classList.toggle('hidden');
});

document.getElementById('toggle-contato-button').addEventListener('click', function() {
    // Toggle visibility of the address and CNPJ forms
    const addressForm = document.getElementById('contato-form');
    addressForm.classList.toggle('hidden');

    const areaAdressButton = document.getElementById('div-address-button');
    areaAdressButton.classList.toggle('hidden');
    const areaEmpresaButton = document.getElementById('div-empresa-button');
    areaEmpresaButton.classList.toggle('hidden');   

    const areaContatoButton = document.getElementById('div-contato-button');
    areaContatoButton.classList.toggle('mt-8');
    areaContatoButton.classList.toggle('border-black/30');
    areaContatoButton.classList.toggle('dark:border-white/60');

    // Toggle visibility of the SVGs
    const toggleSvg = document.getElementById('contato-toggle-svg');
    const hiddenSvg = document.getElementById('contato-hidden-svg');
    
    toggleSvg.classList.toggle('hidden');
    hiddenSvg.classList.toggle('hidden');
});