from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User
#
# Create your views here.


class main(View):
    templates = 'login_form.html'
    def get(self,request):
        return render(request, self.templates, { })
    def post(self,request):
        if User.objects.filter(id=request.POST.get['id'],password=request.POST.get['password']).exists():
            return redirect('/home')
        else:
            print("not exist id, password")
            return redirect('/home/error')
    
    
class signup(View):
    templates = 'signup_form.html'
    def get(self,request):
        return render(request, self.templates, {})
    def post(self, request):
        if User.objects.filter(id=request.POST.get['id']).exists():
                print("exist")
                return redirect('/home/error')
        else:
            user = User(id = request.POST.get['id'], password = request.POST.get['password'])
            user.save()
            return redirect('/login')