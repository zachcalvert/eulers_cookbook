from django.db import models
from django.core.urlresolvers import reverse

class Problem(models.Model):
    number = models.IntegerField(default=1)
    title = models.CharField(max_length=60)
    description = models.CharField(max_length=600)
    link = models.URLField(help_text="URL on Project Euler")
    solved = models.BooleanField(default=False)
    solution = models.CharField(max_length=800, null=True, blank=True) 
    num_inputs = models.IntegerField(default=1)

    # reverses in urls.py
    callback_function = models.CharField(max_length=100, null=True, blank=True)  
    
    output_column_header = models.CharField(max_length=80, null=True, blank=True)

    def get_absolute_url(self):
        return reverse('euler_problem', kwargs={'problem_number': self.number})

    def __unicode__(self):
        return '#{0}: {1}'.format(self.number, self.title)