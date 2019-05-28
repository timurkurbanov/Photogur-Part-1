from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment

def root(request):
    return HttpResponseRedirect('pictures')

def pictures_page(request):
    return render(request, 'pictures.html', {
        'pictures': Picture.objects.all()
        })

def picture_show(request, id):
    return render(request, 'picture.html', {
        'picture_details': Picture.objects.get(pk=id)
    })

# https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#example
# def picture_show(request, id):
#     picture = Picture.objects.get(pk=id)
#     context = {'picture_details': picture}
#     response = render(request, 'picture.html', context)
#     return HttpResponse(response)