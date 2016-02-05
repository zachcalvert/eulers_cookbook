import json
import math
from datetime import datetime
from fractions import gcd
from functools import reduce

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic import TemplateView, View, ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from problems.models import Problem


class ProblemListView(ListView):
    template_name = 'base.html'
    paginate_by = 15

    def get_queryset(self):
        display = self.request.GET.get('display', 'all')
        
        if display == 'solved':
            queryset = Problem.objects.filter(solved=True)
        elif display == 'unsolved':
            queryset = Problem.objects.filter(solved=False)
        else:
            queryset = Problem.objects.all()

        return queryset.order_by('number')

    def get_context_data(self, *args, **kwargs):
        context = super(ProblemListView, self).get_context_data(**kwargs)
        context['display'] = self.request.GET.get('display', 'all')
        return context


class EulerProblemView(TemplateView):
    template_name = 'problem.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EulerProblemView, self).get_context_data(**kwargs)
        context['problem'] = get_object_or_404(Problem, number=kwargs['problem_number'])
        return context


class EulerProblemAPIView(View):
    """ 
    API endpoint that returns JSON formatted problem data
    """
    def get(self, request, problem_number):
        if not problem_number:
            return HttpResponse(json.dumps('please specify a problem number'))

        try:
            problem_number = int(problem_number)
        except ValueError:
            return HttpResponse(json.dumps('Please provide an integer value.', status=400))

        problem = Problem.objects.get(number=problem_number)

        content = {
            'number': problem.number,
            'title': problem.title,
            'description': problem.description,
            'euler_link': problem.link,
            'solved': problem.solved,
            # 'solution': problem.solution,
            'num_inputs': problem.num_inputs,
            'callback_function': problem.callback_function,
            'output_column_header': problem.output_column_header
        }

        return HttpResponse(json.dumps(content))


class InteractiveSolutionView(View):
    """
    Abstract view that takes one integer as input, calculates the result (different per implementation)
    and returns
    a json dict with input, output and timestamp.
    """

    def get_current_time(self):
        return datetime.now().strftime('%m-%d %H:%M:%S')

    def get(self, request):
        x = request.GET.get('x', None)    

        if not x:
            return HttpResponse('Please provide a value.', status=400)    

        try:
            x = int(x)
        except ValueError:
            return HttpResponse('Please provide an integer value.', status=400)

        # check for multiple inputs
        y = self.request.GET.get('y', None)

        if y:
            try:
                y = int(y)
            except ValueError:
                return HttpResponse('Please provide two integer values.', status=400)
            value = self.calculate_result(x, y) 
        else:
            value = self.calculate_result(x) 

        content = {
            'x': x,
            'value': value,
            'last_requested': self.get_current_time()
        }

        if y:
            content['y'] = y

        return HttpResponse(json.dumps(content))


class MultiplesOfThreeAndFiveView(InteractiveSolutionView):
    """
    Problem 1: Multiples of Three and Five
    """
    def multiples_of_three_and_five(self, x):
        return sum([i for i in range(x) if i % 3 == 0 or i % 5 == 0])

    def calculate_result(self, x):
        return self.multiples_of_three_and_five(x)


class EvenFibonacciNumbersView(InteractiveSolutionView):
    """
    Problem 2: Even Fibonacci numbers
    """
    def even_fibonacci_numbers(self, x):
        a, b = 1, 1
        total = 0
        while a <= x:
            if a % 2 == 0:
                total += a
            a, b = b, a+b
        return total

    def calculate_result(self, x):
        return self.even_fibonacci_numbers(x)


class LargestPrimeFactorView(InteractiveSolutionView):
    """
    Problem 3: Largest Prime Factor
    """
    def largest_prime_factor(self, x):
        i = 2
        while i * i < x:
            while x % i == 0:
                x = x / i
            i = i + 1    
        return x

    def calculate_result(self, x):
        return self.largest_prime_factor(x)


class LargestPalindromeProductView(InteractiveSolutionView):
    """
    Problem 4: Largest Palindrome Product
    """

    def is_palindrome(self, x):
        return str(x) == str(x)[::-1]    

    def largest_palindrome_product(self, minimum, maximum):
        z = 0
        x_in = 0
        y_in = 0
        for x in range(maximum, minimum, -1):
            for y in range(maximum,minimum, -1):
                if self.is_palindrome(x*y):
                    if x*y > z:
                        z = x*y
                        x_in = x
                        y_in = y        

        return z

    def calculate_result(self, x, y):
        return self.largest_palindrome_product(x, y)


class SmallestMultipleView(InteractiveSolutionView):
    """
    Problem 5: Smallest Multiple
    """

    def smallest_multiple(self, minimum, maximum):
        return minimum*maximum//gcd(minimum, maximum)

    def calculate_result(self, x, y):
        return reduce(self.smallest_multiple, range(x, y+1))


class SumSquareDifferenceView(InteractiveSolutionView):
    """
    Problem 6: Sum Square Difference
    """  

    def square_of_sums(self, x):
        return sum([ i for i in xrange(1, x + 1) ]) ** 2

    def sum_of_squares(self, x):
        return sum([ i * i for i in xrange(1, x + 1) ])  

    def calculate_result(self, x):
        """
        Problem 6: Sum Square Difference
        """
        return self.square_of_sums(x) - self.sum_of_squares(x)


class TenThousandandFirstPrimeView(InteractiveSolutionView):
    """
    Problem 7: 10,0001st Prime
    """

    def is_prime(self, x):
        if x % 2 == 0 and x > 2:
            return False
        return all(x % i for i in range(3, int(math.sqrt(x)) + 1, 2))

    def nth_prime(self, x):
        i=0
        counter=1
        while (i < x):
            counter += 1;
            if self.is_prime(counter):
                i += 1;
        return counter

    def calculate_result(self, x):
        return self.nth_prime(x)
