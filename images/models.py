from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'image/'blank=True)
    name = models.CharField(max_length =60)
    caption = models.TextField()
    Profile= models.ForeignKey(User,on_delete=models.CASCADE)
    likes=models.like_set.all().count()

    @classmethod
    def save_Image (cls):
        photos=cls.objects.filter()
        return photos

    @classmethod
    def delete_Image (cls):
        photos=cls.objects.filter()
        return photos

    @classmethod
    def update_caption():
        self.save()

    def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    user_name = self.request.GET.get('user_name', '')
    context['all_search_results'] = User.objects.filter(username__icontains=user_name )
    return context

class Like(models.Model):
    user = models.ForeignKey(User)
    picture = models.ForeignKey(Picture)
    created = models.DateTimeField(auto_now_add=True)

    
    def like(request, picture_id):
        new_like, created = Like.objects.get_or_create(user=request.user, picture_id=picture_id)
        if not created:
            # the user already liked this picture before
        else:
            # oll korrekt

    def picture_detail(request, id):
        pic = get_object_or_404(Picture, pk=id)
        user_likes_this = pic.like_set.filter(user=request.user) and True or False

class Profile
    user = models.OneToOneField(User)
    Profile_photo = models.ImageField(upload_to = 'image/'blank=True)
    Bio = models.TextField()

    def __str__(self):  
        return "%s's profile" % self.user  
