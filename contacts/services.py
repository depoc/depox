from .models import Contacts
from finance.models import Transactions


class ContactsLogic:
    @staticmethod
    def get_context(request) -> dict[str, object]:
        context = {}
        context.update(ContactsLogic.get_contacts(request))

        return context
    
    @staticmethod
    def get_contacts(request) -> dict[str, object]:
        contacts = Contacts.objects.all().order_by('nome')

        return {'contacts': contacts}