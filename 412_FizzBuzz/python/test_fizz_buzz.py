import fizz_buzz
import time
import unittest


class TestFizzBuzzSolution1(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()*1000.0
        self.fb = fizz_buzz.Solution1()

    def tearDown(self):
        elapsed = time.time()*1000.0 - self._started_at
        print('{} ({}ms)'.format(self.id(), round(elapsed*1000)))

    def test_with_three(self):
        self.assertListEqual(self.fb.fizzBuzz(n=3),
                             ['1', '2', 'Fizz'],
                             "Using '3' as input is not working...")

    def test_with_five(self):
        self.assertListEqual(self.fb.fizzBuzz(n=5),
                             ['1', '2', 'Fizz', '4', 'Buzz'],
                             "Using '5' as input is not working...")

    def test_with_fifteen(self):
        self.assertListEqual(self.fb.fizzBuzz(n=15),
                             ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'],
                             "Using '15' as input is not working...")


class TestFizzBuzzSolution2(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()*1000.0
        self.fb = fizz_buzz.Solution2()

    def tearDown(self):
        elapsed = time.time()*1000.0 - self._started_at
        print('{} ({}ms)'.format(self.id(), round(elapsed*1000)))

    def test_with_three(self):
        self.assertListEqual(self.fb.fizzBuzz(n=3),
                             ['1', '2', 'Fizz'],
                             "Using '3' as input is not working...")

    def test_with_five(self):
        self.assertListEqual(self.fb.fizzBuzz(n=5),
                             ['1', '2', 'Fizz', '4', 'Buzz'],
                             "Using '5' as input is not working...")

    def test_with_fifteen(self):
        self.assertListEqual(self.fb.fizzBuzz(n=15),
                             ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'],
                             "Using '15' as input is not working...")


class TestFizzBuzzSolution3(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()*1000.0
        self.fb = fizz_buzz.Solution2()

    def tearDown(self):
        elapsed = time.time()*1000.0 - self._started_at
        print('{} ({}ms)'.format(self.id(), round(elapsed*1000)))

    def test_with_three(self):
        self.assertListEqual(self.fb.fizzBuzz(n=3),
                             ['1', '2', 'Fizz'],
                             "Using '3' as input is not working...")

    def test_with_five(self):
        self.assertListEqual(self.fb.fizzBuzz(n=5),
                             ['1', '2', 'Fizz', '4', 'Buzz'],
                             "Using '5' as input is not working...")

    def test_with_fifteen(self):
        self.assertListEqual(self.fb.fizzBuzz(n=15),
                             ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz'],
                             "Using '15' as input is not working...")


if __name__ == "__main__":
    unittest.main()
