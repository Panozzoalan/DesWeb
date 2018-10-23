from django.conf.urls import include, url
from . import views
from django.conf.urls import handler404, handler500

urlpatterns = [
#URL Login
	url(r'^$', views.dw_login),
#URL Post
	url(r'^dw_home/posteos$', views.post_list, name='lista'),
	url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail,  name='post_detail'), 
	url(r'^post/nuevo/$', views.post_new, name='post_new'),
	url(r'^post/(?P<pk>[0-9]+)/editar/$', views.post_edit, name='post_edit'),
#URL Home, Logout
	url(r'^dw/registro$', views.dw_register, name='dw_register'),
	url(r'^dw_logout/$', views.dw_logout),
	url(r'^dw_home/$', views.dw_home),
	url(r'^index/$', views.index),
#URL Post Propios
	url(r'^dw_home/mis-posteos$', views.post_list_privado),
#URL Comentarios
	url(r'^post/(?P<pk>\d+)/comentario/$', views.add_comment_to_post, name='add_comment_to_post'),
#URL Chat
	url(r'^dw_chat/$', views.dw_chat, name='dw_chat'),
	url(r'^post/$', views.Mensaje, name='Mensaje'),
	url(r'^messages/$', views.Messages, name='messages'),
]
