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
from problems import utils


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
            return HttpResponse(json.dumps('A problem number is required.', status=400))

        try:
            problem_number = int(problem_number)
        except ValueError:
            return HttpResponse(json.dumps('A problem number is required.', status=400))

        problem = Problem.objects.get(number=problem_number)

        content = {
            'number': problem.number,
            'title': problem.title,
            'description': problem.description,
            'euler_link': problem.link,
            'solved': problem.solved,
            'num_inputs': problem.num_inputs,
            'callback_function': problem.callback_function,
            'output_column_header': problem.output_column_header
        }

        return HttpResponse(json.dumps(content))


class InteractiveSolutionView(View):
    """
    Abstract view that takes one or two integers as input, calculates the result (different per implementation)
    and returns a json dict with input(s), output and timestamp.
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

    def largest_palindrome_product(self, minimum, maximum):
        z = 0
        x_in = 0
        y_in = 0
        for x in range(maximum, minimum, -1):
            for y in range(maximum,minimum, -1):
                if utils.is_palindrome(x*y):
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


class TenThousandAndFirstPrimeView(InteractiveSolutionView):
    """
    Problem 7: 10,0001st Prime
    """

    def nth_prime(self, x):
        i=0
        counter=1
        while (i < x):
            counter += 1;
            if utils.is_prime(counter):
                i += 1;
        return counter

    def calculate_result(self, x):
        return self.nth_prime(x)


class SummationofPrimesView(InteractiveSolutionView):
    """
    Problem 10: Summation of Primes
    """

    def summation_of_primes(self, x):
        primes = [number for number in range(2, x) if utils.is_prime(number)]
        return sum(primes)

    def calculate_result(self, x):
        return self.summation_of_primes(x)


class PowerDigitSumView(InteractiveSolutionView):
    """
    Problem 16: Power Digit Sum
    """

    def power_digit_sum(self, x):
        """
        Given integer x, determines the sum of each individual digit in the number 2**x.
        """
        return utils.sum_digits_in_number(2**x)

    def calculate_result(self, x):
        return self.power_digit_sum(x)


class FactorialDigitSumView(InteractiveSolutionView):
    """
    Problem 20: Factorial Digit Sum
    """
    def factorial(self, x):
        if x == 0:
            return 1
        else:
            return x * self.factorial(x-1)

    def factorial_digit_sum(self, x):
        """
        Given integer x, determines the sum of each individual digit in the number x!.
        """
        # x_factorial = math.factorial(x)
        x_factorial = self.factorial(x)
        return utils.sum_digits_in_number(x_factorial)

    def calculate_result(self, x):
        return self.factorial_digit_sum(x)


class CircularPrimesView(InteractiveSolutionView):
    """
    Problem 35: Circular Primes
    """

    def circular_primes(self, x):
        """
        Determines the number of circular primes less than x.
        197 is a circular prime because each rotation (197, 971, 719) is prime.
        """
        count = 0
        for number in range(2, x): # else 0 and 1 will count
            num_as_str = str(number)
            for rotation in range(len(num_as_str)): # for each digit
                rotated = utils.rotate_list(num_as_str, rotation) # rotate
                if not utils.is_prime(int(rotated)):
                    break
            else: # no break statement encountered, this number is a circular prime
                count += 1

        return count

    def calculate_result(self, x):
        return self.circular_primes(x)


class DoubleBasePalindromesView(InteractiveSolutionView):
    """
    Problem 36: Double Base Palindromes
    """

    def double_base_palindromes(self, x):
        """
        Calculates the sum of all numbers less than x, that are palindromic in both base 10 and base 2.
        """
        # bin(x) results in a binary number prefaced with '0x', hence the slice 
        double_palindromes = [number for number in range(x) if utils.is_palindrome(number) and utils.is_palindrome(bin(number)[2:])]
        return sum(double_palindromes)

    def calculate_result(self, x):
        return self.double_base_palindromes(x)

