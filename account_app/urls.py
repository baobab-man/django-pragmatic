from django.urls import path

from account_app.views import romeo, AccountCreateView

app_name = "account_app"

urlpatterns = [
    path('romeo/', romeo, name='romeo'),
    path('create/', AccountCreateView.as_view(), name='create'),
]
