import random
import unittest
from Doubly_Linked_List_Seq import Doubly_Linked_List_Seq

def check(test, linked, expected):
    values, nodes = [], []
    previous = None
    node = linked.head
    while node is not None:
        test.assertIs(node.prev, previous)
        test.assertNotIn(id(node), nodes)
        nodes.append(id(node)); values.append(node.item)
        previous, node = node, node.next
    test.assertEqual(values, expected)
    test.assertIs(previous, linked.tail)
    backwards = []
    node = linked.tail
    while node is not None:
        backwards.append(node.item); node = node.prev
    test.assertEqual(backwards, expected[::-1])

class Oracle(unittest.TestCase):
    def test_random_operations_and_node_identity(self):
        rng = random.Random(6006)
        linked = Doubly_Linked_List_Seq(); expected = []
        for _ in range(1000):
            operation = rng.randrange(6)
            if not expected or operation == 0:
                value = rng.randrange(100); linked.insert_first(value); expected.insert(0,value)
            elif operation == 1:
                value = rng.randrange(100); linked.insert_last(value); expected.append(value)
            elif operation == 2:
                self.assertEqual(linked.delete_first(), expected.pop(0))
            elif operation == 3:
                self.assertEqual(linked.delete_last(), expected.pop())
            elif operation == 4:
                start = rng.randrange(len(expected)); end = rng.randrange(start,len(expected))
                first = linked.head.later_node(start); last = linked.head.later_node(end)
                removed = linked.remove(first,last)
                self.assertIs(removed.head,first); self.assertIs(removed.tail,last)
                check(self,removed,expected[start:end+1]); del expected[start:end+1]
            else:
                where = rng.randrange(len(expected)); node = linked.head.later_node(where)
                extra = Doubly_Linked_List_Seq(); extra.build([100,101,102]); first=extra.head
                linked.splice(node,extra); expected[where+1:where+1]=[100,101,102]
                self.assertIs(node.next,first); check(self,extra,[])
            check(self,linked,expected)
    def test_empty_errors_and_reuse(self):
        linked=Doubly_Linked_List_Seq()
        with self.assertRaises(IndexError): linked.delete_first()
        with self.assertRaises(IndexError): linked.delete_last()
        linked.insert_last(1); linked.delete_first(); linked.insert_first(2)
        check(self,linked,[2])
