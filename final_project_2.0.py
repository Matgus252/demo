# This file was created by Matthew Gustafson
# https://www.youtube.com/watch?v=s99L7ctOGkk (42:02)


import random

deck = list('234567890JQKA*4')
random.shuffle(deck)
value = {'2':2, '3':3, '4':4, '4':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':1}
player = [deck.pop() for _ in range(2)]
cpu = [deck.pop() for _ in range(2)]

def check(who, hand):
    subtotal = sum(map(value.get, hand))
    if subtotal > 21:
        return print('{} loses.'.format(who), *hand)
    if len(hand) > 4:
        return print('{} wins.'.format(who), *hand)  
    total = [subtotal] + list(range(subtotal+10, subtotal+10*hand.count('A')+1,10)))
    if 21 in total:
        return print('{} wins.'.format(who), *hand)
    return total

while check('Player', player) and check ('CPU', cpu):
    print(*player)
    p = input('Enter to stay. ')
    if p:
        player.append(deck.pop())
    ai = sum(map(value.get, cpu)) < 15
    if ai:
        cpu.append(deck.pop())
    if not p and not ai:
        if p > 