from django.conf.urls import url
from app_four import views

#template tagging
app_name = 'app_four'

urlpatterns = [
    url(r'^info/$', views.info, name='info'),
    url(r'^other/$', views.other, name='other')
]
