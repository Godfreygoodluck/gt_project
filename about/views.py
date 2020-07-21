from django.shortcuts import render
from about.models import about_company, about_photographer

# Create your views here.



def company_index(request):
    About_Company = about_company.objects.all()
    context = {
        'About_Company' : About_Company
    }
    return render(request, 'about_index.html', context=context)

def photographer_index(request):
    
    About_Photographer = about_photographer.objects.all()
    context = {
	
        'About_Photographer' : About_Photographer
    }
    print(About_Photographer)
    return render(request, 'about_index.html', context=context)
	
