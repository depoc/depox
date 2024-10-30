document.addEventListener('DOMContentLoaded', function() {
    var phoneField = document.querySelector('input[name="celular"]');
    
    // Format CNPJ field on page load (if it already has a value)
    if (phoneField.value) {
        phoneField.value = formatCNPJ(phoneField.value);
    }

    // Optional: Add formatting while typing
    phoneField.addEventListener('input', function() {
        phoneField.value = formatPhone(phoneField.value);
    });

    function formatPhone(phone) {
        // Remove all non-digit characters
        phone = phone.replace(/\D/g, '');
        // Format as 00.000.000/0000-00
        return phone.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
    }
});