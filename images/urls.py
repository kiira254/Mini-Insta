from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path('', views.post, name = 'post'),
    path('image/<int:id>',views.image,name ='image'),
    path('new/image', views.new_image, name='new-image'),
    path('search/', views.search_user, name='search_results'),
    path('profile/',views.profile, name='profile'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login', LoginView.as_view(), name='login_url'),
    url(r'^logout/', LogoutView.as_view(next_page='login_url'), name='logout_url'),
    url(r'^new_image/$', views.new_image, name='new_post'),
    url(r'^user/(\d+)$', views.profile, name='profile'),
    url(r'^update_profile/', views.update_profile, name='update_profile'),
    url(r'^likes/(?P<id>\d+)',views.likes,name ='like'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)