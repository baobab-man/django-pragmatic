from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from account_app.models import Romeo


def romeo(request):

    if request.method == "POST":

        temp = request.POST.get('romeo_input')

        new_romeo = Romeo()
        new_romeo.text = temp
        new_romeo.save()

        return render(request, 'account_app/romeo.html', context={'romeo_output': new_romeo})
    else:
        return render(request, 'account_app/romeo.html',
                      context={'text': 'GET METHOD!!!'})
