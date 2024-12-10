from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .services import ContactsLogic

from .models import Contacts


@login_required(login_url='users:login')
def contacts(request):
    context = {}
    context.update(ContactsLogic.get_context(request))

    return render(request, 'contacts/main.html', context)

@login_required(login_url='users:login')
def edit_contact(request, pk):
    context = ContactsLogic.edit_contact(request, pk)

    return render(request, 'contacts/common/_edit_contact.html', context)

@login_required(login_url='users:login')
def delete_contact(request, pk):
    contact = Contacts.objects.get(pk=pk)
    contact.delete()
    
    return redirect('contacts:main')