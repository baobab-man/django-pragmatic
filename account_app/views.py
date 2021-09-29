from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('account_app:romeo')
    template_name = 'account_app/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'account_app/detail.html'
