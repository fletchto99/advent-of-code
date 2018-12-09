from blist import blist

with open('input.txt') as f:
  line = f.read().rstrip().split(" ")
  players = [0 for i in range(int(line[0]))]
  max_marble = int(line[6])

  marbles = blist([0])
  current_idx = 0

  for m in range(1,max_marble+1):
    print(m)
    if m % 23 == 0:
      players[(m-1)%len(players)] += m
      current_idx -= 7
      if current_idx < 0:
        current_idx = len(marbles) + current_idx
      players[(m-1)%len(players)] += marbles.pop(current_idx)
    else:
      current_idx += 1
      if current_idx == len(marbles):
        current_idx = 0
      current_idx += 1
      marbles.insert(current_idx, m)

  print(max(players))
