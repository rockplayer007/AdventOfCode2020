decks = open('input.txt').read().split('\n\n')
player1 = list(map(int, decks[0].split(':\n')[1].split('\n')))
player2 = list(map(int, decks[1].split(':\n')[1].split('\n')))

counter = 1
while len(player1) != 0 and len(player2) != 0:

    card1 = player1.pop(0)
    card2 = player2.pop(0)

    if card1 > card2:
        player1 += [card1, card2]
    else:
        player2 += [card2, card1]

    counter += 1

winner = player2 if len(player1) == 0 else player1
print(sum(map(lambda el: (list(reversed(winner)).index(el) + 1) * el, winner)))




