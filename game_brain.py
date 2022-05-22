import random

user_choices = ["ROCK", "PAPER", "SCISSORS"]


class GameBrain:
    """A class the contains the game operations of Rock, Paper, Scissors"""
    def __init__(self):
        self.human_score = 0
        self.comp_score = 0
        self.human_name = "Human"
        self.comp_name = "Computer"
        self.human_choice = ""
        self.comp_choice = ""

    def get_human_name(self):
        #Returns the name of the human user
        self.human_name = input("What is your name? ")

    def set_human_name(self, name):
        #Use to set the name of the human player
        self.human_name = name

    def show_scores(self):
        #You can show the score of the human and the computer to the terminal
        print(self.human_name, " Score: ", self.human_score)
        print(self.comp_name, " Score: ", self.comp_score)

    def increment_human_score(self):
        #Increase the human score by 1 point
        self.human_score += 1

    def increment_comp_score(self):
        #Increase the computer score by 1 point
        self.comp_score += 1

    def set_rounds(self, rounds):
        #Use to set the total rounds of rock, paper, scissors
        self.total_rounds = rounds

    def get_human_choice(self, human_user):
        #Use this to get the human choice of rock, paper, scissors from the terminal
        print("Welcome to ROCK, PAPER, SCISSORS")
        human_choice = input("What do you choose? 1) Rock 2) Paper 3) Scissors :  ")
        human_choice = user_choices[int(human_choice) - 1]
        return human_choice

    def get_computer_choice(self):
        #Generate the computer's choice of rock, paper, and scissors with the random manual
        comp_choice = random.choice(user_choices)
        return comp_choice

    def get_winner(self, human_choice):
        #Send in the human choice of rock, paper, or scissors--get the computer's choice--
        # and then return who wins: NOBODY, HUMAN, or COMPUTER
        self.human_choice = human_choice
        self.comp_choice = self.get_computer_choice()
        comp_choice = self.comp_choice
        if human_choice == comp_choice:
            return("NOBODY")
        elif (human_choice == "PAPER" and comp_choice == "ROCK") or (human_choice == "SCISSORS"
                and comp_choice == "PAPER") or (human_choice == 'ROCK' and comp_choice == "SCISSORS"):
            self.increment_human_score()
            return("HUMAN")
        elif (human_choice == "ROCK" and comp_choice == "PAPER") or (human_choice == "PAPER" and comp_choice == "SCISSORS") or (
                human_choice == "SCISSORS" and comp_choice == "ROCK"):
            self.increment_comp_score()
            return("COMPUTER")




