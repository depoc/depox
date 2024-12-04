from django.shortcuts import get_object_or_404

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

        cpf_cnpj: str | None
        if cpf_cnpj := post_data.get('cpf_cnpj'):
            cpf_cnpj_cleaned = cpf_cnpj.replace('.', '') \
                                       .replace('-', '') \
                                       .replace('/', '')
            post_data['cpf_cnpj'] = cpf_cnpj_cleaned

        cep: str | None
        if cep := post_data.get('cep'):
            cep_cleaned = cep.replace('-', '')
            post_data['cep'] = cep_cleaned

        celular: str | None
        if celular := post_data.get('celular'):
            celular_cleaned = celular.replace(' ', '') \
                                     .replace('-', '')
            post_data['celular'] = celular_cleaned

        if request.method == 'POST' and 'add-contact' in request.POST:
            form = ContactsForm(post_data)
            if form.is_valid():
                form.save()

        return {'addContactForm': form}
    
    @staticmethod
    def edit_contact(request, pk) -> dict[str, object]:
        contact = get_object_or_404(Contacts, pk=pk)

        return {'contact': contact}