import random
playerIn = True
dealerIn = True
"""
11 = J
12 = Q
13 = K
14 = A
"""

deck = [2,3,4,5,6,7,8,9,10,'J','Q','K','A',1,2,3,4,5,6,7,8,9,10,'J','Q','K','A',
        2,3,4,5,6,7,8,9,10,'J','Q','K','A',1,2,3,4,5,6,7,8,9,10,'J','Q','K','A']

player_hand = []
dealer_hand = []

def deal_the_cards(turn):
        dealed_card = random.choice(deck)
        turn.append(dealed_card)
        deck.remove(dealed_card)

def total(turn):
        faces = ['J','Q','K']
        total = 0
        for dealed_card in turn:
                if dealed_card in range(1,11):
                        total += dealed_card
                elif dealed_card in faces:
                        total += 10
                else:
                        if total > 11:
                                total += 1
                        else:
                                total += 10
        return total

for _ in range(2):
        deal_the_cards(player_hand)
        deal_the_cards(dealer_hand)


while playerIn or dealerIn:
        print(f'U have {player_hand} for total {total(player_hand)} and Dealer have {dealer_hand[0]} and ? for {total(dealer_hand)}')
        if playerIn:
                stayOrHit = input('1 : Stay\n2 : Hit\n')
        if total(dealer_hand) >= 16:
                dealerIn = False
        else:
                deal_the_cards(dealer_hand)
        if stayOrHit == '1':
                playerIn = False
        else:
                deal_the_cards(player_hand)
        # if total(player_hand) >= 21:
        #         print('You bust! Dealer wins')
        #         break
        # elif total(dealer_hand) >= 21:
        #         break

        if total(player_hand) == 21:
                print(f'\nYou have {player_hand} for a total {total(player_hand)} and the dealer has {dealer_hand} for a total '
                      f'of {total(dealer_hand)}')
                print('BLACKJACK !!! You win!')
        elif total(dealer_hand) == 21:
                print(f'\nYou have {player_hand} for a total {total(player_hand)} and the dealer has {dealer_hand} for a total '
                      f'of {total(dealer_hand)}')
                print('BLACKJACK!!! Dealer wins!')
        elif total(player_hand) > 21:
                print(f'\nYou have {player_hand} for a total {total(player_hand)} and the dealer has {dealer_hand} for a total '
                      f'of {total(dealer_hand)}')
                print('You bust! Dealer wins')
                break
        elif total(dealer_hand) > 21:
                print(f'\nYou have {player_hand} for a total {total(player_hand)} and the dealer has {dealer_hand} for a total '
                      f'of {total(dealer_hand)}')
                print('Dealer bust! You win')
                break
        elif 21 - total(dealer_hand) < 21 - total(player_hand):
                print(f'\nYou have {player_hand} for a total {total(player_hand)} and the dealer has {dealer_hand} for a total '
                      f'of {total(dealer_hand)}')
                print('Dealer wins')
        elif 21 - total(dealer_hand) > 21 - total(player_hand):
                print(f'\nYou have {player_hand} for a total {total(player_hand)} and the dealer has {dealer_hand} for a total '
                      f'of {total(dealer_hand)}')
                print('Congrats! You win')
        elif total(dealer_hand) == total(player_hand):
                print("It's a draw ")
