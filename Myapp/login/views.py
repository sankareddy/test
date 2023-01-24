from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from login.models import loginhistory
import datetime
# Create your views here.
def test(request):
    return HttpResponse("This is login page ")

def loginuser(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username = username)
        except:
            print("Username does not exist")
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            current_time = datetime.datetime.now()
            loginhistory.objects.create(user_id= request.user,login_date_time=current_time)
            return redirect('details')
        else:
            print("Username or password is incorrect")
        print(request.post)
    return render (request,'loginpage.html')

def details(request):
    username_data = request.user.username
    userid  = User.objects.values().filter(username=username_data)
    user_id = (list(userid)[0]['id'])
    details = loginhistory.objects.all().filter(user_id = user_id)
    return render(request,'details.html',{'message':details,'username_data':username_data,'userid':user_id})