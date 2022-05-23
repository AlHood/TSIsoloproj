from src.player import *


class Main:
    def main():
        active_game = True
        player_name = ""

        #a series of operations for the player class

        #hello
        #ask the
        print("Hello, welcome to a simple card drawing and matching game.")
        player_name = input("Please enter your name: ")

        while active_game:
            #Initialization of new round
            player1 = HumanPlayer(player_name)
            player2 = CPUPlayer()

            #Players are dealt 3 cards
            player1.draw_card()
            player1.draw_card()
            player1.draw_card()
            player2.draw_card()
            player2.draw_card()
            player2.draw_card()

            #Starting state
            print(player1.report_hand())
            print(player2.report_hand())

            #Discard round - each player discards 1 card
            discard_input = input("Please enter the number of the card in your hand you wish to discard: ")
            player1.discard_card(discard_input)
            player2.discard_card()

            print(player1.report_hand())
            print(player2.report_hand())

            #Scoring round
            if player1.score_hand() > player2.score_hand():
                print("You have won this round with a score of: " + str(player1.score_hand()) + "\n")
            elif player2.score_hand() > player1.score_hand():
                print("The CPU player has won this round with a score of: " + str(player2.score_hand()) + "\n")
            else:
                print("There is no winner.\n")




            if input("Please enter q to quit, or any other input to play another round: ") == "q":
                active_game = False



        #while loop containing single turn

        pass


if __name__ == '__main__':
    Main.main()

