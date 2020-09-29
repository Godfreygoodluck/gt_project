from django.shortcuts import render
from about.models import about_company, about_photographer

from contact.models import contact
# Create your views here.



def company_index(request):
    About_Company = about_company.objects.all()
    About_Photographer = about_photographer.objects.all()
    contacts = contact.objects.all()
    context = {
        'About_Company' : About_Company,
        'contacts' : contacts,
        'About_Photographer' : About_Photographer
    }
    return render(request, 'about_index.html', context=context)


	
