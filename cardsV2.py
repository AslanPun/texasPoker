import random

card_num = [1,2,3,4,5,6,7,8,9,10,11,12,13]
card_suit = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
card_value = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
card_deck = []
table_cards = []

def create_deck():
    for i in range(0, len(card_suit)):
        for j in range(0, len(card_value)):
            card_deck.append((card_value[j], card_suit[i]))

def shuffle():
    random.shuffle(card_deck)


def get_card_value(card):
    if card[0] == 'Ace':
        return 14
    elif card[0] == 'Two':
        return 2
    elif card[0] == 'Three':
        return 3
    elif card[0] == 'Four':
        return 4
    elif card[0] == 'Five':
        return 5
    elif card[0] == 'Six':
        return 6
    elif card[0] == 'Seven':
        return 7
    elif card[0] == 'Eight':
        return 8
    elif card[0] == 'Nine':
        return 9
    elif card[0] == 'Ten':
        return 10
    elif card[0] == 'Jack':
        return 11
    elif card[0] == 'Queen':
        return 12
    elif card[0] == 'King':
        return 13


def get_card_order(card):
    if card[0] == 'Ace':
        return 1
    elif card[0] == 'Two':
        return 2
    elif card[0] == 'Three':
        return 3
    elif card[0] == 'Four':
        return 4
    elif card[0] == 'Five':
        return 5
    elif card[0] == 'Six':
        return 6
    elif card[0] == 'Seven':
        return 7
    elif card[0] == 'Eight':
        return 8
    elif card[0] == 'Nine':
        return 9
    elif card[0] == 'Ten':
        return 10
    elif card[0] == 'Jack':
        return 11
    elif card[0] == 'Queen':
        return 12
    elif card[0] == 'King':
        return 13
    


# Path: cards.py
def get_card_name(card):
    return card[0] + ' of ' + card[1]

def deal_card():
    return card_deck.pop()

def deal_1_card_to_player(player):
    player.hand.append(deal_card())

def deal_2_cards_to_player(player):
    deal_1_card_to_player(player)
    deal_1_card_to_player(player)

def deal_2_cards_to_each_player():
    for i in range(0, len(player_list)):
        deal_2_cards_to_player(player_list[i])


def deal_1_card_to_table():
    table_cards.append(deal_card())

def deal_5_cards_to_table():
    deal_1_card_to_table()
    deal_1_card_to_table()
    deal_1_card_to_table()
    deal_1_card_to_table()
    deal_1_card_to_table()

def get_card_deck():
    return card_deck

def get_card_num():
    return card_num

def get_card_suit():
    return card_suit

def print_table_cards():
    for i in range(0, len(table_cards)):
        print(get_card_name(table_cards[i]))

############# player start ##################
#create a player class
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hand_card = 0
        self.hand_rank = ""

def create_players():
    global player_list
    player_list = []
    for i in range(0,5):
        player_list.append(Player('Player ' + str(i+1)))
    

def print_players_hand():
    for i in range(0, len(player_list)):
        print(player_list[i].name)
        for j in range(0, len(player_list[i].hand)):
            print(get_card_name(player_list[i].hand[j]))
        print('\n')

############# player end #################

############# compare hands to the table START ##################
from collections import Counter
def check_for_pairs_with_table(player):
    player_and_table_cards = player.hand + table_cards
    player_and_table_cards_value = []
    for card in player_and_table_cards:
        player_and_table_cards_value.append(get_card_value(card))
    counts = dict(Counter(player_and_table_cards_value))
    duplicates = {key:value for key, value in counts.items() if value > 1}
    try:
        max_dup = max(duplicates.values())
    except:
        max_dup = 1
    try:
        high_card = max(duplicates, key=duplicates.get)
    except:
        high_card = max(player_and_table_cards_value)
    
    player.high_card = high_card
    if max_dup == 1:
        player.hand_rank = 'High Card'
    elif max_dup == 2:
        player.hand_rank = 'Pair'
    elif max_dup == 3:
        player.hand_rank = '3 of a kind'
    elif max_dup == 4:
        player.hand_rank = '4 of a kind'


def has_consecutive_five(numbers): # helper function for check_for_straight
    if len(numbers) < 5:
        return False
    numbers.sort()
    for i in range(len(numbers) - 4):
        if numbers[i + 4] - numbers[i] == 4:
            return True
    return False

def check_for_straight(player):
    player_and_table_cards = player.hand + table_cards
    player_and_table_cards_value = []
    for card in player_and_table_cards:
        player_and_table_cards_value.append(get_card_order(card))
    unique = list(set(player_and_table_cards_value))
    if has_consecutive_five(unique):
        player.hand_rank = 'Straight'
        player.high_card = max(unique)


def check_for_flush(player):
    player_and_table_cards = player.hand + table_cards
    player_and_table_cards_value = []
    for card in player_and_table_cards:
        player_and_table_cards_value.append(get_card_value(card))
    player_and_table_cards_suit = []
    for card in player_and_table_cards:
        player_and_table_cards_suit.append(card[1])
    counts = dict(Counter(player_and_table_cards_suit))
    duplicates = {key:value for key, value in counts.items() if value > 4}
    if len(duplicates) > 0:
        player.hand_rank = 'Flush'
        player.high_card = max(player_and_table_cards_value)



############# compare hands to the table END ##################


def main():
    create_players()
    create_deck()
    shuffle()
    deal_2_cards_to_each_player()
    deal_5_cards_to_table()
    print_players_hand()
    print_table_cards()
    check_for_pairs_with_table(player_list[0])
    check_for_straight(player_list[0])
    check_for_flush(player_list[0])
    print(player_list[0].hand_rank)
    print(player_list[0].high_card)

    



if __name__ == '__main__':
    main()