import random
import unittest
from johnson import johnson, INF

def floyd(n,edges):
    d=[[float('inf')]*n for _ in range(n)]
    for i in range(n):d[i][i]=0
    for u,v,w in edges:d[u][v]=min(d[u][v],w)
    for k in range(n):
        for i in range(n):
            for j in range(n):d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    if any(d[i][i]<0 for i in range(n)):return None
    return tuple(tuple(INF if x==float('inf') else x for x in row) for row in d)

class Oracle(unittest.TestCase):
    def test_random_graphs(self):
        rng=random.Random(6006)
        for _ in range(500):
            n=rng.randrange(1,9)
            edges=[(u,v,rng.randrange(-5,16)) for u in range(n) for v in range(n) if rng.random()<0.2]
            self.assertEqual(johnson(n,tuple(edges)),floyd(n,edges))
    def test_disconnected_negative_cycle_and_parallel_edges(self):
        self.assertIsNone(johnson(4,((2,3,-2),(3,2,1))))
        self.assertEqual(johnson(2,((0,1,7),(0,1,-3))),((0,-3),(INF,0)))
        self.assertEqual(johnson(0,()),())
