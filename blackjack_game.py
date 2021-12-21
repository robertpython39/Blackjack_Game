 # Blackjack / 21 game
import random
from replit import clear

print(''' Welcome to:\n
88          88                       88        88                       88
88          88                       88        ""                       88
88          88                       88                                 88
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a
                                              ,88
                                            888P"                                  ''')

def deal_card():
    card_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(card_deck)
    return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) == 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_function(user_score, computer_score):
    if user_score == computer_score:
        return "Draw! "
    elif computer_score == 0:
        return "Lose, the opponent has a Blackjack 😈"
    elif user_score == 0:
        return "You win with a Blackjack 😇"
    elif user_score > 21:
        return "Sorry, mate. You lose. 🥺"
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_cards = []
    dealer_cards = []
    is_game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"     Your cards: {user_cards}, current score: {user_score}")
        print(f"     Dealer's first card {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21 :
            is_game_over = True
        else:
           user_should_deal =  input("Type 'yes' to get another card or 'no' to pass: ").lower()
           if user_should_deal == 'yes':
               user_cards.append(deal_card())
           elif user_should_deal == "no":
               is_game_over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        computer_score = calculate_score(dealer_cards)


    print(f"     Your final hand is {user_cards} and the final score is {user_score}")
    print(f"     Dealer's final hand is {dealer_cards} and the final score is {dealer_cards}")
    print(compare_function(user_score, dealer_score))

while input("Welcome to BLACKJACK! You want to play the game? (yes/no):-->  ").lower() == "yes":
    clear()
    play_game()