import unittest
from unittest.mock import MagicMock
from src.player import *

class test_player(unittest.TestCase):



    # Mock :
    def test_discard_card(self):

        player1 = HumanPlayer("Steve")
        player1.draw_card()
        player1.draw_card()
        player1.draw_card()
        player1.discard_card(1)

        self.assertEqual(1,2)

    # Fake/Double:
    def test_report_hand(self):
        player1 = TestPlayer()
        report_hand_output = player1.report_hand()
        self.assertEqual("Player Hamish The Fake holds: ['R4', 'R4']", report_hand_output)

    # Stub:
    def test_score_hand(self):
        player1 = TestPlayer()
        score_hand_output = player1.score_hand()
        self.assertEqual(148,score_hand_output)

