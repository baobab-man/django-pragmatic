from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from account_app.models import Romeo


def romeo(request):

    if request.method == "POST":

        temp = request.POST.get('romeo_input')

        new_romeo = Romeo()
        new_romeo.text = temp
        new_romeo.save()

        return HttpResponseRedirect(reverse('account_app:romeo'))
    else:
        romeo_list = Romeo.objects.all()
        return render(request, 'account_app/romeo.html',
                      context={'romeo_list': romeo_list})
