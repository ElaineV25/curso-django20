# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
# raise ValueError()
# return HttpResponse('<html><body>Olá Django</body></html><', content_type='text/html')
from pypro.modulos import facade


def home(request):
    return render(request, 'base/home.html', {})
