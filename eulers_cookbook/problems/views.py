import json
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic import TemplateView, View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from problems.models import Problem


class HomePageView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        
        problems = Problem.objects.all()    

        paginator = Paginator(problems, 50)
        page = self.request.GET.get('page')    

        try:
            problems = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            problems = paginator.page(1)
        except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
            problems = paginator.page(paginator.num_pages)    

        context['paginator'] = paginator
        context['problems'] = problems

        return context


class EulerProblemView(TemplateView):
    template_name = 'problem.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EulerProblemView, self).get_context_data(**kwargs)

        problem = get_object_or_404(Problem, number=kwargs['problem_number'])    

        context['problem'] = problem

        return context


class InteractiveCallbackView(View):

    def get_current_time(self):
        now = datetime.now()
        return now.strftime('%m-%d %H:%M:%S')

    def get(self, request):
        number = request.GET.get('number', None)    

        # ensure a value is provided
        if not number:
            return HttpResponse('Please provide a value.', status=400)    

        # ensure the value is an integer
        try:
            number = int(number)
        except ValueError:
            return HttpResponse('Please provide an integer value.', status=400)

        value = self.calculate_result(number) 

        content = {
            'number': number,
            'value': value,
            'last_requested': self.get_current_time()
        }

        return HttpResponse(json.dumps(content))


class ProblemOneView(InteractiveCallbackView):
    """
    Problem 1: Multiples of Three and Five
    """
    def calculate_result(self, n):
        return sum([i for i in range(n) if i % 3 == 0 or i % 5 == 0])


class ProblemTwoView(InteractiveCallbackView):
    """
    Problem 2: Even Fibonacci Numbers
    """
    def calculate_result(self, n):
        a, b = 1, 1
        total = 0
        while a <= n:
            if a % 2 == 0:
                total += a
            a, b = b, a+b
        return total


class ProblemThreeView(InteractiveCallbackView):
    """
    Problem 3: Largest Prime Factor
    """
    def calculate_result(self, n):
        i = 2
        while i * i < n:
            while n % i == 0:
                n = n / i
            i = i + 1    
        return n


class ProblemSixView(InteractiveCallbackView):
    """
    Problem 6: Sum Square Difference
    """  

    def square_of_sums(self, n):
        return sum([ i for i in xrange(1, n + 1) ]) ** 2

    def sum_of_squares(self, n):
        return sum([ i * i for i in xrange(1, n + 1) ])  

    def calculate_result(self, n):
        """
        Problem 4: Largest Palidrome Product
        """
        return self.square_of_sums(n) - self.sum_of_squares(n)    

