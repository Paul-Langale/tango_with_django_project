from django.conf.urls import url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about?\/?$', views.about, name='about'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),
    #added this VlineV in ch6 bullet 2 needs to be category page also changed in index template
    #url(r'^page/(?P<page_name_slug>[\w\-]+)/$',
    #    views.show_category, name='page_category'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/$',
        views.add_page, name='add_page'),
    ]

