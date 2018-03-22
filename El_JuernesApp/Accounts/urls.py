from django.urls import path

from Accounts.views import Home

urlpatterns = [
    path('logged_in/', Home),

]
