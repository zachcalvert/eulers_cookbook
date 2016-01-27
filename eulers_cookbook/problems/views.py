import json
from datetime import datetime

from django.shortcuts import get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.views.generic import TemplateView
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
    template_name = "problem.html"

    def get_context_data(self, *args, **kwargs):
        context = super(EulerProblemView, self).get_context_data(**kwargs)
        
        name = "solutions/{}.html".format(kwargs['problem_number'])
        try:
            get_template(name)
        except TemplateDoesNotExist:
            template_name = "problem.html" 

        problem = get_object_or_404(Problem, number=kwargs['problem_number'])    

        context['problem'] = problem

        return context

