import sys
import random

# get a new shuffle deck when there are not many cards left in a deck
def get_new_deck():
    deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 32
    random.shuffle(deck)
    return deck


# deal two cards to each player
def deal(deck):
    hand = [deck.pop(), deck.pop()]
    return hand


# calculate the total point of each hand 
def calculate_hand(hand):
    point = 0
    aces = ["A" for card in hand if card == "A"]
    hand = [card for card in hand if card != "A"]

    total = sum([int(card) if card not in ["J", "Q", "K"] else 10 for card in hand])
    total = total + len(aces) if not aces or total + len(aces) > 11 else total + len(aces) + 10

    return total

def dealer_hit(hand):
    return calculate_hand(hand) <= 16 or (calculate_hand(hand) == 17 and "A" in hand)


def play(number_of_player, deck):
    print("Welcome to black jack")
    

    dealer_hand = deal(deck)
    players_hand = [deal(deck) for _ in range(number_of_player)]

    # choices for players
    for i, hand in enumerate(players_hand):
        print("dealder's hand is ", "[*, ", dealer_hand[-1], "]")
        if calculate_hand(hand) == 21:
             print("black jack!!!!!.\n")
             break
        # let player to choose hit or stand
        while True:
            print("You current hand is ", hand, " with total of %d. You can choose to hit(h) for another card or stand(s).\n" % calculate_hand(hand))
            # assert the choice typed in is either h or s
            while True: 
                choice = input().lower()
                if choice not in ['h', "s"]:
                    print("you can only type in h for hit and s for stand\n")
                else:
                    break

            if choice == "h":
                hand.append(deck.pop())
                print("you got an", hand[-1], ".\n")
                hand_point = calculate_hand(hand)

                if hand_point == 21:
                    print("congratulations, you got 21.\n")
                    break
                elif hand_point > 21:
                    print("Sorry player #%d, you are busted.\n" % i)
                    break
                else:
                    print("your current point is %d.\n" % calculate_hand(hand))

            else:
                break


    # hittings for dealer
    print("dealder's hand is ", dealer_hand, ".\n")
    while dealer_hit(dealer_hand):
        dealer_hand.append(deck.pop())
        print("dealder hit and got an", dealer_hand[-1], ".\n")

    dealder_point = calculate_hand(dealer_hand)
    players_point = [calculate_hand(hand) for hand in players_hand]

    for i, v in enumerate(players_point):
        print("dealder's hand is", dealer_hand, " with total of %d.\n" % dealder_point)
        if v > 21 or (dealder_point <= 21 and v < dealder_point):
            print("sorry, player #%d, you lose.\n" % i)
        elif v == dealer_hand:
            print("a tie game.\n")
        else:
            print("congratulations, player %d, you win.\n" % i)

    return None

if __name__ == "__main__":
    number_of_player = int(sys.argv[1])
    deck = []
    print("press 1 if you wanna play.\n")
    choice = input()
    while choice == "1":
    	print(len(deck))
    	if len(deck) <= 100:
        	deck = get_new_deck()
    	play(number_of_player, deck)
    	print("press 1 to keep playing.\n")
    	choice = input()





















