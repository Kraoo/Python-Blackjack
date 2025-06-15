import bj_functions

user_play = str(input("Do you want to play blackjack?\n(Y/N)\n"))

while user_play in["yes", "y"]:
    bj_functions.blackjack()
    break
