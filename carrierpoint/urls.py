from django.contrib import admin
from django.urls import path,include
from content.views import home,Post_detail,Author_detail,search,Post_Create
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required





    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('',home,name="home"),
    path('accounts/',include('allauth.urls')),
    path("create/",login_required(Post_Create.as_view()),name="post-create"),
    path('post/<int:pk>',Post_detail.as_view(),name="post"),
    path('author/<user>',Author_detail.as_view(),name="profile"),
    path('search/',search,name='search'),
    


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)