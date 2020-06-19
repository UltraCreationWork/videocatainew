from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from tinymce.models import HTMLField
from django.conf.global_settings import AUTH_USER_MODEL

class PostView(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Comment(models.Model):
    user        = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    timestamp   = models.DateTimeField(auto_now_add=True)
    content     = models.TextField()
    post        = models.ForeignKey('Post', related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Author(models.Model):
    user            =       models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    full_name       =       models.CharField(max_length=255,blank=True)
    profession      =       models.CharField(max_length=30, blank=True)
    about_you       =       models.TextField(blank=True)
    topics          =       models.TextField(blank=True)
    profile_picture =       models.ImageField(upload_to="media",default="default.jpg")


    def __str__(self):
        return self.full_name

    def get_update_url(self):
        return reverse('profile', kwargs={
            'user': self.user
        })
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Post(models.Model):
    title                   =           models.CharField(max_length=100)
    video                    =          models.FileField()
    timestamp               =           models.DateTimeField(auto_now_add=True)
    content                 =           models.TextField()
    comment_count           =           models.IntegerField(default=0)
    author                  =           models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail               =           models.ImageField(upload_to='media')
    categories              =           models.ManyToManyField(Category)
    suggestion_first        =           models.ForeignKey('self', related_name='suggested_one', on_delete=models.SET_NULL, blank=True, null=True)
    suggestion_second       =           models.ForeignKey('self', related_name='suggested_two', on_delete=models.SET_NULL, blank=True, null=True)
    suggestion_third        =           models.ForeignKey('self', related_name='suggested_three', on_delete=models.SET_NULL, blank=True, null=True)
    suggestion_fourth       =           models.ForeignKey('self', related_name='suggested_four', on_delete=models.SET_NULL, blank=True, null=True)
    suggestion_fifth        =           models.ForeignKey('self', related_name='suggested_five', on_delete=models.SET_NULL, blank=True, null=True)
    suggestion_sixth        =           models.ForeignKey('self', related_name='suggested_six', on_delete=models.SET_NULL, blank=True, null=True)
    suggestion_seventh      =           models.ForeignKey('self', related_name='suggested_seven', on_delete=models.SET_NULL, blank=True, null=True)

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

    @property
    def view_count(self):
        return PostView.objects.filter(post=self).count()







