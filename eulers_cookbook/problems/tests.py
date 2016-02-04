import json

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

import views


class MultiplesOfThreeAndFiveTest(TestCase):
    """
    Ensure that the Multiples of Three and Five problem works
    """

    def setUp(self):
        self.view = views.MultiplesOfThreeAndFiveView()

    def test_multiples_of_three_and_five(self):
        """
        The sum of all multiples of three and 5 less than 10 is 23 (given)
        """
        self.assertEqual(self.view.multiples_of_three_and_five(10), 23)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('multiples_of_three_and_five') + '?x=10'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 10)
        self.assertEqual(response_data['value'], 23)


class EvenFibonacciNumbersTest(TestCase):
    """
    Ensure that the Even Fibonacci Numbers problem works
    """

    def setUp(self):
        self.view = views.EvenFibonacciNumbersView()

    def test_even_fibonacci_numbers(self):
        """
        The first 10 terms less than 100 are 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 (given)
        therefore the sum of the even valued terms will be equal to 2 + 8 + 34
        """
        self.assertEqual(self.view.even_fibonacci_numbers(100), 2+8+34)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('even_fibonacci_numbers') + '?x=100'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 100)
        self.assertEqual(response_data['value'], 2+8+34)


class LargestPrimeFactorTest(TestCase):
    """
    Ensure that the Largest Prime Factor problem works
    """

    def setUp(self):
        self.view = views.LargestPrimeFactorView()

    def test_largest_prime_factor(self):
        """
        The largest prime factor of 13195 is 29 (given)
        """
        self.assertEqual(self.view.largest_prime_factor(13195), 29)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('largest_prime_factor') + '?x=13195'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 13195)
        self.assertEqual(response_data['value'], 29)


class LargestPalindromeProductTest(TestCase):
    """
    Ensure that the Largest Palindrome Product problem works
    """

    def setUp(self):
        self.view = views.LargestPalindromeProductView()

    def test_largest_prime_factor(self):
        """
        The largest palindrome product of any two two digit numbers is 9009 (given)
        """
        self.assertEqual(self.view.largest_palindrome_product(10, 99), 9009)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('largest_palindrome_product') + '?x=10&y=99'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 10)
        self.assertEqual(int(response_data['y']), 99)
        self.assertEqual(response_data['value'], 9009)


class SumSquareDifferenceTest(TestCase):
    """
    Ensure that the Sum Square Difference problem works
    """

    def setUp(self):
        self.view = views.SumSquareDifferenceView()    

    def test_square_of_sums(self):
        """
        The sum of the squares of the first 10 natural numbers is 3025 (given)
        """
        self.assertEqual(self.view.square_of_sums(10), 3025)    
    
    def test_sum_of_squares(self):
        """
        The sum of the squares of the first 10 natural numbers is 385 (given)
        """
        self.assertEqual(self.view.sum_of_squares(10), 385)    

    def test_calculate_result(self):
        """
        The calculated difference between the above functions with input 10 is 2640 (given)
        """
        self.assertEqual(self.view.calculate_result(10), 2640)

    def test_interactive_endpoint(self):
        """
        Verify that the ineteractive url works correctly
        """
        client = Client()
        url = reverse('sum_square_difference') + '?x=10'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 10)
        self.assertEqual(response_data['value'], 2640)





