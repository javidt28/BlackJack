""" This is a Game of Blackjack """
import random
import time

def get_card_value(cards):
    """ This function gets the vslue of the cards  """
    total_card_val = 0
    aces = 0

    cads = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]

    # for cad in cards:
    #     if cad == cads:
    #         total_card_val = int(cad)
    #     elif cards == "A":
    #         aces += 10
    #         total_card_val = 1
    #     else:
    #         total_card_val = 10
    # while aces != 0 or total_card_val - 10 < 12:
    #     total_card_val += 10
    #     aces -= 10
    # return total_card_val

    for cad in cards:
        if cad in cads:
            total_card_val += int(cad)
        elif cad == "A":
            # aces += 10
            aces += 1
        else:
            total_card_val += 10

    while aces != 0:
        if (total_card_val + 11) < 21:
            total_card_val += 11
        else:
            total_card_val += 1
        aces -= 1
    return total_card_val

def get_dealer_hand():
    """ This function gets the hand of the dealer """

    dealer_cards = []
    dealer_cards += get_card()
    dealer_cards += get_card()
    while get_card_value(dealer_cards) < 17:
        dealer_cards.append(get_card())
    return dealer_cards

def is_bust(cards):
    """ This function determines if burst or not """
    if get_card_value(cards) > 21:
        return True
    return False


def get_card():
    """ This function is getting the value of the cards """
    rand_card = random.randint(1, 13)

    face_cards = {1: "A", 11: "J", 12: "Q", 13: "K"}
    if rand_card in face_cards:
        return face_cards[rand_card]
    return str(rand_card)

def get_user_decision():
    """ This function gets the user decision """

    hit = 'H'
    stay = 'S'
    user_decision = input("Would you like to hit (H) or stay (S)? ")
    user_decision = user_decision.upper()
    while (user_decision not in hit and user_decision not in stay):
        print("Please insert H or S")
        user_decision = (input("Would you like to hit (H) or stay (S)? "))
    return user_decision

def cards_print_out(plc, cards):
    """ This function prints out the value of the cards """

    result = plc + " cards are "
    for card in cards:
        result += card + ' '

    return result

def play_a_turn():
    """ This function responsible for a turn """

    # cards = []
    # cards.append(get_card())
    # cards.append(get_card())
    cards = [get_card(), get_card()]
    user_decision = " "

    while user_decision != "S":
        print(cards_print_out("Your", cards))
        user_decision = get_user_decision()
        if user_decision == "H":
            cards.append(get_card())
        if is_bust(cards):
            print(cards)
            print("You busted! You lose!")
            return False

    dealer_cards = get_dealer_hand()
    print(cards_print_out("Your", cards))
    print(cards_print_out("Dealer's", dealer_cards))
    your_value = get_card_value(cards)
    dealer_cards = get_dealer_hand()
    dealers_value = get_card_value(dealer_cards)

    if your_value > dealers_value or is_bust(cards):
        print("You win!")
        return True
    # else:
    print("You lose!")
    return False

def get_time(start_time):
    """ This function keeps track or the time """

    time_in_sec = time.time() - start_time
    seconds = int(time_in_sec // 60)
    sec_mins = int(time_in_sec / 60)
    return str(seconds) + "." + str(sec_mins).zfill(2)


def play_game(initial_bet):
    """ This function is the Welcome function for the game """

    print("Welcome to Blackjack")

    initial = initial_bet
    start_time = time.time()
    play_more = True


    while initial > 0 and play_more:
        print("Welcome to another round.")
        print("You have been playing for " + str(get_time(start_time)) + " minutes.")

        bet = input("How much would you like to bet? ")
        win = play_a_turn()
        if win:
            initial += int(bet)
        else:
            initial -= int(bet)

        print("You currently have $" + str(initial))
        play_more_input = input("Would you like to play more? (Y or N) ")
        play_more = play_more_input.upper() == "Y"

        if play_more_input.upper() == "N":
            play_more = False

# This makes sure that we only run the play game when the blackjack
# program is the "main" program.
# You don't have to change anything underneath this.
if __name__ == "__main__":
    INITIAL_BET = int(input("Please insert how much $$$ you want to start with: "))
    play_game(INITIAL_BET)
