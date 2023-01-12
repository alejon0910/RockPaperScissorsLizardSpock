from game_objects import Game, PlayerObject, ComputerPlayer
from playsound import playsound
import time


# Set up class
class GUI_Interface:

    def __init__(self):

        self.game = Game()
        self.game.add_human_player()
        self.game.add_computer_player()
        self.player0 = self.game.players[0]
        self.player1 = self.game.players[1]
        self.clicked = None

    def set_max_rounds(self, rounds):
        self.game.set_max_rounds(rounds)

    def run_game(self, choice):

        if self.game.current_round < self.game.max_rounds:
            self.player0.choose_object(choice)
            self.player1.choose_object()

            self.game.find_winner()

            if self.game.round_result == "win":
                playsound(r"sounds\win.wav")
            elif self.game.round_result == "lose":
                playsound(r"sounds\lose.wav")
            else:
                playsound(r"sounds\tie.wav")

            print(f"\n{self.game.report_round()}")
            print(f"\n{self.player0.name} {self.player0.score} - {self.player1.score} {self.player1.name}")
            self.game.current_round += 1

    def display_winner(self):

        if self.player0.score > self.player1.score:
            return f"WINNER: {self.player0.name}"
        elif self.player1.score > self.player0.score:
            return f"WINNER: {self.player1.name}"
        else:
            return f"WINNER: NO ONE"
