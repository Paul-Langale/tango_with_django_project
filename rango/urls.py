from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about?\/?$', views.about, name='about'),
    ]
#about added in the 3.6 excersise
