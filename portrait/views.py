from django.shortcuts import render
from portrait.models import portrait_project
import os


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


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
