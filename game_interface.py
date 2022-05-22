from tkinter import *
from PIL import ImageTk, Image
from game_brain import GameBrain
import time


THEME_COLOR = "green" #Color of the main window


class GameInterface:
    """Game Interface class includes on the graphic user interface elements that use TKinter to
    make a window with buttons to play Rock, Paper, Scissors against a computer infinite times"""
    def __init__(self, gamebrain):
        self.gamebrain = gamebrain
        """Create the main window"""
        self.root = Tk()
        self.root.title("ROCK, PAPER, SCISSORS")
        self.root.config(bg=THEME_COLOR, padx=20, pady=20)

        #self.root.iconbitmap("images/scissors.ico") #Include an .ico for an icon at the top of the window

        """Creating TKinter Photo objects to use in the window"""
        self.paper_img = ImageTk.PhotoImage(Image.open("images/paper.png"))
        self.rock_img = ImageTk.PhotoImage(Image.open("images/rock_1.png"))
        self.scissors_img = ImageTk.PhotoImage(Image.open("images/scissor_1.png"))
        self.thinking_img = ImageTk.PhotoImage(Image.open("images/thinking.png"))
        self.question_mark_img = ImageTk.PhotoImage(Image.open("images/question_mark.png"))

        """Creating buttons for the human to press to choose rock, paper, scissors"""
        self.button_paper = Button(image=self.paper_img, command=lambda: self.human_button_pushed("PAPER"))
        self.button_rock = Button(image=self.rock_img, command=lambda: self.human_button_pushed("ROCK"))
        self.button_scissors = Button(image=self.scissors_img, command=lambda: self.human_button_pushed("SCISSORS"))

        """Create labels where the text appears in the window"""
        self.title_label = Label(text="ROCK, PAPER, SCISSORS GAME", font=("Verdana", 30), bg=THEME_COLOR)
        self.title_label.grid(row=0, column=0, columnspan=3, padx=50, pady=50)

        """These .grid functions lay out the TKinter widgets in the window that were just instantiated"""
        self.button_rock.grid(row=1, column=0)
        self.button_paper.grid(row=2, column=0)
        self.button_scissors.grid(row=3, column=0)

        self.player_label = Label(text="YOU:", bg=THEME_COLOR)
        self.player_label.grid(row=1, column=1)

        self.comp_label = Label(text="COMPUTER:", bg=THEME_COLOR)
        self.comp_label.grid(row=1, column=2)

        self.human_choice_label = Label(image=self.question_mark_img)
        self.human_choice_label.grid(row=2, column=1)

        self.comp_choice_label = Label(image=self.question_mark_img)
        self.comp_choice_label.grid(row=2, column=2)

        self.label_message = Label(text="LET'S PLAY!", padx=50, pady=50, bg=THEME_COLOR, font=("Verdana", 20))
        self.label_message.grid(row=4, column=0, columnspan=4)

        self.label_winner = Label(text="", font=("Verdana", 20), bg=THEME_COLOR)
        self.label_winner.grid(row=5, column=0, columnspan=4)

        self.label_human_score = Label(text=f"HUMAN SCORE: {self.gamebrain.human_score}", bg=THEME_COLOR)
        self.label_human_score.grid(row=6, column=0)
        self.label_comp_score = Label(text=f"COMPUTER SCORE: {self.gamebrain.comp_score}", bg=THEME_COLOR)
        self.label_comp_score.grid(row=6, column=3)

        # self.label_timer = Label(text="3", bg="white", font=("Verdana", 15))
        # self.label_timer.grid(row=7, column=2, columnspan=2)

        self.quit_button = Button(text="Quit", command=self.root.quit)
        self.quit_button.grid(row=9, column=1, columnspan=1, padx=10)

        self.root.mainloop()

    def timer(self):
        """A function that can countdown to Rock, Paper, Scissors"""
        self.label_timer.config(text="3")
        time.sleep(1)
        self.label_timer.config(text="2")
        time.sleep(1)
        self.label_timer.config(text="1")
        time.sleep(1)
        self.label_timer.config(text="SHOOT!")
        time.sleep(1)
        self.label_timer.config(text="")



    def human_button_pushed(self, choice):
        """Human button pushed will launch the action when the human presses a button: rock, paper, scissors"""
        winner = self.gamebrain.get_winner(choice)

        self.label_winner.config(text=f"{winner} WINS!")
        self.label_message.config(text=f"{self.gamebrain.human_choice} VS {self.gamebrain.comp_choice}")

        #self.timer()
        time.sleep(0.5)

        """This changes the center picture of the human, based on the option selected"""
        if self.gamebrain.human_choice == "ROCK":
            self.human_choice_label.config(image=self.rock_img)
        elif self.gamebrain.human_choice == "PAPER":
            self.human_choice_label.config(image=self.paper_img)
        elif self.gamebrain.human_choice == "SCISSORS":
            self.human_choice_label.config(image=self.scissors_img)

        """This changes the center picture of the computer, based on the randomly generated computer choice"""
        if self.gamebrain.comp_choice == "ROCK":
            self.comp_choice_label.config(image=self.rock_img)
        elif self.gamebrain.comp_choice == "PAPER":
            self.comp_choice_label.config(image=self.paper_img)
        elif self.gamebrain.comp_choice == "SCISSORS":
            self.comp_choice_label.config(image=self.scissors_img)

        """This updates the window and shows the new scores"""
        if winner == "HUMAN":
            self.label_human_score.config(text=f"HUMAN SCORE: {self.gamebrain.human_score}", bg=THEME_COLOR)
        elif winner == "COMPUTER":
            self.label_comp_score.config(text=f"COMPUTER SCORE: {self.gamebrain.comp_score}", bg=THEME_COLOR)

