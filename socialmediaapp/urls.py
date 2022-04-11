from django.conf import settings
from django.contrib import admin
from django.urls import path
from socialmediaapp import views
from django.conf.urls.static import static


# Django admin header customization 

admin.site.site_header = "Social Media Project"
admin.site.site_title= "Welcome to Omm's Dashboard"
admin.site.index_title = "Welcome to this Portal"

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('<id>/<slug>',views.post_detail,name='post_detail'),
    path('post_create/',views.post_create,name='post_create'),
    path('login/',views.user_login,name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('register/',views.register,name='register'),
    path('edit_profile/',views.edit_profile,name='edit_profile')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)