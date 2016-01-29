from django import template
from django.core.urlresolvers import reverse

from problems.models import Problem

register = template.Library()

@register.filter
def previous_url(problem):
    previous_number = problem.number - 1
    return reverse('euler_problem', kwargs={'problem_number': previous_number})

@register.filter
def next_url(problem):
    next_number = problem.number + 1
    return reverse('euler_problem', kwargs={'problem_number': next_number})

@register.filter
def random_solved_problem(num):
	return Problem.objects.filter(solved=True).order_by('?').first().number

@register.filter
def random_problem(num):
	return Problem.objects.order_by('?').first().number