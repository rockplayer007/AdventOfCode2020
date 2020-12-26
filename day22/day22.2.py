decks = open('input.txt').read().split('\n\n')
player1 = list(map(int, decks[0].split(':\n')[1].split('\n')))
player2 = list(map(int, decks[1].split(':\n')[1].split('\n')))
turns = 1

def play_recursive(player1, player2):
    # store initial combination first
    memory = set()

    while len(player1) != 0 and len(player2) != 0:
        global turns
        turns += 1

        if (sha := hash((tuple(player1), tuple(player2)))) in memory:
            return player1, player2
        else:
            memory.add(sha)

        card1 = player1.pop(0)
        card2 = player2.pop(0)

        if card1 <= len(player1) and card2 <= len(player2):
            p1, p2 = play_recursive(player1[:card1], player2[:card2])
            if len(p1) == 0:
                player2 += [card2, card1]
            else:
                player1 += [card1, card2]

            continue

        # normal rule
        if card1 > card2:
            player1 += [card1, card2]
        else:
            player2 += [card2, card1]

    return player1, player2


p1, p2 = play_recursive(player1, player2)
winner = p2 if len(p1) == 0 else p1
#print(turns)
print(sum(map(lambda el: (list(reversed(winner)).index(el) + 1) * el, winner)))
