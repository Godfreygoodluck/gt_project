from django.shortcuts import render
from blog.models import Post, Comment
from blog.forms import CommentForm
import os


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')

    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 12)

    try:
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'blog_index.html', {'numbers': numbers})



def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        'posts' : posts
    }
    
    return render(request, 'blog_category.html', context=context)




def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

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
        numbers = paginator.page(page)
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)


    context = {
        "post": post,
        "numbers": numbers,
        "form": form,
    }
    return render(request, "blog_detail.html", context)












    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 12)

    try:
        number = paginator.page(page)
    except PageNotAnInteger:
        number = paginator.page(1)
    except EmptyPage:
        number = paginator.page(paginator.num_pages)