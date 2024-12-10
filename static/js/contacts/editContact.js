const editContactButton = document.getElementById("editContactButton");
const editContact = document.getElementById("editContact");
const closeEditContact = document.getElementById("closeEditContact");

editContactButton.addEventListener("click", () => {
    editContact.classList.remove("hidden");
    editContact.classList.add("flex");
})

closeEditContact.addEventListener("click", () => {
    editContact.classList.remove("flex");
    editContact.classList.add("hidden");
})

editContact.addEventListener("click", (e) => {
    if (e.target === editContact) {
        editContact.classList.add("hidden");
    }
})

document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') { 
      if (editContact.classList.contains('flex')) {
        editContact.classList.remove('flex');
        editContact.classList.add('hidden');
      }
    }
});