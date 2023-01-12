import tkinter as tk
from game_objects import Game, PlayerObject
from GUI_logic import GUI_Interface
from playsound import playsound


class GameApp(tk.Tk):
    """ GameApp initialises a game and a Tk instance (window)
    The window includes a title and sets up frames with the different views on the game
    The show_frame method unpacks all the frames except for the one that needs to be shown """

    def __init__(self):
        super().__init__()
        self.input_name = None
        self.game = create_game()

        title_string = ", ".join(obj.title() for obj in PlayerObject.allowable_objects)

        # Set the window title
        self.title(title_string)
        self.geometry("600x400")
        self.resizable(False, False)
        self.config(background="white")

        # Create an overall title and pack it into the top of the container
        title_label = tk.Label(self,
                               text=title_string,
                               bg="white",
                               fg="black",
                               width=600,
                               font=("Metropolis Extra Bold", 20),
                               )
        title_label.pack(side=tk.TOP, pady=40)

        # Create a dictionary of frames. The key identifies the frame and the value is an instance of the
        # frame object
        self.frames = {
            "menu_GUI": MenuGUI(self),
            "game_GUI": GameGUI(self)}

        # Show the GameOptionsGUI frame
        self.show_frame("menu_GUI")

    # Function to show the desired game class, which is a subclass of tk.Frame
    def show_frame(self, current_frame: str):
        widgets = self.winfo_children()
        # Forget all the existing frames
        for w in widgets:
            if w.winfo_class() == "Frame":
                w.pack_forget()

        if current_frame == "game_GUI":
            self.geometry("600x550")
        else:
            self.geometry("600x300")

        # Find and pack the current_frame
        frame_to_show = self.frames[current_frame]

        frame_to_show.pack(expand=True, fill=tk.BOTH)
        frame_to_show.set_up()


class MenuGUI(tk.Frame):
    def __init__(self, controller: GameApp):
        super().__init__()
        self.input_name = None
        self.controller = controller
        self.round_number = tk.StringVar()
        self.config(background="white")
        # This spreads out two columns in the available space with equal weight given to both columns
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.num_rounds_label = tk.Label(self, text="Number of Rounds", bg="white", font="Metropolis")
        self.num_rounds_value = tk.Entry(self,width=34)
        self.name_label = tk.Label(self, text="Name", bg="white", font="Metropolis")
        self.name_value = tk.Entry(self,width=34)

        self.next_frame_button = tk.Button(self, text="Start", font="Metropolis", command=self.next_frame, bg="#77afbf", fg="white", width=10)

        # This displays elements in grid layout
        self.name_label.grid(row=1, column=0, padx=55, pady=0, sticky="w")
        self.name_value.grid(row=1, column=1, padx=10, pady=0, sticky="w")
        self.num_rounds_label.grid(row=2, column=0, padx=55, pady=10, sticky="w")
        self.num_rounds_value.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.next_frame_button.grid(row=3, column=0, columnspan=3, padx=60, pady=0, sticky="w")

    def set_up(self):
        # Add code to set up variables for this frame. Note this refers to the game object stored on
        # the main app (the controller)
        self.round_number.set(self.controller.game.current_round)

    def next_frame(self):
        self.controller.frames["game_GUI"].logic.player0.name = self.name_value.get()
        self.controller.frames["game_GUI"].logic.set_max_rounds(int(self.num_rounds_value.get()))
        self.controller.show_frame("game_GUI")


class GameGUI(tk.Frame):
    def __init__(self, controller: GameApp):
        super().__init__()
        self.controller = controller
        self.config(background="white")
        self.config(width=600, height=1000)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.logic = GUI_Interface()

        self.rock_photo = tk.PhotoImage(file=r"images\rock.png")
        self.paper_photo = tk.PhotoImage(file=r"images\paper.png")
        self.scissors_photo = tk.PhotoImage(file=r"images\scissors.png")
        self.lizard_photo = tk.PhotoImage(file=r"images\lizard.png")
        self.spock_photo = tk.PhotoImage(file=r"images\spock.png")
        self.greyrock_photo = tk.PhotoImage(file=r"images\rockGrey.png")
        self.greypaper_photo = tk.PhotoImage(file=r"images\paperGrey.png")
        self.greyscissors_photo = tk.PhotoImage(file=r"images\scissorsGrey.png")
        self.greylizard_photo = tk.PhotoImage(file=r"images\lizardGrey.png")
        self.greyspock_photo = tk.PhotoImage(file=r"images\spockGrey.png")

        self.next_frame_button = tk.Button(self, text="Quit",
                                           command=self.next_frame, font="Metropolis")
        self.report_label = tk.Label(self, text="", bg="white", font="  Metropolis")
        self.round_label = tk.Label(self, text="Round 1", bg="white", font="Metropolis")

        # Functions that each button press will perform
        def display_score():
            self.report_label.config(
                text=self.logic.game.report_round() + f"\n\n{self.logic.player0.score} - {self.logic.player1.score}")

        def change_round():
            self.round_label.config(
                text=f"Round {self.logic.game.current_round}")

        self.user_option_buttons = (tk.Button(self, image=self.rock_photo, borderwidth=0, highlightthickness=0,
                                              command=lambda: [(self.logic.run_game("Rock")),
                                                               display_score(),
                                                               change_round()]),
                                    tk.Button(self, image=self.paper_photo, borderwidth=0, highlightthickness=0,
                                              command=lambda: [(self.logic.run_game("Paper")),
                                                               display_score(),
                                                               change_round()]),
                                    tk.Button(self, image=self.scissors_photo, borderwidth=0, highlightthickness=0,
                                              command=lambda: [(self.logic.run_game("Scissors")),
                                                               display_score(),
                                                               change_round()]),
                                    tk.Button(self, image=self.lizard_photo, borderwidth=0, highlightthickness=0,
                                              command=lambda: [(self.logic.run_game("Lizard")),
                                                               display_score(),
                                                               change_round()]),
                                    tk.Button(self, image=self.spock_photo, borderwidth=0, highlightthickness=0,
                                              command=lambda: [(self.logic.run_game("Spock")),
                                                               display_score(),
                                                               change_round()]))

        self.cpu_option_buttons = (tk.Label(self, image=self.greyrock_photo, borderwidth=0, highlightthickness=0),
                                   tk.Label(self, image=self.greypaper_photo, borderwidth=0, highlightthickness=0),
                                   tk.Label(self, image=self.greyscissors_photo, borderwidth=0, highlightthickness=0),
                                   tk.Label(self, image=self.greylizard_photo, borderwidth=0, highlightthickness=0),
                                   tk.Label(self, image=self.greyspock_photo, borderwidth=0, highlightthickness=0),
                                   )

        for i, btn in enumerate(self.user_option_buttons):
            btn.grid(row=i + 1, column=0, padx=10, pady=10)
        for i, btn in enumerate(self.cpu_option_buttons):
            btn.grid(row=i + 1, column=2, padx=10, pady=10)
        self.next_frame_button.grid(row=5, column=1, padx=10, pady=10)
        self.round_label.grid(row=2, column=1)
        self.report_label.grid(row=3, column=1)

    def set_up(self):
        # Add code to set up variables for this frame
        ...

    def option_button(self, option):
        print(f'You choose {option}')

    def next_frame(self):
        self.controller.show_frame("menu_GUI")
        self.logic.game.reset()
        self.round_label.config(text="Round 1")
        self.report_label.config(text="")


def create_game():
    game = Game()
    game.player = game.add_human_player()
    game.add_computer_player()

    return game


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
    print(app.frames["game_GUI"].logic.game.max_rounds)
    print(app.frames["game_GUI"].logic.game.current_round)
