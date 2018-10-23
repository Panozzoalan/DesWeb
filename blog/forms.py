from django import forms
from .models import Chat
from .models import Post
from .models import Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('titulo', 'texto', 'archivo')
		
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('texto',)
