from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import Blogspostform
from .models import Blogpost

# Create your views here.

def Home(request):
    posts = Blogpost.objects.all()
    return render (request,'home.html' , {'posts':posts})

@login_required
def mypost_create(request):
    if request.method == 'POST':
        form = Blogspostform(request.POST)
        if form.is_valid():
            form.instance.author = request.user 
            form.save()
            return redirect ('myposts-page')
    else:
        form = Blogspostform()
    return render (request,'createpost.html' , {'form':form})

@login_required
def myposts(request):
    author = request.user
    posts = Blogpost.objects.filter(author=author)
    return render (request,'myposts.html',{'posts':posts})

def mypost_read(request,pk):
    post = Blogpost.objects.get(pk=pk)
    return render(request,'readpost.html',{'post':post})

@login_required
def myposts_delete(request,pk):
    post = Blogpost.objects.get(pk=pk)
    post.delete()
    return redirect('myposts-page')

@login_required
def myposts_update(request,pk):
    post = Blogpost.objects.get(pk=pk)
    if request.method == 'POST':
        form = Blogspostform(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('mypost-page')
    else:
        form = Blogspostform(instance=post)
    return render (request,'updatepost.html',{'form':form})        

