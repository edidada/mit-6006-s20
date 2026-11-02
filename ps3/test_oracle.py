import itertools
import unittest
from collections import Counter
from count_anagram_substrings import count_anagram_substrings

class Oracle(unittest.TestCase):
    def test_exhaustive_windows(self):
        for size in range(7):
            for chars in itertools.product('ab',repeat=size):
                text=''.join(chars)
                for width in range(4):
                    patterns=tuple(''.join(p) for p in itertools.product('ab',repeat=width))
                    expected=tuple(sum(Counter(text[i:i+width])==Counter(p) for i in range(max(0,len(text)-width+1))) for p in patterns)
                    self.assertEqual(count_anagram_substrings(text,patterns),expected)
    def test_duplicates_unicode_and_missing_characters(self):
        self.assertEqual(count_anagram_substrings('猫狗猫',('猫狗','狗猫','猫猫','鱼猫')),(2,2,0,0))
        self.assertEqual(count_anagram_substrings('aaaa',('aa','aa')),(3,3))
        self.assertEqual(count_anagram_substrings('abc',()),())
