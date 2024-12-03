from .models import Contacts
from .forms import ContactsForm

from finance.models import Transactions


class ContactsLogic:
    @staticmethod
    def get_context(request) -> dict[str, object]:
        context = {}
        context.update(ContactsLogic.get_contacts(request))
        context.update(ContactsLogic.add_contact(request))

        return context
    
    @staticmethod
    def get_contacts(request) -> dict[str, object]:
        contacts = Contacts.objects.all().order_by('apelido')

        recent_contacts = Contacts.objects.all().order_by('-created')[0:2]

        return {'contacts': contacts, 'recent_contacts': recent_contacts}
    
    @staticmethod
    def add_contact(request) -> dict[str, object]:
        form = ContactsForm()
        post_data = request.POST.copy()
        company = request.user.company
        post_data['company'] = company

        if request.method == 'POST' and 'add-contact' in request.POST:
            form = ContactsForm(post_data)
            if form.is_valid():
                form.save()

        return {'addContactForm': form}
    