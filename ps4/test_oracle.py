import random
import unittest
from tastiest_slice import tastiest_slice, Part_B_Tree, Key_Val_Item

class Oracle(unittest.TestCase):
    def test_random_weighted_quadrants(self):
        rng=random.Random(6006)
        for _ in range(500):
            points=[(rng.randrange(-5,6),rng.randrange(-5,6),rng.randrange(-10,11)) for _ in range(rng.randrange(30))]
            x,y,total=tastiest_slice(points)
            expected=max([0]+[sum(w for px,py,w in points if px<=a and py<=b) for a in {p[0] for p in points} for b in {p[1] for p in points}])
            self.assertEqual(total,expected)
            if total>0:self.assertEqual(sum(w for px,py,w in points if px<=x and py<=y),total)
    def test_augmentation_through_rotations(self):
        rng=random.Random(4);tree=Part_B_Tree();expected={}
        for key in rng.sample(range(300),300):
            value=rng.randrange(-10,11);tree.insert(Key_Val_Item(key,value));expected[key]=value
            running=best=0
            for k in sorted(expected):running+=expected[k];best=max(best,running)
            self.assertEqual(tree.max_prefix()[1],best)
