from django.forms import forms,ModelForm
from .models import Comment,Post

class CreatForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title','categories','content','video','thumbnail','author','suggestion_first','suggestion_second','suggestion_third','suggestion_fourth','suggestion_fifth','suggestion_sixth','suggestion_seventh' ]

