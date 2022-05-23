from src.ReadCSVFile import ReadCSVFile
import random

class Player():

    def __init__(self,name):
        self.name = name
        self.hand = []
        self.score = 0

    def draw_card(self):
        card_color = ["G","R","B","Y"]
        card_value = ["1","2","3","4","5"]
        new_card = str(card_color[random.randrange(0,4)] + card_value[random.randrange(0,5)])
        self.hand.append(new_card)


    def report_hand(self):
        #needs to return a string with player name
        report_string = "Player " + self.name + " holds: " + str(self.hand)
        return report_string

    def discard_card(self):
        self.hand.pop()


    def score_hand(self):
        score = 0
        if self.hand[0][0] == self.hand[1][0]:
            score += 40
        if self.hand[0][1] == self.hand[1][1]:
            score += 100
        score += int(self.hand[0][1])
        score += int(self.hand[1][1])
        return score


class HumanPlayer(Player):

    def __init__(self):
        self.name = input("Please enter your name: ")
        self.hand = []
        self.score = 0

    def discard_card(self,discard):

        try:
            index_adjustment = int(discard) - 1
            self.hand.pop(index_adjustment)
        except:
            print("Unable to discard. Likely invalid input.")


class CPUPlayer(Player):
    def __init__(self):
        read_csv_file = ReadCSVFile()
        names = read_csv_file.get_file_data("names.csv")
        self.name = names[0][random.randrange(0,5)]
        self.hand = []
        self.score = 0


class TestPlayer(Player):
    def __init__(self):
        self.name = "Hamish The Fake"
        self.hand = ["R4", "R4"]
        self.score = 0
