from django.shortcuts import render
from.models import Post,Author
from django.views.generic import DetailView



def home(request):
    context={
        'posts': Post.objects.all()}
    return render(request,'index.html',context)


class Post_detail(DetailView):
    model = Post
    template_name = 'preview.html'
    
