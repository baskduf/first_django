from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class main(View):
    context = {}
    template_name = 'index.html'
    def get(self, request):
        return render(request, self.template_name, self.context)
    def post(self, request):
        return render(request, self.template_name, self.context)
    