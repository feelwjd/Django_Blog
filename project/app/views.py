from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/signin")
def index(request):
    auser = request.user
    anid = auser.username
    return render(request,'index.html',{'id':anid})