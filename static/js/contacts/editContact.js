const buttons = document.querySelectorAll('.contact-info-button');
const contactInfo = document.getElementById('contact-info');
const closeContactInfo = document.getElementById('close-contact-info');

let targetUrl = '';

buttons.forEach(button => {
    button.addEventListener("click", (event) => {
        event.preventDefault();
        targetUrl = button.getAttribute('href');
        contactInfo.classList.remove('hidden');
        contactInfo.classList.add('flex');
    });
});

closeContactInfo.addEventListener("click", () => {
    contactInfo.classList.remove("flex");
    contactInfo.classList.add("hidden");
});

contactInfo.addEventListener("click", (e) => {
    if (e.target === contactInfo) {
        contactInfo.classList.add("hidden");
    }
});