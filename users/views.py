from curses.ascii import US
from click import password_option
from django.http import HttpResponse
from django.shortcuts import render
from regex import P
from .models import User

# Create your views here.
def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html')
    elif request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        passwordcheck = request.POST.get('passwordcheck')
        if password == passwordcheck:
            User.objects.create_user(username=username, password=password)
            return HttpResponse('회원가입 완료!!')
        else:
    
            return HttpResponse('비밀번호 확인해주세요')
    else:
        return HttpResponse("허용되지 않은 메소드입니다.")
    
    