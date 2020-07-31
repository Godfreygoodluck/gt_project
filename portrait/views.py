from django.shortcuts import render
from portrait.models import portrait_project
import os


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from contact.models import contact
from about.models import about_company, about_photographer

# Create your views here.
 

def portrait_index(request):

    portrait = portrait_project.objects.all()
    
    page = request.GET.get('page', 1)
    paginator = Paginator(portrait, 12)

    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    
    
    return render(request, 'portrait_index.html', {'numbers': numbers})


def portrait_contact(request):
    contacts = contact.objects.all()
    context = {
        'contacts' : contacts
    }
    return render(request, 'portrait_index.html', context=context)

def aboutCompany_index(request):
    About_Company = about_company.objects.all()
    context = {
        'About_Company' : About_Company
    }
    return render(request, 'portrait_index.html', context=context)

def aboutPhotographer_index(request):
    
    About_Photographer = about_photographer.objects.all()
    context = {
    
        'About_Photographer' : About_Photographer
    }
    print(About_Photographer)
    return render(request, 'portrait_index.html', context=context)