import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../source')))
from janken_judge import judge

class TestJankenJudge(unittest.TestCase):
    def test_draw_cases(self):
        hands = ["グー", "チョキ", "パー"]
        for hand in hands:
            with self.subTest(hand=hand):
                result = judge(hand, hand)
                self.assertEqual(result, 'draw')

    def test_player_win_cases(self):
        win_cases = [
            ("チョキ", "グー"),
            ("パー", "チョキ"),
            ("グー", "パー")
        ]
        for comp_hand, player_hand in win_cases:
            with self.subTest(comp=comp_hand, player=player_hand):
                result = judge(comp_hand, player_hand)
                self.assertEqual(result, 'player_win')

    def test_computer_win_cases(self):
        lose_cases = [
            ("グー", "チョキ"),
            ("チョキ", "パー"),
            ("パー", "グー")
        ]
        for comp_hand, player_hand in lose_cases:
            with self.subTest(comp=comp_hand, player=player_hand):
                result = judge(comp_hand, player_hand)
                self.assertEqual(result, 'computer_win')