from game_objects import Game, PlayerObject, ComputerPlayer


# Set up class
class CLInterface:

    def __init__(self):

        self.game = Game()
        ...

    def set_up(self):

        self.game.add_human_player()
        self.game.add_computer_player()

        self.player0 = self.game.players[0]
        self.player1 = self.game.players[1]

        self.player0.name = input("\nName:\n")

    def input_max_rounds(self):

        input_rounds = input("\nRounds:\n")

        while not input_rounds.isdigit():
            print("[invalid input]")
            input_rounds = input("\nRounds:\n")

        self.game.set_max_rounds(int(input_rounds))

    def get_choices(self):

        choice = input("\nChoice:\n").lower()

        while choice not in self.game.allowable_objects:
            print("[invalid input]")
            choice = input("\nChoice:\n").lower()

        self.player0.choose_object(choice)
        self.player1.choose_object()


    def run_game(self):

        self.get_choices()
        self.game.find_winner()

        print(f"\n{self.game.report_round()}")
        print(f"\n{self.player0.name} {self.player0.score} - {self.player1.score} {self.player1.name}")


    def run_sequence(self):

        print("-- Rock Paper Scissors Lizard Spock --")

        self.set_up()
        self.game.reset()
        self.input_max_rounds()

        for turn in range(self.game.max_rounds):
            print("\n----------------------------------------")
            self.run_game()

        print("\n----------------------------------------\n")

        if self.player0.score > self.player1.score:
            print(f"WINNER: {self.player0.name}")
        elif self.player1.score > self.player0.score:
            print(f"WINNER: {self.player1.name}")
        else:
            print(f"WINNER: NO ONE")


if __name__ == "__main__":
    cli = CLInterface()
    cli.run_sequence()
