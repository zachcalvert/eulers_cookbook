from django.conf.urls import include, url
from django.views.generic import TemplateView
from problems import views

urlpatterns = [
    url(r'^$', views.site_home, name='site_home'),
    url(r'^about/$', views.about, name='about'),

    url(r'^(?P<problem_number>\d+)(\..+)?/$', views.euler_problem, name='euler_problem'),    
]