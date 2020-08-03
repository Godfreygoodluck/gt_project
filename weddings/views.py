from django.shortcuts import render
from weddings.models import weddings_project
import os


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from contact.models import contact


# Create your views here.



def weddings_index(request):

    weddings = weddings_project.objects.all()
    contacts = contact.objects.all()

    page = request.GET.get('page', 1)
    paginator = Paginator(weddings, 12)

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
    
    return render(request, 'weddings_index.html', context=context)
