import builtins
import unittest
from unittest.mock import MagicMock
from src.player import *

class test_player(unittest.TestCase):

    # Mock : In this test, the python builtins function input() is mocked to provide suitable input
    #for the HumanPlayer() object to construct, and for the discard_card() method to act.
    def test_discard_card(self):
        builtins.input = MagicMock(side_effect =["Steve", "1"])

        player1 = HumanPlayer()
        player1.draw_card()
        player1.draw_card()
        player1.draw_card()
        discard_input = input()
        player1.discard_card(discard_input)

        self.assertEqual(2,len(player1.hand))

    # Fake/Double: The report_hand() function requires that a Player have a name. Humans take their names
    #from input, CPUs take their name randomly from a .csv file in resource. This Faked player object is
    # created with a fixed name to enable testing.
    def test_report_hand(self):
        player1 = TestPlayer()
        report_hand_output = player1.report_hand()
        self.assertEqual("Player Hamish The Fake holds: ['R4', 'R4']", report_hand_output)

    # Stub: Drawing cards involves a random element, therefore in order for the score_hand() method to be tested
    #a player object with stubbed hand attribute for the method to act on is required.
    def test_score_hand(self):
        player1 = TestPlayer()
        score_hand_output = player1.score_hand()
        self.assertEqual(148,score_hand_output)

