from django.shortcuts import render,redirect
from django.utils import timezone
from .models import Post
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django.views.defaults import page_not_found
from .models import Chat
from .forms import PostForm, CommentForm
from .models import Post, Comment

#Lista de Post, Detalles del mismo, Nueva publicación, Editar Post.

@login_required(login_url='/dw_login')
def post_list(request):
    posts = Post.objects.order_by('-created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required(login_url='/dw_login')
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

@login_required(login_url='/dw_login')  
def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

@login_required(login_url='/dw_login')
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
    

#Home, Post propios(Publicados), Detalles de los mismos.
 
@login_required (login_url='/dw_login')
def index (request):
    usuario = request.user
    return render_to_response('blog/index.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required (login_url='/dw_login')
def dw_home (request):
    usuario = request.user
    return render_to_response('blog/dw_home.html', {'usuario':usuario}, context_instance=RequestContext(request))

@login_required(login_url='/dw_login')
def post_list_privado(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/post_list_privado.html', {'posts': posts})


#Cierre de sesión

@login_required(login_url='/dw_login')
def dw_logout (request):
    logout (request)
    return HttpResponseRedirect('/')
    

#Añadir comentarios a la publicación.

@login_required (login_url='/dw_login')
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})
    
#Login y Register
    
def dw_register(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render_to_response('blog/dw_register.html', {'form': form}, context_instance=RequestContext(request))


def dw_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/index')
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso) 
                    return HttpResponseRedirect('/index')
                else:
                    return render_to_response('blog/dw_login/noactivo.html', context_instance=RequestContext(request))
            else:
                return render_to_response('blog/dw_fail_user.html', context_instance=RequestContext(request))
    else:
        form = AuthenticationForm()
    return render_to_response('blog/dw_login.html', {'form': form}, context_instance=RequestContext(request))


#Chat

@login_required (login_url='/dw_login')
def dw_chat(request):
    c = Chat.objects.all()
    return render(request, "blog/dw_chat.html", {'home': 'active', 'chat': c})


@login_required (login_url='/dw_login')
def Mensaje(request):
    if request.method == "POST":
        msg = request.POST.get('msgbox', None)
        c = Chat(user=request.user, message=msg)
        if msg != '':
            c.save()
        return JsonResponse({ 'msg': msg, 'user': c.user.username })
    else:
        return HttpResponse('Request must be POST.')


@login_required (login_url='/dw_login')
def Messages(request):
    c = Chat.objects.all()
    username = request.POST['username']
    return render(request, 'blog/messages.html', {'chat': c})






