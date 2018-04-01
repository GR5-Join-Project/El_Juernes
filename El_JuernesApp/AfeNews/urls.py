from AfeNews import views
from AfeNews.views import Afe_News_List, News_assigned
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('', Afe_News_List, name="AFE"),
    path('assigned/', News_assigned, name="assigned"),
    url(r'^new/(?P<slug>[\w-]+)/$', views.full_new_and_assignations.as_view(), name='full_new_and_assignations')
]
