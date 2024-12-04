document.addEventListener('DOMContentLoaded', function() {
    var phoneField = document.querySelector('input[name="celular"]');
    
    if (phoneField.value) {
        phoneField.value = formatPhone(phoneField.value);
    }

    // Optional: Add formatting while typing
    phoneField.addEventListener('input', function() {
        phoneField.value = formatPhone(phoneField.value);
    });

    function formatPhone(phone) {
        phone = phone.replace(/\D/g, ''); // Remove non-digit characters
        phone = phone.substring(0, 11);  // Limit to a maximum of 11 digits
        return phone.replace(/(\d{2})(\d{5})(\d{4})/, '$1 $2-$3');
    }
});
