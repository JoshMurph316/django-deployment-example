from django.conf.urls import url
from app_two import views

urlpatterns = [
    url(r'^help/', views.help, name='help'),
    url(r'^$', views.users, name='users'),
    url(r'^$', views.index, name='index')
]
