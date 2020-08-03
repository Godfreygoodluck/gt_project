from django.shortcuts import render
from brand.models import brand_project
import os


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contact.models import contact


# Create your views here.



def brand_index(request):

    brand = brand_project.objects.all()
    contacts = contact.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(brand, 12)

    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    context = {
        'contacts' : contacts,
        'numbers': numbers,
    }
    
    return render(request, 'brand_index.html', context=context)
