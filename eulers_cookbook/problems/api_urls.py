from django.conf.urls import include, url
from django.views.generic import TemplateView
from problems import views

urlpatterns = [

    url(r'^v2/problem/(?P<problem_number>\d+)(\..+)?/$', views.EulerProblemAPIView.as_view(), 
    	name='api_euler_problem'),

]
