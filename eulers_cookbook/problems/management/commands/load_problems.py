import json
import requests

from django.core.management.base import BaseCommand

from problems.models import Problem

class Command(BaseCommand):
    """
    Management command to load problem data from eulerscookbook.org
    """
    def handle(self, *args, **options):
        for i in range(1,510):
            url = 'http://eulerscookbook.org/api/{}/'.format(i)
            print(url)
            response = requests.get(url, verify=False)    
            
            response_data = json.loads(response.content)

            problem, created = Problem.objects.get_or_create(number=i, title=response_data['title'])

            if created:
                try:
                    print('added problem {0}: {1}'.format(i, title))
                except UnicodeEncodeError:
                    print('added problem {}'.format(i))

            problem.description = response_data['description']
            problem.link = response_data['euler_link']
            problem.solved = response_data['solved']
            problem.num_inputs = response_data['num_inputs']
            problem.callback_function = response_data['callback_function']
            problem.output_column_header = response_data['output_column_header']

            problem.save()