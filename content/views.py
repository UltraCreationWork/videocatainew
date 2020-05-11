from django.shortcuts import render
from django.utils import timezone
from.models import Post,Author
from django.views.generic import DetailView,ListView
from django.contrib.auth.models import User
from django.db.models import Q

def get_author(user):
    qs = Author.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None


def search(request):
    queryset = Post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)
        ).distinct()

    context = {
        'queryset': queryset
    }
    return render(request, 'search.html', context)

def home(request):
    context={
        'posts': Post.objects.all(),
        'latest_posts':Post.objects.order_by('-timestamp')[0:3],
        'authors':Author.objects.all()
        }
    return render(request,'index.html',context)

class Post_detail(DetailView):
    model = Post
    template_name = 'preview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class Author_detail(DetailView):
    model = Author
    template_name = 'preview.html'


    
