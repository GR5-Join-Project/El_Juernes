from AfeNews import views
from django.conf.urls import url
from django.urls import path

urlpatterns = [
    path('', views.Afe_News_List, name="AFE"),
    path('assigned/', views.News_assigned, name="assigned"),
    url(r'^new/(?P<slug>[\w-]+)/$', views.full_new_and_assignations.as_view(), name='full_new_and_assignations'),
    url(r'^assigned/(?P<slug>[\w-]+)/$', views.new_copywriter.as_view(), name='new_copywriter'),
]
