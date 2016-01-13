import unittest
from exercises.iterators import Cubes, Primes, Fibonacci, Alphabet, Permutations, LookAndSay
import json


class IteratorTests(unittest.TestCase):

    def test_cubes(self):
        c = iter(Cubes())
        for i in range(1, 1001):
            self.assertEqual(next(c), i ** 3)

    def test_primes(self):
        with open('tests/data_primes.json') as file:
            data = json.load(file)

        p = iter(Primes())
        for prime in data:
            self.assertEqual(next(p), prime)

    def test_fibonacci(self):
        with open('tests/data_fibonacci.json') as file:
            data = json.load(file)

        f = iter(Fibonacci())
        for fibonacci in data:
            self.assertEqual(next(f), fibonacci)

    def test_alphabet(self):
        data = ['Alef', 'Bet', 'Gimel', 'Dalet', 'He', 'Vav', 'Zayin', 'Het',
                'Tet', 'Yod', 'Kaf', 'Lamed', 'Mem', 'Nun', 'Samekh', 'Ayin',
                'Pe', 'Tsadi', 'Qof', 'Resh', 'Shin', 'Tav']

        a = iter(Alphabet())
        for alpha in data:
            self.assertEqual(next(a), alpha)
        self.assertRaises(StopIteration, next, a)

    @unittest.skip
    def test_permutations(self):
        pass

    @unittest.skip
    def test_lookandsay(self):
        pass
