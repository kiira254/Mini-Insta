from django.db import models
import datetime as dt
from django.contrib.auth.models import User
import django.utils.timezone
from django.db.models.signals import post_save
from tinymce.models import HTMLField
# from pyuploadcare.dj.models import ImageField

# Create your models here.
# class GeeksModel(models.Model): 
#     title = models.CharField(max_length = 200) 
#     img = models.ImageField(upload_to = "images/") 
    
#     def __str__(self): 
#         return self.title 

class Image(models.Model):
    image = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length =60)
    caption =HTMLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    
    
    class Meta:
        ordering = ('-post_date',)

    def __str__(self):
        return self.name

    @classmethod
    def search_by_title(cls,search_term):
        image = cls.objects.filter(name__icontains=search_term)
        return image

    @classmethod
    def save_Image (cls):
        image=cls.objects.filter()
        return image

    @classmethod
    def delete_Image (cls):
        image=cls.objects.filter()
        return image

    @classmethod
    def update_caption():
        self.save()

    @classmethod
    def get_image_id(cls, id):
        image = Image.objects.get(pk=id)
        return image
    
    @classmethod
    def get_profile_images(cls, profile):
        images = Image.objects.filter(profile__pk = profile)
        return images
    
    @classmethod
    def get_all_images(cls):
        images = Image.objects.all()
        return images


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_name = self.request.GET.get('user_name', '')
        context['all_search_results'] = User.objects.filter(username__icontains=user_name )
        return context

    @classmethod
    def get_comments_by_images(cls, id):
        comments = Comments.objects.filter(image__pk = id)
        return comments

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.like

    
    def like(request, picture_id):
        new_like, created = Like.objects.get_or_create(user=request.user, picture_id=picture_id)
       
    def picture_detail(request, id):
        pic = get_object_or_404(Picture, pk=id)
        user_likes_this = pic.like_set.filter(user=request.user) and True or False

class Comments(models.Model):
    comment = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE,)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments

    
    

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = "images/")
    bio = HTMLField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    @classmethod
    def save_profile(self):
        self.save()
    
    @classmethod
    def delete_profile(self):
        self.delete()

    @classmethod
    def updateProfile(self, update):
       self.bio = update
       self.save

    @classmethod
    def search_profile(cls, search_term):
        user = cls.objects.filter(user__username__icontains=search_term)
        return user 

    @classmethod
    def get_by_id(cls, id):
        profile = cls.objects.get(id=id)
        return profile

    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    
class LetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()