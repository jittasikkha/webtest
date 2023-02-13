from re import search, template
from unittest import result
from django.forms import models
from django.shortcuts import render , redirect , get_object_or_404
from django.template import context
from .models import *
from .forms import PostForm
from django.utils.text import slugify
from django.contrib import messages
from coverapp.models import Coverpic
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.db.models import Q


# Create your views here.

    


def index(request):

    search_query = request.GET.get('search','')

    if search_query:
        posts = Post.objects.filter(Q(title__icontains = search_query) | Q(intro__icontains = search_query) |  Q(slug__icontains = search_query))
    else:
        posts = Post.objects.filter(approved=True)

    categorys = Category.objects.all()
    page = request.GET.get('page')
    num_of_items = 6
    paginator = Paginator(posts,num_of_items)
    tags = Tags.objects.all()
    mostpost = Post.objects.filter(approved=True).order_by('-views')[0:8]

    
    

    def get_ip(request):
        adress = request.META.get('HTTP_X_FORWARDED_FOR')
        if adress:
            ip = adress.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    ip = get_ip(request)
    u = User(user=id)
    print(ip)
    result=User.objects.filter(Q(user__icontains=ip))

    if len(result) == 1 :
        print('user exist')
    elif len(result) > 1:
        print("user exist more.... ")
    else:
        u.save()
        print("user is unique")
    
    count = User.objects.all().count()
    print("total user is " , count)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    cover = Coverpic.objects.filter(approved=True)
    slides = Coverpic.objects.filter(slide=True)
    context = {'posts' : posts , 'cover' : cover , 'paginator' : paginator , 'categorys' : categorys , 'slides' : slides , 'tags': tags , 'count' : count , 'mostpost' : mostpost}
    return render(request, 'cmsapp/index.html',context)




def detail(request, slug):
    post = get_object_or_404(Post , slug=slug)
    post.views = post.views+1
    post.save()
    categorys = Category.objects.all()
    context = {'post' : post , 'categorys' : categorys}
    return render(request,'cmsapp/detail.html',context)

    

def createPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.save()
            return redirect('index')
    context = {'form' : form}
    return render(request,'cmsapp/create.html', context)

def updatePost(request,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES , instance=post)
        if form.is_valid():
            form.save()
            return redirect('detail', slug=post.slug)
    context = {'form': form}
    return render(request, 'cmsapp/create.html', context)

def deletePost(request,slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    if request.method == 'POST':
        post.delete()
        return redirect('index')
    context = {'form': form}
    return render(request, 'cmsapp/delete.html', context)

def category(request,slug):
    categorys = Category.objects.all()
    posts = Post.objects.all()
    category = Category.objects.get(slug=slug)
    context = {'category' : category , 'posts' : posts , 'categorys' : categorys}
    return render(request,'cmsapp/category.html',context)

def tag(request, slug):
    categorys = Category.objects.all()
    tag = Tags.objects.get(slug=slug)
    posts = Post.objects.all()
    context = {'tag' : tag , 'posts': posts , 'categorys' : categorys}
    return render(request,'cmsapp/tag.html',context)



