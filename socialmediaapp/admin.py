from django.contrib import admin
from socialmediaapp.models import Post,Profile
# Register your models here.

class AdminPost(admin.ModelAdmin):
    list_display = ['title','slug','author','body']
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title','author__username')
    date_hierarchy = ('created')


class AdminProfile(admin.ModelAdmin):
    list_display = ['user','dob','photo']
    search_fields = ('dob','user')
    # date_hierarchy = ('created') # not supported in media file


admin.site.register(Post,AdminPost)
admin.site.register(Profile,AdminProfile)




# subas 1234abcd(superuser)
# liza  mona@143
# mona   liza@143
# sunil sunil123
# puja  puja@123