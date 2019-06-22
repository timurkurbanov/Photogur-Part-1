from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from photogur.models import Picture, Comment
from photogur.forms import LoginForm, PictureForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def root(request):
    return HttpResponseRedirect('/pictures/')

def pictures_page(request):
    context = {'pics': Picture.objects.all()}
    html_string = render(request, 'pictures.html', context)
    return HttpResponse(html_string)

def picture_show(request, id):
    picture = Picture.objects.get(pk=id)
    context = {'picture': picture}
    html_string = render(request, 'picture.html', context)
    return HttpResponse(html_string)

@login_required
def add_picture(request):
    if request.method == "POST":
        form = PictureForm(request.POST)
        if form.is_valid():
            new_picture = form.instance
            new_picture.user = request.user
            new_picture.save()
            return HttpResponseRedirect('/')
    else:
        form = PictureForm()
    html_response = render(request, 'new_picture.html', {'form': form})
    return HttpResponse(html_response)

@login_required
def edit_picture(request, id):
    picture = get_object_or_404(Picture, pk=id, user=request.user.pk)
    if request.method == "POST":
        form = PictureForm(request.POST, instance=picture)
        if form.is_valid():
            updated_picture = form.save()
            return HttpResponseRedirect(reverse('picture_details', args=[picture.id]))
    else:
        form = PictureForm(instance=picture)
    context = {'form': form, 'picture': picture}
    html_response = render(request, 'edit_picture.html', context)
    return HttpResponse(html_response)

    context = {'picture': picture}
    html_response = render(request, "edit_picture.html", context)
    return HttpResponse(html_response)

def user_pictures(request):
    context = {'pics': request.user.pictures.all()}
    html_string = render(request, 'pictures.html', context)
    return HttpResponse(html_string)

def picture_search(request):
    # request.GET is a dictionary where keys are form filed names (that we assigned) and values are data entered by the user
    query = request.GET['query']
    search_results = Picture.objects.filter(artist=query)
    context = {'pictures': search_results, 'query': query}
    html_string = render(request, 'search.html', context)
    return HttpResponse(html_string)

def create_comment(request):
    post_dict = request.POST
    picture = Picture.objects.get(pk=post_dict['picture'])
    name = post_dict['comment-name']
    message = post_dict['comment-message']
    new_comment = Comment.objects.create(name=name, message=message, picture=picture)
    path = '/pictures/' + str(picture.pk)
    return HttpResponseRedirect(path)

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate(username=username, password=pw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                form.add_error('username', 'Login failed')
    else:
        form = LoginForm()

    context = {'form': form}
    html_response = render(request, 'login.html', context)
    return HttpResponse(html_response)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    html_response = render(request, 'signup.html', {'form': form})
    return HttpResponse(html_response)
