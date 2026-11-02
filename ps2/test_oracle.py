import random
import unittest
from satisfying_booking import satisfying_booking

class Oracle(unittest.TestCase):
    def test_seeded_brute_force(self):
        rng=random.Random(6006)
        for _ in range(1000):
            requests=[]
            for _ in range(rng.randrange(30)):
                start=rng.randrange(20); end=rng.randrange(start+1,22)
                requests.append((start,end))
            result=satisfying_booking(tuple(requests))
            for time in range(22):
                expected=sum(start<=time<end for start,end in requests)
                self.assertEqual(sum(k for k,start,end in result if start<=time<end),expected)
            for index,(count,start,end) in enumerate(result):
                self.assertGreater(count,0); self.assertLess(start,end)
                if index:
                    previous=result[index-1]
                    self.assertLessEqual(previous[2],start)
                    self.assertFalse(previous[2]==start and previous[0]==count)
    def test_touches_duplicates_gaps_and_empty(self):
        self.assertEqual(satisfying_booking(((0,1),(1,2))),((1,0,2),))
        self.assertEqual(satisfying_booking(((0,1),(0,1),(3,4))),((2,0,1),(1,3,4)))
        self.assertEqual(satisfying_booking(()),())
