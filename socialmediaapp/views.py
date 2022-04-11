from tkinter.messagebox import QUESTION
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render,redirect
from socialmediaapp.forms import *
from django.db.models import Q
from socialmediaapp.models import Post,Profile
from django.contrib.auth import authenticate,login,logout
# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('-id')
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(Q(author__username = query) | Q(title__contains = query) | Q(body__contains = query))
    return render(request,'post_list.html',{'posts':posts})


def post_detail(request,id,slug):
    post = Post.objects.get(id=id)
    return render(request,'post_detail.html',{'post':post})


def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
        else:
            return HttpResponse("Invalid Form")
    else:
        form = PostCreateForm()
        return render(request,'post_create.html',{'form':form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    return redirect('post_list')
                else:
                    return HttpResponse('User is not active')
            else:
                return HttpResponse('User is invalid')
    else:
        form = UserLoginForm()
        return render(request,'login.html',{'form':form})


def user_logout(request):
    logout(request)
    return redirect('post_list')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid:
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return redirect('post_list')
    else:
        form = UserRegistrationForm()
        return render(request,'register.html',{'form':form})


def edit_profile(request):
    if request.method == ' POST':
        user_form = UserEditForm(data=request.POST or None,instance=request.user)
        profile_form = ProfileEditForm(data=request.POST or None,instance=request.user.profile,files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user)
        return render(request,'edit_profile.html',{'user_form':user_form,'profile_form':profile_form})