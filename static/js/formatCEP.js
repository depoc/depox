document.addEventListener('DOMContentLoaded', function() {
    var cepField = document.querySelector('input[name="cep"]');
    
    // Format cep field on page load (if it already has a value)
    if (cepField.value) {
        cepField.value = formatCep(cepField.value);
    }

    // Optional: Add formatting while typing
    cepField.addEventListener('input', function() {
        cepField.value = formatCep(cepField.value);
    });

    function formatCep(cep) {
        // Remove all non-digit characters
        cep = cep.replace(/\D/g, '');
        // Format as 00000-000
        return cep.replace(/(\d{5})(\d{3})/, '$1-$2');
    }
});