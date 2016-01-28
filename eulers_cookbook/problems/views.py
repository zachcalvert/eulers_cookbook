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

        paginator = Paginator(problems, 10)
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
    def calculate_result(self, number):
        return sum([i for i in range(number) if i % 3 == 0 or i % 5 == 0])   


