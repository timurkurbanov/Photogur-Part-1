from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from photogur.models import Picture, Comment
from django.views.decorators.http import require_http_methods

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

def picture_search(request):
	query = request.GET['query']
	search_results = Picture.objects.filter(artist=query)
	context = {'pictures': search_results, 'query': query}
	response = render(request, 'search_results.html', context)
	return HttpResponse(response)

@require_http_methods(['POST'])
def create_comment(request):
	upicture = Picture.objects.GET(id=picture_id)
	name = request.POST['name']
	message = request.POST['message']
	picture = request.POST['picture']
	Comment.objects.create(name=name, picture=picture, message=message)
	return redirect('picture_show', id=picture_id)


# https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/#example
# def picture_show(request, id):
#     picture = Picture.objects.get(pk=id)
#     context = {'picture_details': picture}
#     response = render(request, 'picture.html', context)
#     return HttpResponse(response)