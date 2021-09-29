from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from account_app.views import romeo, AccountCreateView, AccountDetailView

app_name = "account_app"

urlpatterns = [
    path('romeo/', romeo, name='romeo'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name='account_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
]
