document.addEventListener('keydown', function(event) {
    if (event.target.tagName === 'INPUT' || 
        event.target.tagName === 'TEXTAREA' || 
        event.target.tagName === 'SELECT' || 
        event.target.isContentEditable) {
        return;
    }
    
    if (event.key.toLowerCase() === 'f') {
        window.location.href = '/caixa/?data=todos';
    }

    if (event.key.toLowerCase() === 'c') {
        window.location.href = '/contatos/?filtro=todos';
    }

    if (event.key.toLowerCase() === 'h') {
        window.location.href = '/erp';
    }    
});