from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField
# from pyuploadcare.dj.models import ImageField

# Create your models here.
class GeeksModel(models.Model): 
    title = models.CharField(max_length = 200) 
    img = models.ImageField(upload_to = "images/") 
    
    def __str__(self): 
        return self.title 

class Image(models.Model):
    image = models.ImageField(upload_to = "images/")
    name = models.CharField(max_length =60)
    caption =HTMLField(blank=True)
    post_date = models.DateTimeField(auto_now=True)
    likes = models.BooleanField(default=False)
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    comments = HTMLField (max_length=1500)
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

# class Comments(models.Model):
#     user_comment = HTMLField()
#     posted_on = models.DateTimeField(auto_now=True)
#     image = models.ForeignKey(Image, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     def save_comment(self):
#         self.save()
    
    

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to = "images/")
    bio = HTMLField(null=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)

    def save_profile(self):
        self.save()
    
    @classmethod
    def search_profile(cls, name):
        profile = Profile.objects.filter(user__username__icontains = name)
        return profile
    
    @classmethod
    def get_by_id(cls, id):
        profile = Profile.objects.get(user = id)
        return profile

    @classmethod
    def save_profile (cls):
        profile_photo=cls.objects.filter()
        return profile_photo

    @classmethod
    def delete_profile (cls):
        profile_photo=cls.objects.filter()
        return profile_photo

    @classmethod
    def update_profile():
        self.save                                  ()

    @classmethod
    def filter_by_id(cls, id):
        profile = Profile.objects.filter(user = id).first()
        return profile
    def __str__(self):  
        return "%s's profile" % self.profile_photo  

class LetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()