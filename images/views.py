from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image, Profile, Like
from .email import send_welcome_email
# Create your views here.

def post (request):
    image = Image.save_Image()
    return render(request,'post.html',{'image':image})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})


def search_results(request):
    if 'image' in request.GET and request.GET['image']:
        search_term = request.GET.get('image')
        print(search_term)
        searched_photos = Image.search_by_title(search_term)
        print(searched_photos)
        message = f'{search_term}'
        params = {
            'searched_photos': searched_photos,
            'message': message,
        }

        return render(request, 'all-photos/search.html',params)

    else:
        
        message = "You haven't searched for any image"
        return render(request, 'all-photos/search.html',{"message":message})
