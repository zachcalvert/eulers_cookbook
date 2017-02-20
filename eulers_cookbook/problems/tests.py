import json

from django.core.urlresolvers import reverse
from django.test import TestCase, Client

from problems import utils, views


class TestUtils(TestCase):
    """
    Test the functions defined in utils.py
    """
    
    def test_is_prime(self):
        """
        Ensure that the is_prime utility function works.
        """
        self.assertTrue(utils.is_prime(2))
        self.assertTrue(utils.is_prime(3))
        self.assertTrue(utils.is_prime(29))

        self.assertFalse(utils.is_prime(4))
        self.assertFalse(utils.is_prime(9))
        self.assertFalse(utils.is_prime(56))

    def test_is_palindrome(self):
        """
        Ensure that the is_palindrome utility function works.
        """
        self.assertTrue(utils.is_palindrome('racecar'))
        self.assertTrue(utils.is_palindrome('euston saw I was notsue'))
        self.assertTrue(utils.is_palindrome(123454321))

        self.assertFalse(utils.is_palindrome('racecars'))
        self.assertFalse(utils.is_palindrome('Euston saw I was not Suzanne'))
        self.assertFalse(utils.is_palindrome(1234544321))


class MultiplesOfThreeAndFiveTest(TestCase):
    """
    Ensure that the Multiples of Three and Five problem works
    """

    def setUp(self):
        self.view = views.MultiplesOfThreeAndFiveView()

    def test_multiples_of_three_and_five(self):
        """
        The sum of all multiples of three and 5 less than 10 is 23 (given in problem statement)
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
        The first 10 terms less than 100 are 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 (given in problem statement)
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
        The largest prime factor of 13195 is 29 (given in problem statement)
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
        The largest palindrome product of any two two digit numbers is 9009 (given in problem statement)
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
        self.assertEqual(response_data['y'], 99)
        self.assertEqual(response_data['value'], 9009)


class SmallestMultipleTest(TestCase):
    """
    Ensure that the Smallest Multiple problem works
    """

    def setUp(self):
        self.view = views.SmallestMultipleView()    

    def test_smallest_multiple(self):
        """
        the lcm of 4 and 5 is 20 
        """
        self.assertEqual(self.view.smallest_multiple(4, 5), 20)
        """
        the lcm of 4 and 10 is 20
        """
        self.assertEqual(self.view.smallest_multiple(4, 10), 20)

    def test_calculate_result(self):
        """
        The smallest multiple for the range of numbers from 1 to 10 is 2520 (given in problem statement)
        """
        self.assertEqual(self.view.calculate_result(1,10), 2520)


class SumSquareDifferenceTest(TestCase):
    """
    Ensure that the Sum Square Difference problem works
    """

    def setUp(self):
        self.view = views.SumSquareDifferenceView()    

    def test_square_of_sums(self):
        """
        The sum of the squares of the first 10 natural numbers is 3025 (given in problem statement)
        """
        self.assertEqual(self.view.square_of_sums(10), 3025)    
    
    def test_sum_of_squares(self):
        """
        The sum of the squares of the first 10 natural numbers is 385 (given in problem statement)
        """
        self.assertEqual(self.view.sum_of_squares(10), 385)    

    def test_calculate_result(self):
        """
        The calculated difference between the above functions with input 10 is 2640 (given in problem statement)
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


class TenThousandAndFirstPrimeTest(TestCase):
    """
    Ensure that the Ten Thousand and First Prime Number problem works
    """

    def setUp(self):
        self.view = views.TenThousandAndFirstPrimeView()

    def test_nth_prime(self):
        """
        The 6th prime is 13 (given in problem statement)
        """
        self.assertEqual(self.view.nth_prime(6), 13)

    def test_interactive_endpoint(self):
        """
        Verify that the ineteractive url works correctly
        """
        client = Client()
        url = reverse('10001st_prime') + '?x=6'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 6)
        self.assertEqual(response_data['value'], 13)


class SummationofPrimesTest(TestCase):
    """
    Ensure that the Summation of Primes problem works.
    """

    def setUp(self):
        self.view = views.SummationofPrimesView()

    def test_summation_of_primes(self):
        """
        The sum of the primes below 10 is 17 (given in problem statement)
        """
        self.assertEqual(self.view.summation_of_primes(10), 17)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('summation_of_primes') + '?x=10'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 10)
        self.assertEqual(response_data['value'], 17)


class FactorialDigitSumTest(TestCase):
    """
    Ensure that the Factorial Digit Sum problem works.
    """

    def setUp(self):
        self.view = views.FactorialDigitSumView()

    def test_factorial_digit_sum(self):
        """
        The sum of the digits in 10 factorial is 27 (given in problem statement.)
        """
        self.assertEqual(self.view.factorial_digit_sum(10), 27)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('factorial_digit_sum') + '?x=10'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 10)
        self.assertEqual(response_data['value'], 27)


class PowerDigitSumTest(TestCase):
    """
    Ensure that the Power Digit Sum problem works.
    """

    def setUp(self):
        self.view = views.PowerDigitSumView()

    def test_power_digit_sum(self):
        """
        The sum of the digits in 2^15 is 26 (given in problem statement)
        """
        self.assertEqual(self.view.power_digit_sum(15), 26)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('power_digit_sum') + '?x=15'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 15)
        self.assertEqual(response_data['value'], 26)


class CircularPrimesTest(TestCase):
    """
    Ensure that the Circular Primes problem works.
    """

    def setUp(self):
        self.view = views.CircularPrimesView()

    def test_double_base_palindromes(self):
        """
        The sum of the double base palindromes less than 100 is 13 (given in problem statement)
        """
        self.assertEqual(self.view.circular_primes(100), 13)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('circular_primes') + '?x=100'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 100)
        self.assertEqual(response_data['value'], 13)


class DoubleBasePalindomesTest(TestCase):
    """
    Ensure that the Double Base Palindromes problem works.
    """

    def setUp(self):
        self.view = views.DoubleBasePalindromesView()

    def test_double_base_palindromes(self):
        """
        The sum of the double base palindromes less than 1 million is 872187 (verified on project euler)
        """
        self.assertEqual(self.view.double_base_palindromes(1000000), 872187)

    def test_interactive_endpoint(self):
        """
        Verify that the interactive url works correctly
        """
        client = Client()
        url = reverse('double_base_palindromes') + '?x=1000000'
        response = client.get(url)

        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        self.assertEqual(response_data['x'], 1000000)
        self.assertEqual(response_data['value'], 872187)


