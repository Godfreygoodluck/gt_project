from django.shortcuts import render


from contact.models import contact
# Create your views here.

def nav(request):
    contacts = contact.objects.all()
    context = {
        'contacts' : contacts,
    }
    return render(request,'nav.html',context)