import nostrtz
import time
import unittest


class Test_nostrtz1(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()*1000.0
        self.nostrtz = nostrtz.Solution1()

    def tearDown(self):
        elapsed = time.time()*1000.0 - self._started_at
        print('{} ({}ms)'.format(self.id(), round(elapsed*1000)))

    def test_with_fourteen(self):
        self.assertEqual(self.nostrtz.num_of_steps(num=14),
                         6,
                         "Incorrect number of steps for 14")

    def test_with_eight(self):
        self.assertEqual(self.nostrtz.num_of_steps(num=8),
                         4,
                         "Incorrect number of stesp for 8")

    def test_with_123(self):
        self.assertEqual(self.nostrtz.num_of_steps(num=123),
                         12,
                         "Incorrect number of steps for 123")

    def test_with_9000(self):
        self.assertEqual(self.nostrtz.num_of_steps(num=9000),
                         18,
                         "Incorrect number of steps for 9000")


class Test_nostrtz2(unittest.TestCase):

    def setUp(self):
        self._started_at = time.time()*1000.0
        self.nostrtz = nostrtz.Solution2()

    def tearDown(self):
        elapsed = time.time()*1000.0 - self._started_at
        print('{} ({}ms)'.format(self.id(), round(elapsed*1000)))

    def test_with_fourteen(self):
        self.assertEqual(self.nostrtz.num_of_steps(num=14),
                         6,
                         "Incorrect number of steps for 14")

    def test_with_eight(self):
        self.assertEqual(self.nostrtz.num_of_steps(num=8),
                         4,
                         "Incorrect number of stesp for 8")

    def test_with_123(self):
        self.assertEqual(self.nostrtz.num_of_steps(num=123),
                         12,
                         "Incorrect number of steps for 123")

    def test_with_9000(self):
        self.assertEqual(self.nostrtz.num_of_steps(num=9000),
                         18,
                         "Incorrect number of steps for 9000")


"""
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
"""

if __name__ == "__main__":
    unittest.main()
