from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.shortcuts import render


# Create your views here.
#로그인 연동으로 Django 내부 라이브러리로 있는 authenticate를 사용하였다
#---------------회원가입----------------#
def signup(request):
    if request.method == "POST":
        if request.POST["password01"] == request.POST["password02"]: #signup.html로 부터 입력받은 값을 POST 형식으로 가져온다
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password01"])
            auth.login(request,user)
            return redirect('index')
        return render(request, 'signup.html')
    return render(request,'signup.html')
#---------------로그인------------------#
def signin(request):
    if request.method == "POST":
        username = request.POST["username1"]
        password = request.POST["password1"]
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request,'signin.html', {'error':'username or password is incorrect'})
    else:
        return render(request,'signin.html')
    
#----------------로그아웃----------------#
def logout(request):
    auth.logout(request)
    return redirect('signin')