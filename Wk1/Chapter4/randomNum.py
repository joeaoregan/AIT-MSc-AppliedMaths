#!/usr/bin/env python3

# Pig Dice game

import random

# global variables
turn = 1
score = 0
scoreThisTurn = 0
turnOver = False
gameOver = False


def main():
    display_rules()
    play_game()


def display_rules():
    print("Let's Play PIG!")
    print
    print("* See how many turns it takes you to get to 20.")
    print("* Turn ends when you hold or roll a 1.")
    print("* If you roll a 1, you lose all points for the turn.")
    print("* if you hold, you save all points for the turn.")
    print


def play_game():
    while not gameOver:
        take_turn()
    print
    print("Game over!")


def take_turn():
    global turnOver

#    print("TURN", turn)
    print("TURN" + str(turn))
    turnOver = False
    while not turnOver:
        choice = raw_input("Roll or hold? (r/h): ")
        if choice == "r":
            roll_die()
        elif choice == "h":
            hold_turn()
        else:
            print("Invalid choice. Try again.")


def roll_die():
    global turn, scoreThisTurn, turnOver
    die = random.randint(1, 6)
    print("Die: " + str(die))
    if die == 1:
        scoreThisTurn = 0
        turn += 1
        print("Turn over. No score.\n")
        turnOver = True
    else:
        scoreThisTurn += die


def hold_turn():
    global turn, scoreThisTurn, score, turnOver, gameOver
    print("Score for turn: " + str(scoreThisTurn))
    score += scoreThisTurn
    scoreThisTurn = 0
    print("Total score: " + str(score) + "\n")

    turnOver = True
    if score >= 20:
        gameOver = True
        print("You finished in " + str(turn) + " turns!")
    turn += 1


if __name__ == "__main__":
    main()
