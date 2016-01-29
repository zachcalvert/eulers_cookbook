from django.conf.urls import include, url
from django.views.generic import TemplateView
from problems import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='site_home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^(?P<problem_number>\d+)(\..+)?/$', views.EulerProblemView.as_view(), 
    	name='euler_problem'),    


    # interactive callback urls
	url(r'^1/multiples_of_three_and_five$', views.ProblemOneView.as_view(), 
		name='multiples_of_three_and_five'),

	url(r'^2/even_fibonacci_numbers$', views.ProblemOneView.as_view(), 
		name='even_fibonacci_numbers'),

]