#!/usr/bin/python3
from Player import Player
from Board import Board
from Game import Game
import Constants

def main():
    choice = input("Player 1 makes the first move. Will you be player 1 or player 2 (enter 1 or 2): ")
    while choice not in "12":
        choice = input("Invalid option. Enter 1 or 2: ")

    human = Player(Constants.HUMAN)
    computer = Player(Constants.COMPUTER)

    if choice is '1':
        human.setCharacter("X")
        human.setTurn()
        computer.setCharacter("O")
    else:
        human.setCharacter("O")
        computer.setCharacter("X")
        computer.setTurn()

    print("======================================================================================================")
    print("For each move, enter position values 1-9. 1 being the top left spot and 9 being the bottom right spot.")
    print("The computer runs " + str(Constants.SIMULATIONS) + " simulations on each possible move it can make on a "
                                                             "given state.")
    print("======================================================================================================")
    gameBoard = Board([Board.EMPTYCHARACTER for i in range(Board.BOARDLENGTH)])
    Game(gameBoard, human, computer)

if __name__ == '__main__': main()