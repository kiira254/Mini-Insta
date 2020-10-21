from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime as dt
from .models import Image, Profile, Like,GeeksModel, Comments
from .email import send_welcome_email
from django.contrib.auth.decorators import login_required
from .forms import LetterForm, ImageForm, GeeksForm,SignupForm,ProfileForm, CommentForm
from django.contrib.auth.models import User
# Create your views here.

@login_required(login_url='/accounts/login/')
def profile (request):
    current_user = request.user
    
    posts = Image.save_Image()
    comments = Comments.get_comments()
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
    return render(request,'profile/profile.html',context)

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=Profile.objects.get(user_id=current_user))
        if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
        return redirect('home')

    
    else:
        if Profile.objects.filter(user_id=current_user).exists():
            form = GeeksForm(instance = Profile.objects.get(user_id=current_user))
        else:
            form = GeeksForm()
    return render(request, 'profile/edit-profile.html', {'current_user':current_user, 'form':form, 'profile':profile})


@login_required(login_url='/accounts/login/')
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
            image.user = current_user
            image.save()
        return redirect('post')

    else:
        form = ImageForm()
    return render(request, 'new_post.html', {'current_user':current_user,"form": form})

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


def signup(request):
    name = "Sign Up"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('username')
            send_mail(
            'Welcome to Mini-Insta.',
            f'Hello {name},\n '
            'Welcome to Mini-Insta.',
            'nkamotho69@gmail.com',
            [email],
            fail_silently=False,
            )
        return redirect('post')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form, 'name':name})

def likes(request,id):
    likes=0
    post = Post.objects.get(id=id)
    post.likes = post.likes+1
    post.save()    
    return redirect("home")