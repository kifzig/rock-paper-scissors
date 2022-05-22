"""This python program launches a Rock, Paper, Scissors game that can be played against a computer with a
graphical user interface created with TKinter. The human can choose to play as many rounds as they like, and can
make their choices of Rock, Paper, or Scissors through the user interface."""

from game_brain import GameBrain
from game_interface import GameInterface
import pydoc


game_brain = GameBrain()
"""Game brain instantiates the operations maker of Rock, Paper, Scissors"""

game_interface = GameInterface(game_brain)
"""We pass the game brain to the game interface so that in can launch the operations through the interface"""



