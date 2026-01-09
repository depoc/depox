const addContactButton = document.getElementById("addContactButton");
const addContact = document.getElementById("addContact");
const closeAddContact = document.getElementById("closeAddContact");

addContactButton.addEventListener("click", () => {
    addContact.classList.remove("hidden");
    addContact.classList.add("flex");
})

closeAddContact.addEventListener("click", () => {
    addContact.classList.remove("flex");
    addContact.classList.add("hidden");
})

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { 
      if (addContact.classList.contains('flex')) {
        addContact.classList.remove('flex');
        addContact.classList.add('hidden');
      }
    }
});