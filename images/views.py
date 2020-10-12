from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image, Profile, Like

# Create your views here.

def post (request):
    photos = Image.save_()
    return render(request,'posts.html',{{'photos':photos}})

def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})


# def search_results(request):
#     user_name = self.request.GET.get('search', '')
#     print(user_name)
#     message = f'{search_term}'
#     params = {
#         'user_name' = user_name,
#         'message': message,
#         }

#         return render(request, 'all-photos/search.html',params)

#     else:
        
#         message = "You haven't searched for any User"
#         return render(request, 'all-photos/search.html',{"message":message})
