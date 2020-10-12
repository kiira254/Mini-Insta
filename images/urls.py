from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post, name = 'post'),
    path('image/<int:id>',views.image,name ='image'),
    # path('new/image', views.new_image, name='new-image'),
    # path('search/', views.search_results, name='search_results'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)