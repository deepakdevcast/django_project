from django.shortcuts import render
from django.http import HttpResponse
from user_app.models import User
# Create your views here.
def index(request):
    user_del = User.objects.order_by('first_name')
    user_dict = {'access_users':user_del}
    return render(request,'user_app/home.html',context=user_dict)
