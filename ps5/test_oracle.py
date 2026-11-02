import unittest
from solve_tilt import solve_tilt, move

class Edges(unittest.TestCase):
    def test_already_solved_and_impossible(self):
        self.assertEqual(solve_tilt((('o','.'),('.','.')),(0,0)),[])
        self.assertIsNone(solve_tilt((('o','#'),('#','.')),(1,1)))
    def test_one_ball_all_open_targets(self):
        board=(('o','.','.'),('.','.','.'),('.','.','.'))
        for target, distance in [((0,0),0),((2,0),1),((0,2),1),((2,2),2)]:
            actions=solve_tilt(board,target)
            self.assertEqual(len(actions),distance)
            result=board
            for action in actions:result=move(result,action)
            self.assertEqual(result[target[1]][target[0]],'o')
        self.assertIsNone(solve_tilt(board,(1,1)))
