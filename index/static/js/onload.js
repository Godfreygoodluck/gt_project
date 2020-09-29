from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.http import JsonResponse

from contact.models import contact
from weddings.models import weddings_project
from portrait.models import portrait_project
from blog.models import blog_post, Comment, Category
from blog.forms import CommentForm
from brand.models import brand_project
from about.models import about_company, about_photographer
from index.models import our_Services, our_Surport, testimonials


# Create your views here.
 



def index(request):

    #Ajax..................................................................................
    limit = request.GET.get('limit')
    start = request.GET.get('start')
    
    
    #blog_post..................................................................................
    blog = blog_post.objects.all().order_by('-created_on')

    page = request.GET.get('page', 1)
    paginator = Paginator(blog, 12)

    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(1)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)


    #blog_details 
    


    #gallery

    #weddings..................................................................................

    weddings = weddings_project.objects.all().order_by('-created_on')
    
    results_per_page = 12
    paginator = Paginator(weddings, results_per_page)

    try:
        weddings = paginator.page(page)
    except PageNotAnInteger:
        weddings = paginator.page(2)
    except EmptyPage:
        weddings = paginator.page(paginator.num_pages)



    #portriat..................................................................................

    portrait = portrait_project.objects.all().order_by('-created_on')
    
    results_per_page = 12
    paginator = Paginator(portrait, results_per_page)

    try:
        portrait = paginator.page(page)
    except PageNotAnInteger:
        portrait = paginator.page(2)
    except EmptyPage:
        portrait = paginator.page(paginator.num_pages)
    


    #brand..................................................................................
    brand = brand_project.objects.all().order_by('-created_on')
    
    results_per_page = 12
    paginator = Paginator(brand, results_per_page)

    try:
        brand = paginator.page(page)
    except PageNotAnInteger:
        brand = paginator.page(2)
    except EmptyPage:
        brand = paginator.page(paginator.num_pages)
    


    #about..................................................................................
    About_Company = about_company.objects.all()
    About_Photographer = about_photographer.objects.all()


    #contact..................................................................................
    contacts = contact.objects.all()

    #services..................................................................................
    services = our_Services.objects.all()
    surport = our_Surport.objects.all()
    testimonial = testimonials.objects.all()
    
    context = {
        'services' : services,
        'surport' : surport,
        'testimonial' : testimonial,
        'blog': blog,
        'brand': brand,
        'weddings': weddings,
        'portrait': portrait,
        'contacts' : contacts,
        'About_Company' : About_Company,
        'About_Photographer' : About_Photographer,
        
    }

    return render(request, 'index.html', context=context)
#..................................................................................
#..................................................................................



#weddings..................................................................................
def weddings_index(request):
    page = request.POST.get('page')
    weddings = weddings_project.objects.all().order_by('-created_on')
    
    results_per_page = 12
    paginator = Paginator(weddings, results_per_page)

    try:
        weddings = paginator.page(page)
    except PageNotAnInteger:
        weddings = paginator.page(2)
    except EmptyPage:
        weddings = paginator.page(paginator.num_pages)
    
    weddings_posts_html = loader.render_to_string(
        'weddings.html',
        {'weddings': weddings}
    )

    weddings_output_data = {
        'weddings_posts_html': weddings_posts_html,
        'has_next': weddings.has_next()
    }
    return JsonResponse(weddings_output_data)

#portrait..................................................................................
def portrait_index(request):
    page = request.POST.get('page')
    portrait = portrait_project.objects.all().order_by('-created_on')
    
    results_per_page = 12
    paginator = Paginator(portrait, results_per_page)

    try:
        portrait = paginator.page(page)
    except PageNotAnInteger:
        portrait = paginator.page(2)
    except EmptyPage:
        portrait = paginator.page(paginator.num_pages)
    
    portrait_posts_html = loader.render_to_string(
        'portrait.html',
        {'portrait': portrait}
    )

    portrait_output_data = {
        'portrait_posts_html': portrait_posts_html,
        'has_next': portrait.has_next()
    }
    
    return JsonResponse(console.log(portrait_output_data))   

#brand..................................................................................
def brand_index(request):
    page = request.POST.get('page')
    brand = brand_project.objects.all().order_by('-created_on')
    
    results_per_page = 12
    paginator = Paginator(brand, results_per_page)

    try:
        brand = paginator.page(page)
    except PageNotAnInteger:
        brand = paginator.page(2)
    except EmptyPage:
        brand = paginator.page(paginator.num_pages)
    
    brand_posts_html = loader.render_to_string(
        'brand.html',
        {'brand': brand}
    )

    brand_output_data = {
        'brand_posts_html': brand_posts_html,
        'has_next': brand.has_next()
    }
    return JsonResponse(brand_output_data) 


#blog_index..................................................................................
def blog_index(request):
    page = request.POST.get('page')
    blog = blog_post.objects.all().order_by('-created_on')
    
    results_per_page = 12
    paginator = Paginator(blog, results_per_page)

    try:
        blog = paginator.page(page)
    except PageNotAnInteger:
        blog = paginator.page(2)
    except EmptyPage:
        blog = paginator.page(paginator.num_pages)
    
    blog_posts_html = loader.render_to_string(
        'blog.html',
        {'blog': blog}
    )

    blog_output_data = {
        'blog_posts_html': blog_posts_html,
        'has_next': blog.has_next()
    }
    return JsonResponse(blog_output_data)


#blog_detail..................................................................................
def blog_detail(request, pk):
    post = blog_post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)

    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 4)

    try:
        comment_numbers = paginator.page(page)
    except PageNotAnInteger:
        comment_numbers = paginator.page(1)
    except EmptyPage:
        comment_numbers = paginator.page(paginator.num_pages)


    context = {
        "post": post,
        "comment_numbers": comment_numbers,
        "form": form,
    }
    return render(request, "blog_detail.html", context)


#blog_category..................................................................................
def blog_category(request, category):
    posts = blog_post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        'posts' : posts
    }
    
    return render(request, 'blog_category.html', context=context)