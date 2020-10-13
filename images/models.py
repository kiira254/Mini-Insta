from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from tinymce.models import HTMLField

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'image/',blank=True)
    name = models.CharField(max_length =60)
    caption =HTMLField()
    profile= models.ForeignKey(User,on_delete=models.CASCADE)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    # likes = models.ManyToManyField(User, through="Like")

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_name = self.request.GET.get('user_name', '')
        context['all_search_results'] = User.objects.filter(username__icontains=user_name )
        return context

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

    # @classmethod
    # def search_image(cls, key):
    #     Image = cls.objects.filter(
    #         cls(caption__contains=key) | cls(name__icontains=key))
    #     print(Image)
    #     return Image

    # @classmethod
    # def search_by_category(cls, name):
    #     Image = cls.objects.filter(name__icontains=name)
    #     return Image


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_photo = models.ImageField(upload_to = 'image/', blank=True)
    Bio = models.TextField()

    def __str__(self):  
        return "%s's profile" % self.profile_photo  

class LetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()