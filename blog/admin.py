from django.contrib import admin
from .models import Post
from .models import Comment
from .models import Chat

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Chat)


#class Post (models.Model):
#	author = model.Foreignkey('auth.user')
#	titulo = model.CharField()
#	texto = model.TextField ()
#	creation_date = model.DateTimeField(default=timezone.now)
#	
#	def publish (self):
#		self.save()
#		
#	def __str__ (self):
#		return post.titulo

#from .models import Post

#class PostForm (forms.ModelForm):
#	class Meta:
#		model = Post
#		field = ('titulo')