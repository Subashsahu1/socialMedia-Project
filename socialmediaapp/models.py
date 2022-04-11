from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save 
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("post_detail", args=[self.id,self.slug])

    class Meta:
        verbose_name_plural = 'Post'

@receiver(pre_save, sender=Post)
def pre_save_slug(sender, **kwargs):
    slug1 = slugify(kwargs['instance'].title)
    kwargs['instance'].slug = slug1


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    dob = models.DateField(null=True,blank=True)
    photo = models.ImageField(null=True,blank=True)

    def __str__(self):
        return 'Profile of user {}'.format(self.user.username)

    class Meta:
        verbose_name_plural = 'Profile'