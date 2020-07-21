from django.shortcuts import render
from contact.models import contact

import os
# Create your views here.
 

def contact_index(request):
    contacts = contact.objects.all()
    context = {
        'contacts' : contacts
    }
    return render(request, 'contact_index.html', context=context)

