from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

#Modelo Post
class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	titulo = models.CharField(max_length=20)
	texto = models.TextField()
	archivo = models.FileField(upload_to='documents/', blank=True, null=True)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)
		
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.titulo
		

#Modelo Comentarios
class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User')
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.texto


def approved_comments(self):
    return self.comments.filter(approved_comment=True)


#Modelo Chat
class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message





