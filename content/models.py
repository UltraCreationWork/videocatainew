from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from tinymce.models import HTMLField



class Author(models.Model):
    user            =       models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name       =       models.CharField(max_length=255,blank=True)
    profession      =       models.CharField(max_length=30, blank=True)
    about_you       =       models.TextField(blank=True)
    topics          =       models.TextField(blank=True)
    profile_picture =       models.ImageField(upload_to="media",default="default.jpg")


    def __str__(self):
        return self.full_name

    def get_update_url(self):
        return reverse('profile-page', kwargs={
            'user': self.user
        })

class Post(models.Model):
    title           =           models.CharField(max_length=100)
    file            =           models.FileField(upload_to='media')
    timestamp       =           models.DateTimeField(auto_now_add=True)
    content         =           models.TextField()
    comment_count   =           models.IntegerField(default=0)
    author          =           models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail       =           models.ImageField()
    categories      =           models.CharField(max_length=255)
    previous_post   =           models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    next_post       =           models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={
            'pk': self.pk
        })

    def get_update_url(self):
        return reverse('post-update', kwargs={
            'pk': self.pk
        })

    def get_delete_url(self):
        return reverse('post-delete', kwargs={
            'pk': self.pk
        })

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')







