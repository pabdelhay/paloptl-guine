from django.shortcuts import render
from django.views import View


class TestView(View):
    def get(self, request):
        return render(request, 'teste.html', context={})
