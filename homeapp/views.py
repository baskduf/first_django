from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class main(View):
    template='home.html'

    def get(self, request):
        return render(request, self.template, {})
    
class error(View):
    template='error.html'

    def get(self, request):
        return render(request, self.template, {})