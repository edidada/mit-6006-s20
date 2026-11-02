import itertools
import random
import unittest
from short_company import short_company


def valid_sequences(prices, k):
    for mask in range(1 << len(prices)):
        indices = [i for i in range(len(prices)) if mask >> i & 1]
        if all(prices[a] > prices[b] and b // k - a // k <= 1
               for a, b in zip(indices, indices[1:])):
            yield tuple(prices[i] for i in indices)


class OracleTests(unittest.TestCase):
    def test_random_exhaustive_subsets(self):
        rng = random.Random(6007)
        for _ in range(350):
            n, k = rng.randint(1, 4), rng.randint(1, 3)
            companies = ('A', 'B')
            prices = tuple(tuple(rng.randint(1, 8) for _ in range(n*k))
                           for _ in companies)
            feasible = [set(valid_sequences(p, k)) for p in prices]
            expected = max(len(s) for f in feasible for s in f)
            company, sequence = short_company(companies, prices, n, k)
            self.assertEqual(len(sequence), expected)
            self.assertIn(tuple(sequence), feasible[companies.index(company)])

    def test_skipped_day_and_late_start(self):
        self.assertEqual(len(short_company(('A',), ((9, 10, 8),), 3, 1)[1]), 2)
        self.assertEqual(short_company(('A',), ((1, 9, 8, 7),), 4, 1),
                         ('A', [9, 8, 7]))
