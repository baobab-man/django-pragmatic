from django.urls import path

from account_app.views import romeo

app_name = "account_app"

urlpatterns = [
    path('romeo/', romeo, name='romeo')
]