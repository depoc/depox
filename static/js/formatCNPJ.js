document.addEventListener('DOMContentLoaded', function() {
    var cnpjField = document.querySelector('input[name="cnpj"]');
    
    // Format CNPJ field on page load (if it already has a value)
    if (cnpjField.value) {
        cnpjField.value = formatCNPJ(cnpjField.value);
    }

    // Optional: Add formatting while typing
    cnpjField.addEventListener('input', function() {
        cnpjField.value = formatCNPJ(cnpjField.value);
    });

    function formatCNPJ(cnpj) {
        // Remove all non-digit characters
        cnpj = cnpj.replace(/\D/g, '');
        // Format as 00.000.000/0000-00
        return cnpj.replace(/(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})/, '$1.$2.$3/$4-$5');
    }
});