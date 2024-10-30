document.addEventListener('keydown', function(event) {
    if (event.target.tagName === 'INPUT' || 
        event.target.tagName === 'TEXTAREA' || 
        event.target.isContentEditable) {
        return;
    }
    
    if (event.key.toLowerCase() === 'f') {
        window.location.href = '/caixa';
    }
});

document.addEventListener('keydown', function(event) {
    if (event.target.tagName === 'INPUT' || 
        event.target.tagName === 'TEXTAREA' || 
        event.target.isContentEditable) {
        return;
    }

    if (event.key.toLowerCase() === 'i') {
        window.location.href = '/erp';
    }
});