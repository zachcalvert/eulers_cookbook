from django.conf.urls import include, url
from django.views.generic import TemplateView
from problems import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='site_home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),

    url(r'^(?P<problem_number>\d+)(\..+)?/$', views.EulerProblemView.as_view(), name='euler_problem'),    
]