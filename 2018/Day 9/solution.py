from blist import blist

with open('input.txt') as f:
    line = f.read().rstrip().split(" ")
    players = [0 for i in range(int(line[0]))]
    marbles = blist([0])
    current_idx = 0

    for m in range(1, int(line[6]) + 1):
        if m % 23 == 0:
            players[(m - 1) % len(players)] += m
            current_idx = (current_idx - 7) % len(marbles)
            players[(m - 1) % len(players)] += marbles.pop(current_idx)
        else:
            current_idx = (current_idx + 2) % len(marbles)
            marbles.insert(current_idx, m)

    print(max(players))
