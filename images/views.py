from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image, Profile, Like,GeeksModel
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import LetterForm, ImageForm, GeeksForm,SignupForm,ProfileForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def profile (request):
    context = {} 
    context['form'] = GeeksForm() 
    if request.method == "POST": 
        form = GeeksForm(request.POST, request.FILES) 
        if form.is_valid(): 
            name = form.cleaned_data.get("name") 
            img = form.cleaned_data.get("geeks_field") 
            obj = GeeksModel.objects.create( 
                                 title = name,  
                                 img = img 
                                 ) 
            obj.save() 
            print(obj) 
    else: 
        form = GeeksForm() 
        context['form']= form 
    return render(request,'profile.html',context)
def post (request):
    image = Image.save_Image()
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = LetterRecipients(name = name,email =email)
            recipient.save()
            send_welcome_email(name,email)
            HttpResponseRedirect('post')
    else:
        form = LetterForm()
    
    return render(request,'post.html',{'image':image, 'letterForm':form})

@login_required(login_url='/accounts/login/')
def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-photos/image.html", {"image":image})

@login_required(login_url='/accounts/login/')
def new_image(request):
    current_user = request.user
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.editor = current_user
            image.save()
        return redirect('post')

    else:
        form = NewImageForm()
    return render(request, 'new_post.html', {"form": form})

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
