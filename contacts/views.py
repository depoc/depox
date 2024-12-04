from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .services import ContactsLogic


@login_required(login_url='users:login')
def contacts(request):
    context = {}
    context.update(ContactsLogic.get_context(request))

    return render(request, 'contacts/main.html', context)

@login_required(login_url='users:login')
def edit_contact(request, pk):
    context = ContactsLogic.edit_contact(request, pk)

    return render(request, 'contacts/common/_edit_contact.html', context)