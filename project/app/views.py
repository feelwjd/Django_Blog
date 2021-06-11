from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from django.http import Http404
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="/signin")
def index(request):
    auser = request.user
    anid = auser.username
    blog = Blog.objects

    return render(request,'index.html',{'id':anid,'blog':blog})

def detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        raise Http404('해당 게시물을 찾을 수 없습니다.')
    return render(request,'detail.html',{'blog':blog})

def newr(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        auser = request.user.username
        new_board = Blog(
            title = form.cleaned_data['title'],
            body = form.cleaned_data['body'],
            writer = auser
        )
        new_board.save()
        return redirect('/')
    return render(request, 'newr.html', {'form' :form})