from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.http import HttpResponseRedirect, JsonResponse
from .models import *
from django.contrib import messages
from . forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout


# @login_required(login_url='/accounts/login/')
def index(request):
    hoods = Hood.objects.all()
    return render(request, 'hoods/index.html',{"hoods":hoods})
    
def signup(request):
    global register_form
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
        register_form = {
            'form': form,
        }
    return render(request, 'django_registration/registration_form.html', {'form': form})


@login_required(login_url='/accounts/login/')
def upload_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            hood.owner= current_user
            upload.save()
            return redirect('index')
    else:
        form = HoodForm()
    return render(request, 'hoods/upload_hood.html', locals())


@login_required(login_url='/accounts/login/')
def hood(request,hood_id):
    current_user = request.user
    hood_name = current_user.profile.hood
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    businesses = Business.get_business(hood_id)
    posts = Post.get_post(hood_id)

    return render(request,'hoods/hood.html',{"hood_name":hood_name,"hood":hood,"businesses":businesses,"posts":posts})


@login_required(login_url='/accounts/login')
def join(request,hood_id):
    hood = Hood.objects.get(id=hood_id)
    current_user = request.user
    current_user.profile.hood = hood
    current_user.profile.save()
    return redirect('hood',hood_id)


@login_required(login_url='/accounts/login')
def leave(request,hood_id):
    current_user = request.user
    current_user.profile.hood = None
    current_user.profile.save()
    return redirect('index')


def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        searched_business = Business.search_business(search_term)
        message = f"{search_term}"

        return render(request, 'hoods/search_business.html',locals())

    else:
        message = "You haven't searched for any term"
        return render(request,'hoods/search.html',{"message":message})    
    
# Views for profile
@login_required(login_url='/accounts/login/')
def profile(request, username):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,

    }
    return render(request, 'profile/profile.html', params)



@login_required(login_url='/accounts/login/')
def edit(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,

    }
    return render(request, 'profile/edit_profile.html', params)


# business views
@login_required(login_url='/accounts/login')
def upload_business(request):
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    if request.method == 'POST':
        businessform = BusinessForm(request.POST, request.FILES)
        if businessform.is_valid():
            upload = businessform.save(commit=False)
            upload.user=request.user
            upload.hood=request.user.profile.hood
            upload.save()
        return redirect('hood',request.user.profile.hood.id)
    else:
        businessform = BusinessForm()
    return render(request,'hoods/business.html',locals())  


# Post view
@login_required(login_url='/accounts/login')
def add_post(request):
    hood = Hood.objects.get(id=request.user.profile.hood.id)
    if request.method == 'POST':
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post = postform.save(commit=False)
            post.profile = request.user.profile
            post.user = request.user
            post.hood=request.user.profile.hood
            post.save()
            return redirect('hood',request.user.profile.hood.id)
    else:
        postform = PostForm()
    return render(request,'hoods/upload_post.html',locals())