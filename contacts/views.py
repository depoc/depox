from django.shortcuts import render

from .services import ContactsLogic


def contacts(request):
    context = {}
    context.update(ContactsLogic.get_contacts(request))

    return render(request, 'contacts/main.html', context)
