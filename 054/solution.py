#! encoding: utf8
from profile_decorate import profile

"""
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand	 	Player 1	 	Player 2	 	Winner
1	 	5H 5C 6S 7S KD
Pair of Fives
 	2C 3S 8S 8D TD
Pair of Eights
 	Player 2
2	 	5D 8C 9S JS AC
Highest card Ace
 	2C 5C 7D 8S QH
Highest card Queen
 	Player 1
3	 	2D 9C AS AH AC
Three Aces
 	3D 6D 7D TD QD
Flush with Diamonds
 	Player 2
4	 	4D 6S 9H QH QC
Pair of Queens
Highest card Nine
 	3D 6D 7H QD QS
Pair of Queens
Highest card Seven
 	Player 1
5	 	2H 2D 4C 4D 4S
Full House
With Three Fours
 	3C 3D 3S 9S 9D
Full House
with Three Threes
 	Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""


class LevelArray:
    level_array = {
        'high_card': 0,
        'pair': 1,
        'two_pairs': 2,
        'three_of_a_kind': 3,
        'straight': 4,
        'flush': 5,
        'full_house': 6,
        'four_of_a_kind': 7,
        'straight_flush': 8,
    }


def card_map(card):
    if card.isdigit():
        return int(card)
    elif card == 'A':
        return 14
    elif card == 'J':
        return 11
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'T':
        return 10
    else:
        print('Error with {}'.format(card))


class FormedHand:
    def __init__(self, level_type, cards):
        self.level = LevelArray.level_array[level_type]
        self.card_list = cards


def is_left_win(left, right):
    if left.level > right.level:
        return True
    elif left.level == right.level:
        for idx, card in enumerate(left.card_list):
            if card > right.card_list[idx]:
                return True
            elif card < right.card_list[idx]:
                return False
            else:
                pass
        else:
            return False
    else:
        return False


def decide_hand_level(card_array):
    type_array = list()
    number_array = list()

    for card in card_array:
        number_array.append(card_map(card[0:1]))
        type_array.append(card[1:])

    if len(set(type_array)) == 1:
        is_flush = True
    else:
        is_flush = False

    sort_by_type = [i[1] for i in sorted([[number_array.count(x), x] for x in set(number_array)], reverse=True)]

    for num in sort_by_type:
        if number_array.count(num) == 4:
            return FormedHand(level_type='four_of_a_kind', cards=sort_by_type)
        elif number_array.count(num) == 3:
            if len(sort_by_type) == 2:
                return FormedHand(level_type='full_house', cards=sort_by_type)
            else:
                return FormedHand(level_type='three_of_a_kind', cards=sort_by_type)
        elif number_array.count(num) == 2:
            if len(sort_by_type) == 3:
                return FormedHand(level_type='two_pairs', cards=sort_by_type)
            elif len(sort_by_type) == 4:
                return FormedHand(level_type='pair', cards=sort_by_type)
        else:
            if min(sort_by_type)+4 == max(sort_by_type):
                if is_flush:
                    return FormedHand(level_type='straight_flush', cards=sorted(sort_by_type, reverse=True))
                else:
                    return FormedHand(level_type='straight', cards=sorted(sort_by_type, reverse=True))
            else:
                if is_flush:
                    return FormedHand(level_type='flush', cards=sorted(sort_by_type, reverse=True))
                else:
                    return FormedHand(level_type='high_card', cards=sorted(sort_by_type, reverse=True))


@profile
def main():
    fh = open('p054_poker.txt')
    player1_win_cnt = 0
    for line in fh.readlines():
        card_array = line.split()
        player1_hand = decide_hand_level(card_array[:5])
        player2_hand = decide_hand_level(card_array[5:])

        if is_left_win(player1_hand, player2_hand):
            player1_win_cnt += 1

    print('Player 1 win {} hands'.format(player1_win_cnt))


if __name__ == '__main__':
    main()
