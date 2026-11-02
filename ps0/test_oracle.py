import itertools
import unittest
from count_long_subarray import count_long_subarray

class Oracle(unittest.TestCase):
    def test_exhaustive_small_sequences(self):
        for length in range(8):
            for sequence in itertools.product(range(3), repeat=length):
                sizes = [end-start for start in range(length)
                         for end in range(start+1,length+1)
                         if all(sequence[i]<sequence[i+1] for i in range(start,end-1))]
                expected = sizes.count(max(sizes)) if sizes else 0
                self.assertEqual(count_long_subarray(sequence),expected,sequence)
    def test_large_monotone_and_constant(self):
        self.assertEqual(count_long_subarray(tuple(range(100000))),1)
        self.assertEqual(count_long_subarray((5,)*100000),100000)
