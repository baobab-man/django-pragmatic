from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def romeo(request):

    if request.method == "POST":
        return render(request, 'account_app/romeo.html', context={'text': 'POST METHOD!!!'})
    else:
        return render(request, 'account_app/romeo.html',
                      context={'text': 'GET METHOD!!!'})
