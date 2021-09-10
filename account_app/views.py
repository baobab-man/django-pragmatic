from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def romeo(request):
    return render(request, 'account_app/romeo.html')
