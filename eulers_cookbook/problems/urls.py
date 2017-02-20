from django.conf.urls import include, url
from django.views.generic import TemplateView
from problems import views

urlpatterns = [

    url(r'^$', views.ProblemListView.as_view(), name='site_home'),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"), name='about'),
    url(r'^search/$', include('haystack.urls')),

    url(r'^(?P<problem_number>\d+)(\..+)?/$', views.EulerProblemView.as_view(), 
    	name='euler_problem'),    

    # interactive problem urls
	url(r'^1/multiples_of_three_and_five$', views.MultiplesOfThreeAndFiveView.as_view(), 
		name='multiples_of_three_and_five'),

	url(r'^2/even_fibonacci_numbers$', views.EvenFibonacciNumbersView.as_view(), 
		name='even_fibonacci_numbers'),

	url(r'^3/largest_prime_factor$', views.LargestPrimeFactorView.as_view(), 
		name='largest_prime_factor'),

	url(r'^4/largest_palindrome_product$', views.LargestPalindromeProductView.as_view(),
		name='largest_palindrome_product'),

	url(r'^5/smallest_multiple$', views.SmallestMultipleView.as_view(),
		name='smallest_multiple'),

	url(r'^6/sum_square_difference$', views.SumSquareDifferenceView.as_view(), 
		name='sum_square_difference'),

	url(r'^7/10001st_prime$', views.TenThousandAndFirstPrimeView.as_view(),
		name='10001st_prime'),

	url(r'^10/summation_of_primes$', views.SummationofPrimesView.as_view(),
		name='summation_of_primes'),

	url(r'^16/power_digit_sum$', views.PowerDigitSumView.as_view(),
		name='power_digit_sum'),

	url(r'^20/factorial_digit_sum$', views.FactorialDigitSumView.as_view(),
		name='factorial_digit_sum'),

	url(r'^35/circular_primes$', views.CircularPrimesView.as_view(),
		name='circular_primes'),

	url(r'^36/double_base_palindromes$', views.DoubleBasePalindromesView.as_view(),
		name='double_base_palindromes'),
	
]
