from django.shortcuts import render, HttpResponse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm,editPostedForm


# Create your views here.
def home(request):
    posts = Post.objects.order_by('-pub_date')
    paginator = Paginator(posts, 2) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blog_post.html", {'posts': posts})


def detail(request, id):
    posts = Post.objects.get(id=id)
    return render(request, "detail_post.html", {'posts': posts})


def add_post(request):
    forms = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        print form
        if form.is_valid():
            uncommit = form.save(commit=False)
            title= form.cleaned_data['title']
            description=form.cleaned_data['description']
            form.save()
            return redirect("home")
        else:
          print form.errors
    else:
        form = PostForm()
    return render(request, "add_post.html", {'forms': forms})

def edit_post(request,id):

    posts=Post.objects.get(id=id)
    forms = PostForm
    if request.method == 'POST':
        form = PostForm(request.POST, instance=posts)
        print form
        if form.is_valid():
            uncommit = form.save(commit=False)
            title= form.cleaned_data['title']
            description=form.cleaned_data['description']
            form.save()
            return redirect("home")
        else:
          print form.errors
    else:
        form = PostForm()
    return render(request, "edit_post.html", {'forms': forms,'posts':posts})

def delete_post(request,id):
    posts=Post.objects.get(id=id)
    if request.method == 'POST':
        posts.delete()
        return redirect("home")

def about(request):
    return render(request,'about.html',{})


