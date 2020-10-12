from django.shortcuts import render, redirect

# Create your views here.

def post (request):
    photos = cls.objects.filter()
    return render(request,'posts.html',{{'photos':photos}})