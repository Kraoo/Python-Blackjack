import random
import bj_art
import bj_dict

def hit_user_card(hit_user_choice, user_card, user_total, com_total, com_card):
    while True:
        user_next_card = random.choice(list(bj_dict.cards.values()))
        user_total += user_next_card
        print(f"Your card is {user_next_card}")
        if user_total > 21:
            print(f"\nTotal: {user_total}\nYou Lose :(")
            return user_total
        elif user_total == 21:
            print("You cannot hit, you are at 21.")
            continue
        else:
            print(f"\nTotal: {user_total}")
        hit_user_choice = str(input("Hit again?\n(Y/N)\n")).lower()
        if hit_user_choice in ["yes", "y"]:
            True
        elif hit_user_choice in ["no", "n"]:
            print(f"The computer cards are {' & '.join(str(card) for card in com_card)}")
            hit_com_card(user_total, com_total, com_card)
            return
        else:
            print("Invalid Input")
            continue
def hit_com_card(user_total, com_total, com_card):
    while True:
        if com_total > 21:
            print(f"The computer total is {com_total}\nYOU WIN")
            return False
        elif com_total > user_total and user_total < 21:
            print(f"The computer total is {com_total}\nYou Lose :(")
            return False
        elif com_total < user_total and user_total < 21:
            com_next_card = random.choice(list(bj_dict.cards.values()))
            com_total += com_next_card
            print(f"The computer drew {com_next_card}\n")
            True
        elif user_total == 21:
            com_next_card = random.choice(list(bj_dict.cards.values()))
            com_total += com_next_card
            if com_total == 21:
                print(f"Your total: {user_total}\nCom total: {com_total}\nIt's a draw")
                return False
            elif com_total > 21:
                print(f"The computer total is {com_total}\nYOU WIN")
                return False
def continue_playing():
    while True:
        play_again = str(input("Do you want to play agian?\n(Y/N)\n"))
        if play_again in ["yes", "y"]:
            blackjack()
            return False
        elif play_again in ["no", "n"]:
            print("Thank you for playing! Goodbye")
            return False

def blackjack():
    print(bj_art.logo)
    # User starting cards
    user_card = random.choices(list(bj_dict.cards.values()), k=2)
    user_total = sum(user_card)
    print(f"Your cards are {' & '.join(str(card)for card in user_card)}\nYour total: {user_total}\n")

    # Computer starting cards
    com_card = random.choices(list(bj_dict.cards.values()), k=2)
    com_total = sum(com_card)
    print(f"The computer cards are {com_card[0]}, and ?\n")

    # Ask user if they want to hit
    hit_user_choice = str(input("Do you want to hit?\n(Y/N)\n")).lower()
    if hit_user_choice in ["yes", "y"]:
        hit_user_card(hit_user_choice, user_card, user_total, com_total, com_card)
    elif hit_user_choice in ["no", "n"]:
        print(f"The computer cards are {' & '.join(str(card) for card in com_card)}")
        hit_com_card(user_total, com_total, com_card)
    
    # Ask the user if they want to play again
    continue_playing()
