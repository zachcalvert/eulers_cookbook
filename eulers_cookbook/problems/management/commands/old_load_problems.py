import json
import requests
from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand

from problems.models import Problem

class Command(BaseCommand):
    """
    Management command to scrape problem info from projecteuler.net into the db
    """
    def handle(self, *args, **options):
        for i in range(1,15):
            url = 'https://projecteuler.net/problem={}'.format(i)
            response = requests.get(url, verify=False)    

            soup = BeautifulSoup(response.text)    

            title_html = soup.find('h2')
            title = title_html.text    

            problem_html = soup.find('div', class_='problem_content')
            description = problem_html.text    

            print(url)

            problem, created = Problem.objects.get_or_create(
                number=i,
                title=title,
                description=description,
                link=url,
            )
            if created:
                try:
                    print('added problem {0}: {1}'.format(i, title))
                except UnicodeEncodeError:
                    print('added problem {}'.format(i))
